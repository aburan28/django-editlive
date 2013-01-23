# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, View
from django.template import RequestContext, Template
from django.http import HttpResponse

from test_app.models import EditliveBaseFieldsTest, EditliveBaseFieldsTest2

TEST_TEMPLATE = """
{%% extends "test_app/base.html" %%}
{%% load editlive_tags %%}
{%% block content %%}
<div class="span12">
    <h1>{{ field|capfirst }}Field</h1>
    <h3>Test: {{ options }}</h3>
    {%% editlive "object.%(fieldname)s" %(options)s as test %%}{{ test }}
</div>
{%% endblock %%}
"""

class TestView(View):
    def get(self, request, field):
        options = []
        for k in request.GET.keys():
            options.append('%s="%s"' % (k, request.GET.get(k)))

        fieldname = field.endswith('2') and field[:-1] or field
        model = field.endswith('2') and EditliveBaseFieldsTest2\
                                    or EditliveBaseFieldsTest

        tpl = TEST_TEMPLATE % {
            'fieldname': fieldname + '_test',
            'options': ' '.join(options),
        }

        t = Template(tpl)
        c = RequestContext(request, {
            'field': field,
            'object': model.objects.all()[0],
        })

        return HttpResponse(t.render(c))


class HomeView(View):
    def get(self, request):
        return HttpResponse(Template('').render(RequestContext(request, {})))
