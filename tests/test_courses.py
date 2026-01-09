import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        page_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(page_title).to_be_attached()
        expect(page_title).to_have_text("Courses")

        not_results_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(not_results_title).to_be_attached()
        expect(not_results_title).to_have_text("There is no results")

        empty_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_icon).to_be_attached()
        expect(empty_icon).to_be_visible()

        empty_block_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(empty_block_text).to_have_text("Results from the load test pipeline will be displayed here")