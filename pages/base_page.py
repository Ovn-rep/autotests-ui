from typing import Pattern
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url, wait_until='networkidle')

    def reload(self):
        self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expect_url: Pattern[str]):
        expect(self.page).to_have_url(expect_url)