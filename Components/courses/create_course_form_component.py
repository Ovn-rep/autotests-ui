from Components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Input(page, "create-course-form-title-input", "Title")
        self.estimated_time = Input(page, "create-course-form-estimated-time-input", "Estimated time")
        self.description = Textarea(page, "create-course-form-description-input", "Description")
        self.max_score = Input(page, "create-course-form-max-score-input", "Max score")
        self.min_score = Input(page, "create-course-form-min-score-input", "Min score")

    def fill(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title.fill(title)
        self.title.check_have_value(title)

        self.estimated_time.fill(estimated_time)
        self.estimated_time.check_have_value(estimated_time)

        self.description.fill(description)
        self.description.check_have_value(description)

        self.max_score.fill(max_score)
        self.max_score.check_have_value(max_score)

        self.min_score.fill(min_score)
        self.min_score.check_have_value(min_score)

    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title.check_visible()
        self.title.check_have_value(title)

        self.estimated_time.check_visible()
        self.estimated_time.check_have_value(estimated_time)

        self.description.check_visible()
        self.description.check_have_value(description)

        self.max_score.check_visible()
        self.max_score.check_have_value(max_score)

        self.min_score.check_visible()
        self.min_score.check_have_value(min_score)