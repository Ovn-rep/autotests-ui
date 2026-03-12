import allure
from elements.base_element import BaseElement
from playwright.sync_api import expect, Locator
from tools.playwright.logger import get_logger


logger = get_logger("INPUT")

class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "input"

    def get_by_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_by_locator(nth, **kwargs).locator('input')

    def fill(self, text: str, nth: int = 0, **kwargs):
        step = f"Fill {self.type_of} '{self.name}' to value '{text}'"
        with allure.step(step):
            locator = self.get_by_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(text)

    def check_have_value(self, text: str, nth: int = 0, **kwargs):
        step = f"Checking that {self.type_of} '{self.name}' has a value '{text}'"
        with allure.step(step):
            locator = self.get_by_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(text)
