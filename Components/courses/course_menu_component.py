from Components.base_component import BaseComponent
from playwright.sync_api import Page
from elements.button import Button


class CourseMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, 'course-view-menu-button', "Menu")
        self.edit_button = Button(page, 'course-view-edit-menu-item', "Edit")
        self.delete_button = Button(page, 'course-view-delete-menu-item', "Delete")

    def click_edit_button(self, index: int):
        self.menu_button.click(nth = index)

        self.edit_button.check_visible(nth = index)
        self.edit_button.click(nth = index)

    def click_delete_button(self, index: int):
        self.menu_button.click(nth = index)

        self.delete_button.check_visible(nth=index)
        self.delete_button.click(nth=index)
