from selene import browser, be, have


def test_google_should_find_selene(browser_set_size, browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('selene: User-oriented Web UI browser tests in Python'))


def test_google_should_not_find_anything(browser_set_size, browser_open):
    browser.element('[name="q"]').should(be.blank).type("thereisnowayyоu'llfindanything").press_enter()
    # browser.element('[class="card-section"] [role="heading"]').should(have.text("Результатов: примерно 0"))
    browser.element('[class="card-section"] [role="heading"]').should(have.text("По запросу thereisnowayyоu'llfindanything ничего не найдено."))
