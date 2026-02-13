from Components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from Components.views.empty_view_component import EmptyViewComponent


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        self.icon = page.get_by_test_id(f"{identifier}-image-upload-widget-info-icon")
        self.title = page.get_by_test_id(f"{identifier}-image-upload-widget-info-title-text")
        self.description = page.get_by_test_id(f"{identifier}-image-upload-widget-info-description-text")

        self.upload_button = page.get_by_test_id(f"{identifier}-image-upload-widget-upload-button")
        self.upload_input = page.get_by_test_id(f"{identifier}-image-upload-widget-input")

        self.image = page.get_by_test_id(f"{identifier}-image-upload-widget-preview-image")
        self.remove_button = page.get_by_test_id(f"{identifier}-image-upload-widget-remove-button")

    def check_visible(self, uploaded_file: bool = False):
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Tap on "Upload image" button to select file')

        expect(self.description).to_be_visible()
        expect(self.description).to_have_text("Recommended file size 540X300")

        expect(self.upload_button).to_be_visible()

        if uploaded_file:
            expect(self.remove_button).to_be_visible()

            expect(self.image).to_be_visible()

        if not uploaded_file:
            self.preview_empty_view.check_visible(
                    "No image selected",
                    "Preview of selected image will be displayed here"
            )

    def click_upload_button(self):
        self.upload_button.click()

    def click_remove_button(self):
        self.remove_button.click()

    def upload_file(self, file: str):
       self.upload_input.set_input_files(file)



