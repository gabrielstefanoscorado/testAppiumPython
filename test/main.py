import pytest
from appium import webdriver
from page_object.gallery_page import GalleryPage


class TestMovie:

    @pytest.fixture
    def driver(self, request):
        desired_cap = {
            "platformName": "Android",
            "platformVersion": "12",
            "appPackage": "com.sec.android.gallery3d",
            "appActivity": "com.samsung.android.gallery.app.activity.GalleryActivity",
            "newCommandTimeout": 30
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        request.addfinalizer(driver.quit)
        return driver

    def test_create_movie(self, driver):
        expected_text = "Select items"
        gallery_page = GalleryPage(driver)
        gallery_page.open_gallery_and_click_on_albums()
        assert gallery_page.create_a_movie() == expected_text, f"Expected text: '{expected_text}'" \
                                                               f", Actual text: '{gallery_page.create_a_movie()}'"
