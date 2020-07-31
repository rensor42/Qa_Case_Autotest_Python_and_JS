from selenium import webdriver
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "https://qa-routes.praktikum-services.ru"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(2)

        # Код, который заполняет обязательные поля
        print("Шаг 1: ввод часов и минут")
        input1 = browser.find_element_by_id('form-input-hour')
        input1.send_keys("08")
        input2 = browser.find_element_by_id('form-input-minute')
        input2.send_keys("00")

        print("Шаг 2: заполнение поля Откуда")
        input3 = browser.find_element_by_id('form-input-from')
        input3.send_keys("Усачева, 3")

        print("Шаг 3: заполнение поля Куда")
        input4 = browser.find_element_by_id('form-input-to')
        input4.send_keys("Комсомольский проспект, 18")

        print("Шаг 4: выбор режима Свой");
        button = browser.find_element_by_id("form-mode-custom")
        button.click()

        print("Шаг 5: выбор вида транспорта")
        button = browser.find_element_by_id("from-type-taxi")
        button.click()    
                
        print("Ожидание элемента с результатом")
        message = browser.find_element_by_id("result-time-price")
        message_text = message.text

        print("Проверка")
        self.assertEqual(message_text, "Такси ~ 22 руб.\nВ пути 2 мин.")

if __name__ == "__main__":
    unittest.main()