import pytest
from selene.support.shared import browser

@pytest.fixture() #Открытие страницы гугла в браузере
def open_browser():
    browser.config.window_height = 720
    browser.config.window_width = 1280
    browser.open('https://google.com')

