from selenium import webdriver


class LoginTest(object):
    def test_valid_login(self):
        base_url = "https://letskodeit.teachable.com/"

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)

        login_link = driver.find_element_by_xpath('//a[@class = "navbar-link fedora-navbar-link"]')
        login_link.click()

        email_field = driver.find_element_by_xpath('//input[@id="user_email"]')
        email_field.send_keys("test@email.com")

        password_field = driver.find_element_by_xpath('//input[@id="user_password"]')
        password_field.send_keys("abcabc")

        login_button = driver.find_element_by_xpath('//input[@name = "commit"]')
        login_button.click()

        # avatar = driver.find_element_by_xpath('//img[@class = "gravatar"]')
        avatar = driver.find_elements_by_xpath('//img[@class = "gravatar"]')
        if avatar:
            print("Login Successful")
        else:
            print("Login Failed")

ff = LoginTest()
ff.test_valid_login()
