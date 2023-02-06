from BasePage.BaseApp import BasePage


class ClickButton(BasePage):

    def checkandclick(self, locator_button):
        return self.find_element(locator_button).click()

