from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # number = browser.find_element_by_xpath('//img[@id="treasure"]')
    #
    # answer = browser.find_element_by_id('answer')
    # answer.send_keys(calc(number.get_attribute('valuex')))
    #
    # allow_robot = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
    # allow_robot.click()
    #
    # allow_robot_second = browser.find_element_by_xpath('//input[@id="robotsRule"]')
    # allow_robot_second.click()
    select = browser.find_element_by_xpath('//select[@id="dropdown"]').click()
    numberFirst = browser.find_element_by_xpath('//span[@id="num1"]')
    numberSecond = browser.find_element_by_xpath('//span[@id="num2"]')

    answer = int(numberFirst.text) + int(numberSecond.text)

    print(answer)

    selectAnswer = browser.find_element_by_css_selector(f'[value="{answer}"]').click()

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла