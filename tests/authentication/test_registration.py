import pytest
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.registration
@pytest.mark.regression
class TestRegistration:
        def test_successfully_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
                registration_page.visit(
                        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

                registration_page.input.fill(email="email@yande.ru", username="username", password="user12345")
                registration_page.click_registration_button()

                dashboard_page.toolbar.check_visible()