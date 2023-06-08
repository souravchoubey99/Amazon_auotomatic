import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options =Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(3.5)
driver.get("https://www.amazon.in/")
log_in = driver.find_element("xpath","//span[text() = 'Hello, sign in']")
log_in.click()
log_in_step_1 = driver.find_element("xpath","//input[@type = 'email']")
log_in_step_1.send_keys(9305038724)
log_in_step_2 = driver.find_element("xpath","//span[@id = 'continue']")
log_in_step_2.click()
log_in_step_3 = driver.find_element("xpath","//input[@type = 'password']")
log_in_step_3.send_keys(987654321)
# nd_log_in_step_3 =driver.find_element("xpath","//input[@id='ap_password'")
# nd_log_in_step_3.send_keys(6205360927)

sig_in = driver.find_element("xpath","//input[@id = 'signInSubmit']")
sig_in.click()

search_box = driver.find_element("xpath","//input[@type='text']")
search_box.send_keys("iphone")
time.sleep(2)
first_option = driver. find_element("xpath","//div[@aria-label = 'iphone 14']")
first_option.click()

order_choose = driver.find_element("xpath","//img[@alt = 'Sponsored Ad - Apple iPhone 14 Plus (256 GB) - Purple']")
order_choose.click()
driver.switch_to.window(driver.window_handles[1])
choose_color = driver.find_element("xpath","//img[@alt = 'Red']")
choose_color.click()
choose_ram = driver.find_element("xpath","//p[text() = '512 GB']")
choose_ram.click()
order_place_2nd =driver.find_element("xpath","//input[@id = 'buy-now-button']")
order_place_2nd.click()
 