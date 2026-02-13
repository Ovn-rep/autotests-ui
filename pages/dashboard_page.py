from Components.charts.chart_view_component import ChartViewComponent
from Components.dashboard.dashboard_toolbar_view_component import DashboardToolbarComponent
from Components.navigation.navbar_component import NavbarComponent
from Components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = DashboardToolbarComponent(page)
        self.students_chart = ChartViewComponent(page, identifier = "students", chart_type = "bar")
        self.activities_chart = ChartViewComponent(page, identifier="activities", chart_type="line")
        self.courses_chart = ChartViewComponent(page, identifier="courses", chart_type="pie")
        self.scores_chart = ChartViewComponent(page, identifier="scores", chart_type="scatter")