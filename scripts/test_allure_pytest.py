import allure

@allure.step("Opening browser") # название шага
def open_browser():
    with allure.step("Get browser"): # вложенный шага
        ...

    with allure.step("Starting browser"):
        ...

@allure.step("Creating course with '{title}'")
def create_course(title: str):
    ...

@allure.step("Close browser")
def close_browser():
    ...


def test_features():
    open_browser()
    create_course(title = "Playwright")
    close_browser()
