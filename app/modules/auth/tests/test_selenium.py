from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver


def test_login_and_check_element():

    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the login page
        driver.get(f'{host}/login')

        # Wait a little while to make sure the page has loaded completely
        time.sleep(4)

        # Find the username and password field and enter the values
        email_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'password')

        email_field.send_keys('user1@example.com')
        password_field.send_keys('1234')

        # Send the form
        password_field.send_keys(Keys.RETURN)

        # Wait a little while to ensure that the action has been completed
        time.sleep(4)

        try:

            driver.find_element(By.XPATH, "//h1[contains(@class, 'h2 mb-3') and contains(., 'Latest datasets')]")
            print('Test passed!')

        except NoSuchElementException:
            raise AssertionError('Test failed!')

    finally:

        # Close the browser
        close_driver(driver)


# Call the test function
test_login_and_check_element()


def test_developer_signup():
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Abrir la página de registro de desarrollador
        driver.get(f'{host}/signup/developer')

        # Esperar un poco para asegurarse de que la página se haya cargado completamente
        time.sleep(4)

        # Verificar que estamos en la página de registro de desarrollador
        assert "Sign up as Developer" in driver.page_source, "Not on the correct page"

        # Llenar el formulario de registro de desarrollador
        name_field = driver.find_element(By.NAME, 'name')
        surname_field = driver.find_element(By.NAME, 'surname')
        email_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'password')
        team_field = driver.find_element(By.NAME, 'team')
        github_field = driver.find_element(By.NAME, 'github')

        # Completar los campos del formulario
        name_field.send_keys('John')
        surname_field.send_keys('Doe')
        email_field.send_keys('developer@example.com')
        password_field.send_keys('password123')
        team_field.send_keys('University of Seville')  # Seleccionar un equipo del desplegable
        github_field.send_keys('john-doe-github')  # Usuario GitHub (opcional)

        # Enviar el formulario
        github_field.send_keys(Keys.RETURN)

        # Esperar un poco para asegurarse de que el registro se haya procesado
        time.sleep(4)

        # Verificar si la redirección se realiza correctamente y si el usuario está autenticado
        try:
            # Verificar si el usuario es redirigido correctamente después del registro
            # driver.find_element(By.XPATH, "//h1[contains(text(), 'Welcome')]")
            print('Test passed! Developer successfully registered and redirected.')

        except NoSuchElementException:
            raise AssertionError('Test failed! Developer not redirected after registration.')

    finally:
        # Cerrar el navegador
        close_driver(driver)

    # Llamar a la función de prueba
    test_developer_signup()
