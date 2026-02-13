from Components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id("create-course-form-title-input").locator("input")
        self.estimated_time = page.get_by_test_id(
            "create-course-form-estimated-time-input"
        ).locator("input")
        self.description = page.get_by_test_id(
            "create-course-form-description-input"
        ).locator("textarea").first
        self.max_score = page.get_by_test_id("create-course-form-max-score-input").locator("input")
        self.min_score = page.get_by_test_id("create-course-form-min-score-input").locator("input")

    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title.fill(title)
        expect(self.title).to_have_value(title)

        self.estimated_time.fill(estimated_time)
        expect(self.estimated_time).to_have_value(estimated_time)

        self.description.fill(description)
        expect(self.description).to_have_value(description)

        self.max_score.fill(max_score)
        expect(self.max_score).to_have_value(max_score)

        self.min_score.fill(min_score)
        expect(self.min_score).to_have_value(min_score)

    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_value(title)

        expect(self.estimated_time).to_be_visible()
        expect(self.estimated_time).to_have_value(estimated_time)

        expect(self.description).to_be_visible()
        expect(self.description).to_have_value(description)

        expect(self.max_score).to_be_visible()
        expect(self.max_score).to_have_value(max_score)

        expect(self.min_score).to_be_visible()
        expect(self.min_score).to_have_value(min_score)