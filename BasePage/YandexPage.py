
from BasePage.BaseApp import BasePage
from selenium.webdriver.common.by import By
from factory_page.button import ClickButton
from factory_page.field import ClickAndWriteField
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search3__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")


class SearchHelper(BasePage):

    def enter_word(self, word):
        field = ClickAndWriteField(self.driver)
        field.check_and_click(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD, "hello")

    def click_on_the_search_button(self):
        button = ClickButton(self.driver)
        button.check_and_click(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON)

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR,time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu
