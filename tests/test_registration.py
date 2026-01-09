from playwright.sync_api import sync_playwright, expect, Page

def test_successfull_registration(chromium_page: Page):

        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill("email@yande.ru")

        username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill("username")

        password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill("user12345")

        registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        dashboard_title = chromium_page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_title).to_be_visible()