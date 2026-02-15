import pytest
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
        def test_successful_authorization(
                self,
                login_page: LoginPage,
                registration_page: RegistrationPage,
                dashboard_page: DashboardPage
        ):
                registration_page.visit(
                        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
                )
                registration_page.input.fill(email = "alm@al.ru", username = "Alexk", password = "Alexk127")
                registration_page.click_registration_button()

                dashboard_page.navbar.check_visible(username = "Alexk")
                dashboard_page.toolbar.check_visible()
                dashboard_page.sidebar.check_visible()
                dashboard_page.sidebar.click_logout()

                login_page.input.fill(email = "alm@al.ru", password = "Alexk127")
                login_page.click_login_button()

                dashboard_page.navbar.check_visible(username="Alexk")
                dashboard_page.toolbar.check_visible()
                dashboard_page.sidebar.check_visible()

        @pytest.mark.parametrize(
                "email, password", [
                        ('user.name@gmail.com', 'password'),
                        ('user.name@gmail.com', '  '),
                        ('  ', 'password')
                ]
        )
        def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
                login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
                login_page.input.fill(email=email, password=password)
                login_page.click_login_button()
                login_page.check_wrong_email_or_password_alert()

        def test_navigate_from_authorization_to_registration(
                self,
                registration_page: RegistrationPage,
                login_page: LoginPage
        ):
                login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
                login_page.click_registration_link()

                registration_page.input.check_visible(email = "", username = "", password = "")
