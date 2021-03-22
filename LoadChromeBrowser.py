from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/how-to-invoke-the-chrome-browser-in-selenium-with-python")
