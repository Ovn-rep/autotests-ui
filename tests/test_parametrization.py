import pytest
from playwright.sync_api import Playwright, Page

users = {
    "+78923": "user with email and password",
    "+76523": "user with email",
    "+75324": "user with password"
}


@pytest.mark.parametrize(
    'numbers',
    users.keys(),
    ids = lambda numbers: f"{numbers}: {users[numbers]}"
)
def test_users_auth_with_phone_numbers(chromium_page: Page, numbers: str):
    ...
