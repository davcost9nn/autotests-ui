import pytest
from playwright.sync_api import sync_playwright, Page, Playwright

from pages.authentication.registration_page import RegistrationPage


@pytest.fixture
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()


@pytest.fixture(scope='session')
def initialize_browser_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        registration_page = RegistrationPage(page=page)
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='user.name@gmail.com',username ='username',password='password')
        registration_page.click_registration_button()

        context.storage_state(path="browser-state.json")
        browser.close()

@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state) -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        state_path = "browser-state.json"
        context = browser.new_context(storage_state=state_path)
        page = context.new_page()
        yield page
        browser.close()
