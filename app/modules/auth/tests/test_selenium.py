import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from app.modules.auth.services import AuthenticationService
from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import close_driver, initialize_driver

authentication_service = AuthenticationService()


def test_login_and_check_element():

    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the login page
        driver.get(f"{host}/login")

        # Wait a little while to make sure the page has loaded completely
        time.sleep(4)

        # Find the username and password field and enter the values
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")

        email_field.send_keys("uvlhub.reply@gmail.com")
        password_field.send_keys("uvl12hub34")

        # Send the form
        password_field.send_keys(Keys.RETURN)

        # Wait a little while to ensure that the action has been completed
        time.sleep(4)

        # Insert the email key
        clave = authentication_service.get_validation_email_key()
        print(clave)
        key_field = driver.find_element(By.NAME, "key")
        key_field.send_keys(clave)
        key_field.send_keys(Keys.RETURN)

        try:

            driver.find_element(
                By.XPATH,
                "//h1[contains(@class, 'h2 mb-3') and contains(., 'Latest datasets')]",
            )
            print("Test passed!")

        except NoSuchElementException:
            raise AssertionError("Test failed!")

    finally:

        # Close the browser
        close_driver(driver)


# Call the test function
# test_login_and_check_element()
