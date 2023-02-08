from BasePage.BaseApp import BasePage


class ClickButton(BasePage):

    def check_and_click(self, locator_button):
        return self.find_element(locator_button).click()

