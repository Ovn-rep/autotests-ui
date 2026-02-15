import pytest
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_create_course(self, create_course_page: CreateCoursePage, course_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.create_courses_toolbar.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="", estimated_time="", description="",
            max_score="0", min_score="0"
        )

        create_course_page.create_exercises_toolbar.check_visible()
        create_course_page.check_visible_create_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright", estimated_time="2 weeks", description="Playwright",
            max_score="100", min_score="10"
        )

        create_course_page.create_courses_toolbar.click_create_course_button()

        course_list_page.toolbar.check_visible()
        course_list_page.course_card.check_visible(
            index=0, title="Playwright",
            max_score="100", min_score="10",
            estimated_time="2 weeks"
        )

    def test_empty_courses_list(self, course_list_page: CoursesListPage):
        course_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        course_list_page.navbar.check_visible("username")
        course_list_page.sidebar.check_visible()

        course_list_page.toolbar.check_visible()
        course_list_page.check_visible_empty_course()

    def test_edit_course(self, create_course_page: CreateCoursePage, course_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.create_course_form.fill(
            title="Playwright", estimated_time="2 weeks", description="Playwright",
            max_score="100", min_score="10"
        )
        create_course_page.image_upload_widget.upload_preview_image(file = "testdata/files/image.png")
        create_course_page.create_courses_toolbar.click_create_course_button()
        course_list_page.course_card.check_visible(
            index = 0, title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )

        course_list_page.course_card.menu.click_edit_button(0)
        create_course_page.create_course_form.fill(
            title="Agaaga", estimated_time="3 weeks", description="Agaaga",
            max_score="100000", min_score="10000999"
        )

        create_course_page.create_courses_toolbar.click_create_course_button()
        course_list_page.course_card.check_visible(
            index=0, title="Agaaga",
            estimated_time="3 weeks",
            max_score="100000",
            min_score="10000999"
        )




