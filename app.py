import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

opts = Options()
opts.headless=False

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=opts)
driver.get("https://gmail.com")
time.sleep(1)

try:

    login_input = driver.find_element_by_name("identifier")
    login_input.send_keys("metodageek@gmail.com")
    later_input = driver.find_element_by_id("identifierNext")
    later_input.click()
    time.sleep(2)
    pass_func = driver.find_element_by_name('password')
    pass_func.send_keys('#pasta1111')
    nextBtn = driver.find_element_by_id('passwordNext')
    time.sleep(1)
    nextBtn.click()
    time.sleep(4)

    mailsTbl = driver.find_element_by_xpath("//table[@class='F cf zt']")
    mails = mailsTbl.find_elements_by_xpath("//tr[@class='zA yO']")
    for mail in mails:
        # currMail = mail.find_element_by_xpath("//td[@class='yX xY ']")
        currMail = mail.find_element_by_xpath("//td[@class='yX xY ']")
        subject = mail.text.split('\n')[1]
        print(subject)
except NoSuchElementException:
    print("Error !!!")

driver.quit()
