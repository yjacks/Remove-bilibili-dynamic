from selenium import webdriver
import time, sys,json
from selenium.webdriver.common.by import By
import selenium.common.exceptions


def remove_all(uid,cookies):
    driver = webdriver.Firefox()  # Driver
    driver.get("https://space.bilibili.com/"+str(uid)+"/dynamic")
    # 固定等待
    time.sleep(5)
    ab = json.loads(cookies)
    for cc in ab:
        driver.add_cookie(cc)
    driver.refresh()
    time.sleep(5)
    mmm=1
    while True:
        try:
            f = driver.find_element(By.XPATH,"/html/body/div[2]/div[4]/div/div/div[1]/div/div[1]/div["+str(mmm)+"]/div/div/div[2]/div[4]/div")
        except selenium.common.exceptions.NoSuchElementException:
            print("Error in find button.Number",mmm)
            mmm += 1
            for i in range(int(mmm/10)):
                driver.execute_script("var q=document.documentElement.scrollTop=" + str(2 ** 20))
            continue
        try:
            f.click()
        except:
            continue
        try:
            g = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div/div[1]/div/div[1]/div["+str(mmm)+"]/div/div/div[2]/div[4]/div/div/div[2]/div[2]")
        except selenium.common.exceptions.NoSuchElementException:
            print("Error in key delete.Number",mmm)
            mmm +=1
            for i in range(int(mmm/10)):
                driver.execute_script("var q=document.documentElement.scrollTop=" + str(2 ** 20))
            continue
        g.click()
        v = driver.find_element(By.CSS_SELECTOR, "button.bili-modal__button:nth-child(1)")
        v.click()
        html = driver.execute_script("return document.documentElement.outerHTML")  # 返回页面
        if "你已经到达了世界的尽头" in html:  # 到了最下面
            return True
        time.sleep(0.3)



def get_cookie():
    # 需要人工操作
    web=webdriver.Firefox()
    web.get("https://www.bilibili.com")
    time.sleep(120)
    a=web.get_cookies()
    j=json.dumps(a)
    return j
