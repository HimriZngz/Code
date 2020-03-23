from selenium import webdriver  # 导入包或函数

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')

diver = webdriver.Firefox(executable_path='C:/Program Files/Mozilla Firefox/geckodriver.exe')  # 创建浏览器对象

diver.get('https://www.dogedoge.com')  # 请求页面

# 页面的基本操作，点击、输入
diver.find_elements_by_id('search_form_input_homepage').send_keys('Python')  # 以id查找到输入框元素并进行输入
diver.find_elements_by_id('search_button_homepage').click()  # 查找到“搜索”按钮，并点击




