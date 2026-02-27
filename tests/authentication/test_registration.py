import pytest
import allure
from allure_commons.types import Severity
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.registration
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
class TestRegistration:
        @allure.title('Check registration with correct email, username and password')
        @allure.severity(Severity.CRITICAL)
        def test_successfully_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
                registration_page.visit(
                        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

                registration_page.input.fill(email="email@yande.ru", username="username", password="user12345")
                registration_page.click_registration_button()

                dashboard_page.toolbar.check_visible()