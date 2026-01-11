from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')

    def fill_registration_form(self):
        self.email_input.fill("email@yande.ru")
        expect(self.email_input).to_have_value("email@yande.ru")

        self.username_input.fill("username")
        expect(self.username_input).to_have_value("username")

        self.password_input.fill("user12345")
        expect(self.password_input).to_have_value("user12345")

    def click_registration_button(self):
        self.registration_button.click()

