from Components.base_component import BaseComponent
from playwright.sync_api import Page
from Components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.text import Text
from elements.image import Image


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        self.icon = Icon(page, f"{identifier}-image-upload-widget-info-icon", "Image upload info")
        self.title = Text(
            page, f"{identifier}-image-upload-widget-info-title-text", "Image upload info title"
        )
        self.description = Text(
            page, f"{identifier}-image-upload-widget-info-description-text", "Image upload info Description"
        )

        self.upload_button = Button(
            page, f"{identifier}-image-upload-widget-upload-button", "Upload image"
        )
        self.upload_input = FileInput(page, f"{identifier}-image-upload-widget-input", "Upload")

        self.image = Image(page, f'{identifier}-image-upload-widget-preview-image', 'Preview')
        self.remove_button = Button(
            page, f'{identifier}-image-upload-widget-remove-button', 'Remove image'
        )

    def check_visible(self, is_image_uploaded: bool = False):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text('Tap on "Upload image" button to select file')

        self.description.check_visible()
        self.description.check_have_text('Recommended file size 540X300')

        self.upload_button.check_visible()

        if is_image_uploaded:
            self.remove_button.check_visible()
            self.image.check_visible()

        if not is_image_uploaded:
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self):
        self.remove_button.click()

    def upload_preview_image(self, file: str):
        self.upload_input.upload_file(file)



