# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementExpection


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm Abir')

mgs = "Selenium rocks!!!!"
options = webdriver.ChromeOptions()

options.add_argument(r'--user-data-dir=C:\Users\Dell\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome("C:\\Users\\Dell\\Downloads\\chromedriver.exe", options=options)
driver.get("https://web.whatsapp.com/")

time.sleep(5)

user_name_list = ['Nahid Miu']
search_box = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]")
try:
    search_box.send_keys(user_name_list)
    search_box.click()
except NoSuchElementExpection as se:
    print("There is no person in your contact list")
except Exception:
    driver.close()

for user_name in user_name_list:
    try:

        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        # user = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]".format(user_name))
        user.click()
    except NoSuchElementExpection as se:
        print("There is no person in your contact list")
    except Exception:
        driver.close()
time.sleep(5)

message_box = driver.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]")

time.sleep(3)

message_box.send_keys(mgs)

message_box = driver.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[2]/button/span")
# message_box.click()
#message_status = driver.find_element_by_xpath(
#    "/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div/span")
#print("Status: " + str(message_status))

logout = driver.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[3]/div/span")
logout.click()
logout_btn = driver.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[3]/span/div[1]/ul/li[5]/div[1]")
#logout_btn.click()
'''
confirm_logout = driver.find_element_by_xpath(
    "/html/body/div[1]/div[1]/span[2]/div[1]/div/div/div/div/div/div[3]/div[2]/div/div")
confirm_logout.click()
'''
time.sleep(2)
'''
if message_status == "Read":
    print("Read")
elif message_status == "Delivered":
    print("Delivered")
else:
    print(message_status)
'''
time.sleep(2)

driver.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
