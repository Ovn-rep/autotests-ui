from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from Components.navigation.navbar_component import NavbarComponent
from Components.navigation.sidebar_component import SidebarComponent
from Components.views.empty_view_component import EmptyViewComponent
from Components.courses.course_toolbar_component import CourseToolbarComponent
from Components.courses.course_view_component import CourseViewComponent


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.empty_view = EmptyViewComponent(page, 'courses-list')
        self.course_card = CourseViewComponent(page)
        self.toolbar = CourseToolbarComponent(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

    def check_visible_empty_course(self):
        self.empty_view.check_visible(
            "There is no results",
            "Results from the load test pipeline will be displayed here"
        )

