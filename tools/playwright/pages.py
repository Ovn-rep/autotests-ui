import allure
from playwright.sync_api import Playwright, Page


def initialize_page(playwright: Playwright, test_name: str, storage_state: str|None=None) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=storage_state, record_video_dir='./videos')
    context.tracing.start(snapshots=True, screenshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=f"./tracing/{test_name}.zip")
    browser.close()

    allure.attach.file(source=f'./tracing/{test_name}.zip', extension='zip', name="trace")
    allure.attach.file(page.video.path(), name="video", attachment_type=allure.attachment_type.WEBM)
