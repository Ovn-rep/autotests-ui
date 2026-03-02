import pytest
import allure
from config import settings
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION, AllureTag.USER_LOGIN)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
class TestAuthorization:
        @allure.title("Check login with correct email and password")
        @allure.severity(Severity.BLOCKER)
        def test_successful_authorization(
                self,
                login_page: LoginPage,
                registration_page: RegistrationPage,
                dashboard_page: DashboardPage
        ):
                registration_page.visit(AppRoute.REGISTRATION)
                registration_page.input.fill(
                        email = settings.test_user.email,
                        username = settings.test_user.username,
                        password = settings.test_user.password
                )
                registration_page.click_registration_button()

                dashboard_page.navbar.check_visible(username = settings.test_user.username)
                dashboard_page.toolbar.check_visible()
                dashboard_page.sidebar.check_visible()
                dashboard_page.sidebar.click_logout()

                login_page.input.fill(email = settings.test_user.email, password = settings.test_user.password)
                login_page.click_login_button()

                dashboard_page.navbar.check_visible(username=settings.test_user.username)
                dashboard_page.toolbar.check_visible()
                dashboard_page.sidebar.check_visible()

        @pytest.mark.parametrize(
                "email, password", [
                        ('user.name@gmail.com', 'password'),
                        ('user.name@gmail.com', '  '),
                        ('  ', 'password')
                ]
        )
        @allure.title('Check login with wrong email or password')
        @allure.severity(Severity.CRITICAL)
        def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
                login_page.visit(AppRoute.LOGIN)
                login_page.input.fill(email=email, password=password)
                login_page.click_login_button()
                login_page.check_wrong_email_or_password_alert()

        @allure.title("Check navigation from login page to registration page ")
        @allure.severity(Severity.NORMAL)
        def test_navigate_from_authorization_to_registration(
                self,
                registration_page: RegistrationPage,
                login_page: LoginPage
        ):
                login_page.visit(AppRoute.LOGIN)
                login_page.click_registration_link()

                registration_page.input.check_visible(email = "", username = "", password = "")
