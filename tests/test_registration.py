from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

def test_successfully_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_page.input.fill(email = "email@yande.ru", username = "username", password = "user12345")
        registration_page.click_registration_button()

        dashboard_page.check_visible_dashboard_title()