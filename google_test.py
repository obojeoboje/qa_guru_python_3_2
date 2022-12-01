from selene.support.shared import browser
from selene import be, have


def test_google_selene(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter() #Вводим нужное значение в поиск и жмем ввод
    browser.element('[id="search"]').should(have.text('Selene - Wikipedia')) #Проверяем что на странице присутствует 'Selene - Wikipedia'

def test_google_cats(open_browser):
    browser.element('[name="q"]').should(be.blank).type('cats').press_enter() #Вводим нужное значение в поиск и жмем ввод
    browser.element('[id="search"]').should(have.no.text('dogs')) #Проверяем что на странице НЕ присутствует 'dogs'