from allure_commons.types import Severity
from config import settings
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
import pytest
import allure
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.dashboard
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.STUDENTS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
class TestDashboard:
    @allure.title('Check displaying of dashboard page')
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        dashboard_page_with_state.toolbar.check_visible()

        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible(settings.test_user.username)

        dashboard_page_with_state.students_chart.check_visible(title="Students")
        dashboard_page_with_state.activities_chart.check_visible(title="Activities")
        dashboard_page_with_state.courses_chart.check_visible(title="Courses")
        dashboard_page_with_state.scores_chart.check_visible(title="Scores")