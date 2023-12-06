import unittest
from appium import webdriver
from page_object.gallery_page import GalleryPage


class TestMovie(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            "platformName": "Android",
            "platformVersion": "12",
            "appPackage": "com.sec.android.gallery3d",
            "appActivity": "com.samsung.android.gallery.app.activity.GalleryActivity",
            "newCommandTimeout": 30
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

    def tearDown(self):
        self.driver.quit()

    def test_create_movie(self):
        expected_text = "Select items"
        gallery_page = GalleryPage(self.driver)
        gallery_page.open_gallery_and_click_on_albums()
        actual_text = gallery_page.create_a_movie()
        self.assertEqual(actual_text, expected_text, f"Expected text: '{expected_text}', Actual text: '{actual_text}'")


if __name__ == "__main__":
    unittest.main()
