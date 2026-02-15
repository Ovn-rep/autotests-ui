from elements.base_element import BaseElement
from playwright.sync_api import expect, Locator


class Textarea(BaseElement):
    def get_by_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_by_locator(nth, **kwargs).locator('textarea').first

    def fill(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_by_locator(nth, **kwargs)
        locator.fill(text)

    def check_have_value(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_by_locator(nth, **kwargs)
        expect(locator).to_have_value(text)