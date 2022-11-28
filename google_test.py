from selene.support.shared import browser
from selene import be, have

def test_google_search(open_browser, size_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene was inspired by Selenide from Java world.'))

def test_google_search_negative(open_browser, size_browser):
    browser.element('[name="q"]').should(be.blank).type(',mxhjdlkf;msj28jsbf757').press_enter()
    browser.element('.card-section').should(have.text('did not match any documents.'))
