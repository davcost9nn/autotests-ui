import pytest
from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        courses_results = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        courses_description_results = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')

        expect(courses_title).to_be_visible()
        expect(courses_results).to_be_visible()
        expect(courses_description_results).to_be_visible()
