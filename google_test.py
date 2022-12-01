from selene.support.shared import browser
from selene import be, have


def test_google_selene(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter() #Вводим нужное значение в поиск и жмем ввод
    browser.element('[id="search"]').should(have.text('Selene - Wikipedia')) #Проверяем что на странице присутствует 'Selene - Wikipedia'

def test_google_fake(open_browser):
    browser.element('[name="q"]').should(be.blank).type('fsgdassavcgtaewrcxasd').press_enter() #Вводим нужное значение в поиск и жмем ввод
    browser.element('[id="search"]').should(have.text('нет полезных результатов')) #Проверяем что на странице нет результатов