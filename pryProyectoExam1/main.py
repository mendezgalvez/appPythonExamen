import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class TestSelectSelenium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()

    @unittest.skip("temp")
    def test_suma_dos_numeros(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
        text_input_1 = driver.find_element_by_xpath("//input[@id='sum1']")
        text_input_2 = driver.find_element(By.XPATH, "//input[@id='sum2']")
        total_button = driver.find_element_by_xpath("//button[contains(text(),'Get Total')]")
        text_outut = driver.find_element_by_xpath('//*[@id="displayvalue"]')

        text_input_1.send_keys('4')
        text_input_2.send_keys('6')
        total_button.click()
        self.assertEqual('10', text_outut.text)

    @unittest.skip("temp")
    def test_check_all_checkbutton(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

        time.sleep(2)
        options_list = [
            "//label[text()='Option 1']",
            "//label[text()='Option 2']",
            "//label[text()='Option 3']",
            "//label[text()='Option 4']",
        ]

        for s in options_list:
            check_button = driver.find_element_by_xpath(s)
            check_button.click()
        # self.driver.find_element(By.CSS_SELECTOR, ".checkbox:nth-child(3) .cb1-element").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".checkbox:nth-child(4) .cb1-element").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".checkbox:nth-child(5) .cb1-element").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".checkbox:nth-child(6) .cb1-element").click()
        time.sleep(5)
        check_all_button = driver.find_element_by_id('check1')
        button_text = check_all_button.get_attribute('value')
        self.assertEqual(button_text, "Uncheck All")

    def test_check_radio_button(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

        radio_button_male = driver.find_element_by_xpath(
            "//body/div[@id='easycont']/div[1]/div[2]/div[2]/div[2]/div[1]/label[1]/input[1]"
        )
        radio_button_0_5 = driver.find_element_by_xpath(
            "//body[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/label[1]/input[1]"
        )
        get_values_button = driver.find_element_by_xpath(
            "//button[contains(text(),'Get values')]"
        )
        text_output = driver.find_element_by_xpath(
            "//body/div[@id='easycont']/div[1]/div[2]/div[2]/div[2]/p[2]"
        )

        radio_button_male.click()
        radio_button_0_5.click()
        get_values_button.click()
        self.assertRegex(text_output.text, "Male")
        self.assertRegex(text_output.text, "0 - 5")


if __name__ == '__main__':
    unittest.main()
