import pytest
from playwright.sync_api import Page, Playwright
from pages.authentication.registration_page import RegistrationPage


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        registration_page = RegistrationPage(page = page)
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.input.fill(email = "email@yande.ru", username = "username", password = "user12345")
        registration_page.click_registration_button()

        context.storage_state(path="browser-state.json")

        browser.close()

@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state: None, playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()
        yield page
        browser.close()






