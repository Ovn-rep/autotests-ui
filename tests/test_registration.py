from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from playwright.sync_api import Page

def test_successfull_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_page.fill_registration_form()
        registration_page.click_registration_button()

        dashboard_page.check_dashboard_title_to_be_visible()