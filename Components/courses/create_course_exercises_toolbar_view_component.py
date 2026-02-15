from Components.base_component import BaseComponent
from playwright.sync_api import Page
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "create-course-exercises-box-toolbar-title-text", "Title")
        self.create_exercises_button = Button(
            page, "create-course-exercises-box-toolbar-create-exercise-button", "Create exercises"
        )

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text("Exercises")

        self.create_exercises_button.check_visible()

    def click_create_exercises_button(self):
        self.create_exercises_button.click()