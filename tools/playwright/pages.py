import allure
from config import settings, Browsers
from playwright.sync_api import Playwright, Page
from tools.playwright.mocks import abort_static_mock


def initialize_page(
        playwright: Playwright,
        test_name: str,
        browser_type: Browsers,
        storage_state:
        str|None=None
) -> Page:
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(snapshots=True, screenshots=True, sources=True)
    page = context.new_page()
    abort_static_mock(page)

    yield page

    context.tracing.stop(path=settings.tracing_dir.joinpath(f"{test_name}.zip"))
    browser.close()

    allure.attach.file(source=settings.tracing_dir.joinpath(f'{test_name}.zip'), extension='zip', name="trace")
    allure.attach.file(page.video.path(), name="video", attachment_type=allure.attachment_type.WEBM)
