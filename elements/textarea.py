from elements.base_element import BaseElement
import allure
from playwright.sync_api import expect, Locator


class Textarea(BaseElement):
    @property
    def type_of(self) -> str:
        return "textarea"

    def get_by_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_by_locator(nth, **kwargs).locator('textarea').first

    def fill(self, text: str, nth: int = 0, **kwargs):
        with allure.step(f"Fill {self.type_of} '{self.name}' to value '{text}'"):
            locator = self.get_by_locator(nth, **kwargs)
            locator.fill(text)

    def check_have_value(self, text: str, nth: int = 0, **kwargs):
        with allure.step(f"Checking that {self.type_of} '{self.name}' has a value '{text}'"):
            locator = self.get_by_locator(nth, **kwargs)
            expect(locator).to_have_value(text)