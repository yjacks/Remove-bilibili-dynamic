from selenium import webdriver
import time, sys,json
from selenium.webdriver.common.by import By


def remove_all(uid,cookies):
    driver = webdriver.Firefox()  # Driver
    driver.get("https://space.bilibili.com/674013151/dynamic")
    # 固定等待
    time.sleep(10)
    ab = json.loads(cookies)
    for cc in ab:
        driver.add_cookie(cc)
    driver.refresh()
    time.sleep(10)
    mmm=1
    while True:
        try:
            f = driver.find_element(By.XPATH,"/html/body/div[2]/div[4]/div/div/div[1]/div/div[1]/div[%d]/div/div/div[2]/div[4]/div"%mmm)
            f.click()
            g = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div[1]/div[%d]/div/div/div[2]/div[4]/div/div/div[2]/div[2]"%mmm)
            g.click()
            v = driver.find_element(By.CSS_SELECTOR, "button.bili-modal__button:nth-child(1)")
            v.click()
            html = driver.execute_script("return document.documentElement.outerHTML")  # 返回页面
            if "你已经到达了世界的尽头" in html:  # 到了最下面
                return True
            driver.refresh()
            time.sleep(5)
        except:
            mmm+=1
            continue
    return k


def get_cookie():
    # 需要人工操作
    web=webdriver.Firefox()
    web.get("https://www.bilibili.com")
    time.sleep(120)
    a=web.get_cookies()
    j=json.dumps(a)
    return j
