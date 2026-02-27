import allure

from elements.base_element import BaseElement


class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return "file input"

    def upload_file(self, file: str, nth: int = 0, **kwargs):
        with allure.step(f"Set file '{file}' to the {self.type_of} {self.name}"):
            locator = self.get_by_locator(nth, **kwargs)
            locator.set_input_files(file)