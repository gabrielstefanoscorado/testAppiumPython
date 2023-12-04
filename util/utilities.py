from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Utilities:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_element_on_screen_and_click(self, locator, by_type=AppiumBy.XPATH):
        element = self.wait.until(EC.element_to_be_clickable((by_type, locator)))
        element.click()

    def wait_and_click(self, locator, by_type=AppiumBy.XPATH):
        element = self.wait.until(EC.visibility_of_element_located((by_type, locator)))
        element.click()

    def get_element_text(self, locator, by_type=AppiumBy.XPATH):
        element = self.driver.find_element(by_type, locator)
        return element.text

    def scroll_down(self):
        height = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        start_x = width // 2
        start_y = int(height * 0.8)
        end_y = int(height * 0.2)
        self.driver.swipe(start_x, start_y, start_x, end_y, duration=1000)

    def swipe_left(self):
        height = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        start_x = int(width * 0.8)
        end_x = int(width * 0.2)
        start_y = height // 2
        self.driver.swipe(start_x, start_y, end_x, start_y, duration=1000)

    def swipe_right(self):
        height = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        start_x = int(width * 0.2)
        end_x = int(width * 0.8)
        start_y = height // 2
        self.driver.swipe(start_x, start_y, end_x, start_y, duration=1000)

    def scroll_to_element_and_click(self, locator, by_type=AppiumBy.XPATH, max_swipes=5):
        for _ in range(max_swipes):
            try:
                element = self.driver.find_element(by_type, locator)
                if element.is_displayed() and element.is_enabled():
                    self.driver.find_element(by_type, locator).click()
                    return True
            except NoSuchElementException:
                pass
            self.scroll_down()
        return False

    def send_keys_to_element(self, locator, text, by_type=AppiumBy.XPATH):
        element = self.wait.until(EC.visibility_of_element_located((by_type, locator)))
        element.send_keys(text)

    def long_press_element(self, locator, by_type=AppiumBy.XPATH, duration=1000):
        element = self.wait.until(EC.visibility_of_element_located((by_type, locator)))
        action = TouchAction(self.driver)
        action.long_press(element, duration=duration).release().perform()

    def android_back_button(self):
        self.driver.press_keycode(4)

    def android_home_button(self):
        self.driver.press_keycode(3)

    def android_app_switch_button(self):
        self.driver.press_keycode(187)
