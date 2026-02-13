from Components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class CourseCreateExercisesComponent(BaseComponent):
    def click_delete_button(self):
        delete_button = self.page.get_by_test_id(
            f"create-course-exercise-car-delete-exercise-button"
        )
        delete_button.click()

    def check_visible(self, index: int, title: str, description: str):
        subtitle = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-subtitle-text"
        )

        title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        ).locator("input")

        description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        ).locator("input")

        expect(subtitle).to_be_visible()
        expect(subtitle).to_have_value(f"#{index + 1} Exercise")

        expect(title_input).to_be_visible()
        expect(title_input).to_have_value(title)

        expect(description_input).to_be_visible()
        expect(description_input).to_have_value(description)

    def fill_exercise_form(self, index: int, title: str, description: str):
        exercise_input_title = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        ).locator("input")

        exercise_input_description = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        ).locator("input")

        exercise_input_title.fill(title)
        expect(exercise_input_title).to_have_value(title)

        exercise_input_description.fill(description)
        expect(exercise_input_description).to_have_value(description)



