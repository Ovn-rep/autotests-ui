from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")

    def check_dashboard_title_to_be_visible(self):
        expect(self.dashboard_title).to_be_visible()