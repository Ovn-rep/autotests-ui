from playwright.sync_api import sync_playwright, expect, Page

def test_wrong_email_or_password_authorization(chromium_page: Page):
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        user_name_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        user_name_input.fill('username')

        password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('Password')

        registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        header_dashboard = chromium_page.get_by_test_id('dashboard-toolbar-title-text')

        expect(header_dashboard).to_be_visible()
        expect(header_dashboard).to_have_text('Dashboard')