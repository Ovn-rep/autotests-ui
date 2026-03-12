import allure
from elements.base_element import BaseElement
from tools.playwright.logger import get_logger


logger = get_logger("FILE_INPUT")

class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return "file input"

    def upload_file(self, file: str, nth: int = 0, **kwargs):
        step = f"Set file '{file}' to the {self.type_of} {self.name}"
        with allure.step(step):
            logger.info(step)
            locator = self.get_by_locator(nth, **kwargs)
            locator.set_input_files(file)