import pytest
from playwright.sync_api import Page, expect
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


def test_create_course(create_course_page: CreateCoursePage, course_list_page: CoursesListPage):

        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.check_visible_create_course_title()
        create_course_page.check_disabled_create_course_button()
        create_course_page.check_visible_preview_empty_view()
        create_course_page.chek_visible_create_course_form(
                title= "",estimated_time="",
                description="", max_score="0",
                min_score="0"
        )
        create_course_page.check_visible_create_exercises_title()
        create_course_page.check_visible_create_exercises_button()
        create_course_page.check_visible_create_exercises_empty_view()

        create_course_page.upload_preview_file('./testdata/files/image.png')
        create_course_page.check_visible_with_uploaded_image(uploaded_image=True)
        create_course_page.fill_create_course_form(
                title="Playwright", estimated_time="2 weeks",
        description="Playwright", max_score="100",
               min_score="10"
        )
        create_course_page.click_create_course_button()

        course_list_page.check_visible_course_title()
        course_list_page.chek_visible_create_course_button()
        course_list_page.check_visible_course_card(
                index=0, text="Playwright",
                max_score_text="100", min_score_text="10",
                estimated_time_text="2 weeks"
        )

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(course_list_page: CoursesListPage):
    course_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    course_list_page.navbar.check_visible("username")
    course_list_page.sidebar.check_visible()

    course_list_page.check_visible_course_title()
    course_list_page.chek_visible_create_course_button()
    course_list_page.check_visible_empty_course()









