import allure
from elements.base_element import BaseElement
from playwright.sync_api import expect
from tools.playwright.logger import get_logger
from ui_coverage import ActionType


logger = get_logger("BUTTON")

class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "button"

    def check_disabled(self, nth: int = 0, **kwargs):
        step = f"Checking that {self.type_of} {self.name} is disabled"
        with allure.step(step):
            locator = self.get_by_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()

        self.track_coverage(ActionType.DISABLED, nth, **kwargs)

    def check_enabled(self, nth: int = 0, **kwargs):
        step = f"Checking that {self.type_of} {self.name} is enabled"
        with allure.step(step):
            locator = self.get_by_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_enabled()

        self.track_coverage(ActionType.ENABLED, nth, **kwargs)

