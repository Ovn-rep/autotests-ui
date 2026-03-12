from playwright.sync_api import Page


def abort_static_mock(page: Page):
    page.route("**/*.{ico,jpg,png,svg,mp3,mp4,webm,woof,woof2}", lambda route: route.abort())