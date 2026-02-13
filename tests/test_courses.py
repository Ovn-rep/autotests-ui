import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


def test_create_course(create_course_page: CreateCoursePage, course_list_page: CoursesListPage):

        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.create_courses_toolbar.check_visible(is_create_course_disabled = True)
        create_course_page.image_upload_widget.check_visible(uploaded_file=False)
        create_course_page.create_course_form.check_visible(
            title= "", estimated_time="", description="",
            max_score="0", min_score="0"
        )

        create_course_page.create_exercises_toolbar.check_visible()
        create_course_page.check_visible_create_exercises_empty_view()

        create_course_page.image_upload_widget.upload_file('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(uploaded_file=True)
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

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(course_list_page: CoursesListPage):
    course_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    course_list_page.navbar.check_visible("username")
    course_list_page.sidebar.check_visible()

    course_list_page.toolbar.check_visible()
    course_list_page.check_visible_empty_course()









