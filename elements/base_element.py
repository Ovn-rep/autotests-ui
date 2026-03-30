from playwright.sync_api import Page, expect, Locator
import allure
from elements.ui_coverage import tracker
from ui_coverage_tool import ActionType, SelectorType
from tools.playwright.logger import get_logger


logger = get_logger("BASE_ELEMENT")

class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    def type_of(self) -> str:
        return "base element"

    def get_by_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        step = f"Getting element with 'data-testid={locator}' at index = '{nth}'"
        with allure.step(step):
            logger.info(step)
            return self.page.get_by_test_id(locator).nth(nth)

    def get_raw_locator(self, nth: int = 0, **kwargs) -> str:
        return f"//*[@data-testid='{self.locator.format(**kwargs)}'][{nth + 1}]"

    def track_coverage(self, action_type: ActionType, nth: int = 0, **kwargs):
        tracker.track_coverage(
            selector=self.get_raw_locator(nth, **kwargs),
            action_type=action_type,
            selector_type=SelectorType.XPATH
        )

    def click(self, nth: int = 0, **kwargs):
        step = f"Clicking {self.type_of} '{self.name}'"
        with allure.step(step):
            locator = self.get_by_locator(nth, **kwargs)
            logger.info(step)
            locator.click()

        self.track_coverage(ActionType.CLICK, nth, **kwargs)

    def check_visible(self, nth: int = 0, **kwargs):
        step = f"Checking that {self.type_of} '{self.name}' is visible"
        with allure.step(step):
            locator = self.get_by_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

        self.track_coverage(ActionType.VISIBLE, nth, **kwargs)

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        step = f"Checking that {self.type_of} '{self.name} has text '{text}'"
        with allure.step(step):
            locator = self.get_by_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)

        self.track_coverage(ActionType.TEXT, nth, **kwargs)