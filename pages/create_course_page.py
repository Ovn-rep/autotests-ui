from Components.courses.course_create_exercises_component import CourseCreateExercisesComponent
from Components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarComponent
from Components.courses.create_course_form_component import CreateCourseFormComponent
from Components.courses.create_course_toolbar_view_component import CreateCourseToolbarComponent
from Components.navigation.navbar_component import NavbarComponent
from Components.views.empty_view_component import EmptyViewComponent
from Components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.create_courses_toolbar = CreateCourseToolbarComponent(page)
        self.create_exercises_form = CourseCreateExercisesComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.create_exercises_toolbar = CreateCourseExercisesToolbarComponent(page)
        self.create_exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')

    def check_visible_create_exercises_empty_view(self):
        self.create_exercises_empty_view.check_visible(
            "There is no exercises",
            'Click on "Create exercise" button to create new exercise'
        )




