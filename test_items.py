from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_search_button(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-lg")
    assert len(button) > 0, "Кнопки нет"
