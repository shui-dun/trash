import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import random
import time

# 自动填“问卷星”

if __name__ == '__main__':
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})
    driver = uc.Chrome(options=options)
    driver.get("https://www.wjx.cn/vm/PgndNFc.aspx")
    divs = driver.find_elements(By.CSS_SELECTOR, '.field.ui-field-contain')
    for div in divs:
        ty = div.get_attribute("type")
        if ty == "1":
            inp = div.find_element(By.TAG_NAME, "input")
            inp.send_keys("hello world")
        elif ty == "3":
            a = div.find_elements(By.CLASS_NAME, "jqradio")
            random.choice(a).click()
        elif ty == "4":
            a = div.find_elements(By.CLASS_NAME, "jqcheck")
            for i in range(len(a) // 2):
                random.choice(a).click()
    time.sleep(1)
    button = driver.find_element(By.ID, "ctlNext")
    button.click()
    driver.quit()
