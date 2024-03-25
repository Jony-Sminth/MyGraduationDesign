from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time

browser_options = Options()
browser_options.add_argument("--headless")  # 无头模式，可选
browser_options.add_argument("--disable-gpu")  # 禁用 GPU 加速，可选
browser = webdriver.Chrome(executable_path='D:\ChromeDriver\chromedriver.exe', options=browser_options)  # 注意这里要指定 chromedriver.exe 的完整路径
headers = {'user-agent': 'https://s.weibo.com/?Refer='}
print("browser has been built")

def get_cookie(url='https://weibo.com/login.php'):
    url = url
    browser.get(url)
    print("During the 25 seconds, scan the code to login to your account")
    time.sleep(25)
    with open('cookies.txt', 'w') as f:
        f.write(json.dumps(browser.get_cookies()))
        f.close
    print("Got cookie successfully!")

if __name__ == '__main__':
    get_cookie()
