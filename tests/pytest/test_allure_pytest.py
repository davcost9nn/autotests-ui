import allure

@allure.step("Opening browser")
def open_browser():
    with allure.step('Get browser'):
        ...
@allure.step('Creating course')
def create_browser():
        ...
@allure.step('Closing browser')
def close_browser():
    ...

def test_feature():
    open_browser()

    create_browser()

    close_browser()