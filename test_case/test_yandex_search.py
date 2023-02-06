from BasePage.YandexPage import SearchHelper
import time

def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Hello")
    #time.sleep(2)
    yandex_main_page.click_on_the_search_button()
    time.sleep(2)
    elements = yandex_main_page.check_navigation_bar()
    time.sleep(2)
    assert "anime" in elements

