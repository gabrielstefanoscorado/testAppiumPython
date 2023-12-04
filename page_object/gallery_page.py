from appium.webdriver.common.appiumby import AppiumBy
from util.utilities import Utilities
from page_factory.page_locators import GalleryPageLocator


class GalleryPage:

    def __init__(self, driver):
        self.driver = driver
        self.utilities = Utilities(driver)

    def open_gallery_and_click_on_albums(self):
        self.utilities.go_to_element_on_screen_and_click(GalleryPageLocator.ALBUM_BUTTON, AppiumBy.XPATH)

    def create_a_movie(self):
        self.utilities.go_to_element_on_screen_and_click(GalleryPageLocator.CAMERA_BUTTON, AppiumBy.XPATH)
        self.utilities.go_to_element_on_screen_and_click(GalleryPageLocator.MORE_OPTIONS_BUTTON,
                                                         AppiumBy.ACCESSIBILITY_ID)
        self.utilities.go_to_element_on_screen_and_click(GalleryPageLocator.CREATE_BUTTON, AppiumBy.XPATH)
        self.utilities.go_to_element_on_screen_and_click(GalleryPageLocator.MOVIE_BUTTON, AppiumBy.XPATH)
        header_text = self.utilities.get_element_text(GalleryPageLocator.HEADER_TEXT, AppiumBy.ID)
        return header_text
