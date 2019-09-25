from selenium import webdriver
import time
import pickle
import json
class LocalStorage:
    def __init__(self, driver):
        self.driver = driver
    def set(self, key, value):
            self.driver.execute_script(\
            "window.localStorage.setItem('{}',{})".format(key, json.dumps(value)))
    def get(self, key=None):
        if key:
            return self.driver.execute_script(\
                    "return window.localStorage.getItem('{}')".format(key))
        else:
            return self.driver.execute_script("""
                    var items = {}, ls = window.localStorage;
                    for (var i = 0, k; i < ls.length; i++)
                    items[k = ls.key(i)] = ls.getItem(k);
                    return items;
                    """)
    def remove(self, key):
        self.driver.execute_script(\
                "window.localStorage.removeItem('{}');".format(key))
    def clear(self):
        self.driver.execute_script(\
        "window.localStorage.clear();") 

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
my_file = open("some.txt")
my_string = my_file.read()
storage = LocalStorage(driver)
if storage.get("CookieClickerGame") == None:
    storage.set("CookieClickerGame", my_string)
    my_file.close()
print(storage.get("CookieClickerGame"))
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)
driver.execute_script("setInterval(() => { document.getElementById('bigCookie').click() }, 10)")
while True:
    my_file = open("some.txt", "w")
    my_file.write(storage.get("CookieClickerGame"))
    my_file.closed
    try:
        try:
            driver.find_element_by_xpath("//*[@class='crate upgrade enabled']").click()
            driver.find_element_by_xpath("//*[@id='shimmer']").click()
        except:
            print("нет доступных апгрейдов")
        try:
            driver.find_element_by_xpath("//*[@class='product unlocked enabled']").click()
        except:
            print("нет доступных товаров")
    except:
        print("Пока")
        driver.quit()

