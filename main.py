from unittest import TestCase
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class OttripTest(TestCase):
    def setUp(self):
        """
        Предусловие: зайти на сайт www.onetwotrip.com
        """
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://www.onetwotrip.com/ru")

    def test(self):
        """
        Тест-кейс "Проверка вывода сообщения об ошибке при вводе несуществующего email в форме "забыли пароль""
        Шаги:
        1. Зайти на сайт "www.onetwotrip.com"
        2. Нажать "Личный кабинет"
        3. В открывшемся окне нажимаем "забыли пароль"
        4. В открывшемся окне ввести несуществующий email
        Ожидание:
        Вывод сообщения об ошибке "Пользователя с таким email не существует" в браузере.
        """
        self.driver.find_element_by_class_name("enter").click()
        self.driver.find_element_by_class_name("getNewPas").click()
        self.driver.find_element_by_id("input_remind_email").send_keys("llllll@mail.ru")
        self.driver.find_element_by_css_selector(
            "table.layout:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > button:nth-child(1)").click()
        self.driver.find_element_by_id("RemindAuth")
        error = self.driver.find_element_by_class_name("Error")
        self.assertIn("Пользователя с таким email не существует" in error.text)

    def TearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
