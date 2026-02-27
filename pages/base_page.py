from typing import Pattern
import allure
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f"Opening the {url}"):
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        with allure.step(f"Reloading page with url {self.page.url}"):
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expect_url: Pattern[str]):
        with allure.step(f"Checking that current url matches pattern {expect_url.pattern}"):
            expect(self.page).to_have_url(expect_url)