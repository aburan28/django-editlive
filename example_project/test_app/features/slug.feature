Feature: Slug field tests
    Functional tests for the editlive Slug field

    Scenario: Slugfield Initial state
        Given I access the url "/test/slug/"
        Then I see "input#id_slug_test[name='slug_test'][type='text'][maxlength='50']"
        Then I see a "charField" editlive for "#id_slug_test"
        Then I see "#id_slug_test" is hidden
        Then I see a visible placeholder for "#id_slug_test"

    Scenario: Slugfield Edit mode
        Given I access the url "/test/slug/"
        When I click on the placeholder for "#id_slug_test"
        Then I see "#id_slug_test" is visible

