from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')
    user_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
    user_name_input.fill('username')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('Password')
    registration_button = page.get_by_test_id('registration-page-registration-button')
    page.wait_for_timeout(5000)
    registration_button.click()

    header_dashboard = page.get_by_test_id('dashboard-toolbar-title-text')

    expect(header_dashboard).to_be_visible()
    expect(header_dashboard).to_have_text('Dashboard')