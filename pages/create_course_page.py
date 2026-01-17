from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = page.get_by_test_id("create-course-toolbar-title-text")
        self.create_course_button = page.get_by_test_id("create-course-toolbar-create-course-button")

        self.preview_image = page.get_by_test_id("create-course-preview-image-upload-widget-preview-image")
        self.preview_empty_view_icon = page.get_by_test_id("create-course-preview-empty-view-icon")
        self.preview_empty_view_title = page.get_by_test_id("create-course-preview-empty-view-title-text")
        self.preview_empty_view_description = page.get_by_test_id("create-course-preview-empty-view-description-text")

        self.upload_empty_view_icon = page.get_by_test_id("create-course-preview-image-upload-widget-info-icon")
        self.upload_empty_view_title = page.get_by_test_id("create-course-preview-image-upload-widget-info-title-text")
        self.upload_empty_view_description = page.get_by_test_id(
            "create-course-preview-image-upload-widget-info-description-text"
        )
        self.remove_image_button = page.get_by_test_id(
            "create-course-preview-image-upload-widget-remove-button"
        )
        self.upload_image_button = page.get_by_test_id(
            "create-course-preview-image-upload-widget-upload-button"
        )
        self.upload_image_file = page.get_by_test_id(
            "create-course-preview-image-upload-widget-input"
        )

        self.create_course_input_title = page.get_by_test_id("create-course-form-title-input").locator("input")
        self.create_course_input_estimated_time = page.get_by_test_id(
            "create-course-form-estimated-time-input"
        ).locator("input")
        self.create_course_textarea_description = page.get_by_test_id(
            "create-course-form-description-input"
        ).locator("textarea").first
        self.create_course_input_max_score = page.get_by_test_id("create-course-form-max-score-input").locator("input")
        self.create_course_input_min_score = page.get_by_test_id("create-course-form-min-score-input").locator("input")

        self.create_exercises_title = page.get_by_test_id("create-course-exercises-box-toolbar-title-text")
        self.create_exercises_button = page.get_by_test_id(
            "create-course-exercises-box-toolbar-create-exercise-button"
        )

        self.create_exercises_empty_view_icon = page.get_by_test_id("create-course-exercises-empty-view-icon")
        self.create_exercises_empty_view_title = page.get_by_test_id("create-course-exercises-empty-view-title-text")
        self.create_exercises_empty_view_description = page.get_by_test_id(
            "create-course-exercises-empty-view-description-text"
        )

    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text("Create course")

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_visible_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def check_disabled_create_course_button(self):
        expect(self.create_course_button).to_be_disabled()

    def check_visible_preview_empty_view(self):
        expect(self.preview_empty_view_icon).to_be_visible()

        expect(self.preview_empty_view_title).to_be_visible()
        expect(self.preview_empty_view_title).to_have_text("No image selected")

        expect(self.preview_empty_view_description).to_be_visible()
        expect(self.preview_empty_view_description).to_have_text("Preview of selected image will be displayed here")

    def check_visible_with_uploaded_image(self, uploaded_image: bool = False):
        expect(self.upload_empty_view_icon).to_be_visible()

        expect(self.upload_empty_view_title).to_be_visible()
        expect(self.upload_empty_view_title).to_have_text('Tap on "Upload image" button to select file')

        expect(self.upload_empty_view_description).to_be_visible()
        expect(self.upload_empty_view_description).to_have_text("Recommended file size 540X300")

        expect(self.upload_image_button).to_be_visible()

        if uploaded_image:
            expect(self.remove_image_button).to_be_visible()

    def click_remove_image_button(self):
        self.remove_image_button.click()

    def check_visible_preview_image(self):
        expect(self.preview_image).to_be_visible()

    def upload_preview_file(self, file: str):
        self.upload_image_file.set_input_files(file)

    def chek_visible_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        expect(self.create_course_input_title).to_be_visible()
        expect(self.create_course_input_title).to_have_value(title)

        expect(self.create_course_input_estimated_time).to_be_visible()
        expect(self.create_course_input_estimated_time).to_have_value(estimated_time)

        expect(self.create_course_textarea_description).to_be_visible()
        expect(self.create_course_textarea_description).to_have_value(description)

        expect(self.create_course_input_max_score).to_be_visible()
        expect(self.create_course_input_max_score).to_have_value(max_score)

        expect(self.create_course_input_min_score).to_be_visible()
        expect(self.create_course_input_min_score).to_have_value(min_score)

    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_input_title.fill(title)
        expect(self.create_course_input_title).to_have_value(title)

        self.create_course_input_estimated_time.fill(estimated_time)
        expect(self.create_course_input_estimated_time).to_have_value(estimated_time)

        self.create_course_textarea_description.fill(description)
        expect(self.create_course_textarea_description).to_have_value(description)

        self.create_course_input_max_score.fill(max_score)
        expect(self.create_course_input_max_score).to_have_value(max_score)

        self.create_course_input_min_score.fill(min_score)
        expect(self.create_course_input_min_score).to_have_value(min_score)

    def check_visible_create_exercises_title(self):
        expect(self.create_exercises_title).to_be_visible()
        expect(self.create_exercises_title).to_have_text("Exercises")

    def check_visible_create_exercises_button(self):
        expect(self.create_exercises_button).to_be_visible()

    def click_create_exercises_button(self):
        self.create_exercises_button.click()

    def check_visible_create_exercises_empty_view(self):
        expect(self.create_exercises_empty_view_icon).to_be_visible()

        expect(self.create_exercises_empty_view_title).to_be_visible()
        expect(self.create_exercises_empty_view_title).to_have_text("There is no exercises")

        expect(self.create_exercises_empty_view_description).to_be_visible()
        expect(self.create_exercises_empty_view_description).to_have_text(
            'Click on "Create exercise" button to create new exercise'
        )

    def click_delete_exercise_button(self, index: int):
        delete_exercise_button = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button"
        )
        delete_exercise_button.click()

    def check_visible_exercise_form(self, index: int, title: str, description: str):
        exercise_subtitle = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-subtitle-text"
        )

        exercise_input_title = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        ).locator("input")

        exercise_input_description = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        ).locator("input")

        expect(exercise_subtitle).to_be_visible()
        expect(exercise_subtitle).to_have_value(f"#{index + 1} Exercise")

        expect(exercise_input_title).to_be_visible()
        expect(exercise_input_title).to_have_value(title)

        expect(exercise_input_description).to_be_visible()
        expect(exercise_input_description).to_have_value(description)

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




