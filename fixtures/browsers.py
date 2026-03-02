import pytest
from config import settings
from playwright.sync_api import Page, Playwright
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest
from tools.playwright.pages import initialize_page
from tools.routes import AppRoute


@pytest.fixture
def chromium_page(request: SubRequest,playwright: Playwright) -> Page:
        yield from initialize_page(playwright=playwright, test_name=request.node.name)

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(base_url=settings.get_base_url())
        page = context.new_page()

        registration_page = RegistrationPage(page = page)
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.input.fill(
                email=settings.test_user.email,
                username=settings.test_user.username,
                password=settings.test_user.password
        )
        registration_page.click_registration_button()

        context.storage_state(path=settings.browser_state_file)

        browser.close()

@pytest.fixture
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
        yield from initialize_page(
                playwright=playwright, test_name=request.node.name,
                storage_state=settings.browser_state_file
        )





