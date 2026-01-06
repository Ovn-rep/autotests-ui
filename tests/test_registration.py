from playwright.sync_api import sync_playwright, expect

def test_successfull_registration():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill("email@yande.ru")

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill("username")

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill("user12345")

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path="browser-state.json")