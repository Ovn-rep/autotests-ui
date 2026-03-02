import pytest
import allure
from config import settings
from allure_commons.types import Severity
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.routes import AppRoute


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.ADMINISTRATION)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, create_course_page: CreateCoursePage, course_list_page: CoursesListPage):
        create_course_page.visit(AppRoute.COURSES_CREATE)

        create_course_page.create_courses_toolbar.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="", estimated_time="", description="",
            max_score="0", min_score="0"
        )

        create_course_page.create_exercises_toolbar.check_visible()
        create_course_page.check_visible_create_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
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

    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, course_list_page: CoursesListPage):
        course_list_page.visit(AppRoute.COURSES)

        course_list_page.navbar.check_visible(settings.test_user.username)
        course_list_page.sidebar.check_visible()

        course_list_page.toolbar.check_visible()
        course_list_page.check_visible_empty_course()

    @allure.title('Check edit course')
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, create_course_page: CreateCoursePage, course_list_page: CoursesListPage):
        create_course_page.visit(AppRoute.COURSES_CREATE)

        create_course_page.create_course_form.fill(
            title="Playwright", estimated_time="2 weeks", description="Playwright",
            max_score="100", min_score="10"
        )
        create_course_page.image_upload_widget.upload_preview_image(file = settings.test_data.image_png_file)
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




