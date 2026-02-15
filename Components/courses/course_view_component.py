from Components.base_component import BaseComponent
from playwright.sync_api import Page
from Components.courses.course_menu_component import CourseMenuComponent
from elements.image import Image
from elements.text import Text


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseMenuComponent(page)

        self.title = Text(page, 'course-widget-title-text', "Title")
        self.image = Image(page, 'course-preview-image', "Image")
        self.max_score = Text(page, 'course-max-score-info-row-view-text', "Max score")
        self.min_score = Text(page, 'course-min-score-info-row-view-text', "Min score")
        self.estimated_time = Text(page, 'course-estimated-time-info-row-view-text', "Estimated time")



    def check_visible(self, index: int, title:str, max_score: str, min_score: str, estimated_time: str):
        self.title.check_visible(nth = index)
        self.title.check_have_text(title, nth = index)

        self.image.check_visible(nth = index)

        self.max_score.check_visible(nth=index)
        self.max_score.check_have_text(f"Max score: {max_score}", nth=index)

        self.min_score.check_visible(nth=index)
        self.min_score.check_have_text(f"Min score: {min_score}", nth=index)

        self.estimated_time.check_visible(nth=index)
        self.estimated_time.check_have_text(f"Estimated time: {estimated_time}", nth=index)



