from playwright.sync_api import sync_playwright, Request, Response

request_listener = lambda request: print(f'Request: {request}')
respones_listener = lambda respones: print(f'Respones: {respones}')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.on('request', request_listener)
    page.on('response', respones_listener)
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    page.wait_for_timeout(3000)