from BasePage.BaseApp import BasePage


class ClickAndWriteField(BasePage):

    def check_and_click(self, locator_field, request):
        field = self.find_element(locator_field)
        field.click()
        field.send_keys(request)
        return field
