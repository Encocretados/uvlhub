import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from app.modules.auth.services import AuthenticationService
from app.modules.community.models import Community
from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import close_driver, initialize_driver

authentication_service = AuthenticationService()


def test_create_community():

    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # 1. Abrir la página de login
        driver.get(f"{host}/login")

        # Espera para asegurarse de que la página cargue completamente
        time.sleep(2)

        # 2. Rellenar el formulario de login
        email_field = driver.find_element(
            By.ID, "email"
        )  # Suponiendo que el campo es 'email'
        password_field = driver.find_element(
            By.ID, "password"
        )  # Suponiendo que el campo es 'password'

        # Ingresar las credenciales
        email_field.send_keys("uvlhub.reply@gmail.com")
        password_field.send_keys("uvl12hub34")

        # 3. Enviar el formulario de login
        password_field.send_keys(Keys.RETURN)  # Enviar el formulario con "Enter"

        # Esperar un poco para asegurarse de que el login sea exitoso y redirija a la página de creación de comunidad
        time.sleep(4)

        # Insert the email key
        clave = authentication_service.get_validation_email_key()
        print(clave)
        key_field = driver.find_element(By.NAME, "key")
        key_field.send_keys(clave)
        key_field.send_keys(Keys.RETURN)

        time.sleep(4)

        # 1. Abrir la página de creación de la comunidad
        driver.get(f"{host}/community/create")

        # Espera para asegurarse de que la página cargue completamente
        time.sleep(2)

        # 2. Rellenar el formulario de creación de la comunidad
        name_field = driver.find_element(By.ID, "name")
        description_field = driver.find_element(By.ID, "description")

        # Ingresar los datos para la nueva comunidad
        name_field.send_keys("Test Community")
        description_field.send_keys("This is a test community for Selenium testing.")

        # 3. Enviar el formulario (haciendo submit en el campo de descripción o haciendo click en el botón)
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()  # Simula presionar "Enter" para enviar el formulario

        # 4. Esperar un poco para que se procese la creación
        time.sleep(4)

        try:
            # 5. Verificar que la comunidad aparece en la lista
            # Aquí buscamos el nombre de la comunidad dentro del enlace
            community_name = "Test Community"
            driver.find_element(By.XPATH, f"//a[contains(text(), '{community_name}')]")
            print("Test passed! Community created successfully.")

        except NoSuchElementException:
            raise AssertionError("Test failed! Community not found after creation.")

    finally:
        # Cerrar el navegador después de la prueba
        close_driver(driver)


def test_edit_community():

    from app import app

    with app.app_context():
        community = Community.query.filter_by(name="Test Community").first()
        if not community:
            raise AssertionError("Test failed! Community not found.")

    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        driver.get(f"{host}/login")

        # Espera para asegurarse de que la página cargue completamente
        time.sleep(2)

        # 2. Rellenar el formulario de login
        email_field = driver.find_element(
            By.ID, "email"
        )  # Suponiendo que el campo es 'email'
        password_field = driver.find_element(
            By.ID, "password"
        )  # Suponiendo que el campo es 'password'

        # Ingresar las credenciales
        email_field.send_keys("uvlhub.reply@gmail.com")
        password_field.send_keys("uvl12hub34")

        # 3. Enviar el formulario de login
        password_field.send_keys(Keys.RETURN)  # Enviar el formulario con "Enter"

        # Esperar un poco para asegurarse de que el login sea exitoso y redirija a la página de creación de comunidad
        time.sleep(4)

        # Insert the email key
        clave = authentication_service.get_validation_email_key()
        print(clave)
        key_field = driver.find_element(By.NAME, "key")
        key_field.send_keys(clave)
        key_field.send_keys(Keys.RETURN)

        time.sleep(4)

        # 1. Abrir la página de edición de la comunidad
        driver.get(
            f"{host}/community/{community.id}/edit"
        )  # Suponiendo que la comunidad con ID=1 existe

        # Espera para asegurarse de que la página cargue completamente
        time.sleep(2)

        # 2. Rellenar el formulario de edición de la comunidad
        name_field = driver.find_element(By.ID, "name")
        description_field = driver.find_element(By.ID, "description")

        # Modificar los datos para la comunidad
        name_field.clear()
        name_field.send_keys("Updated Test Community")
        description_field.clear()
        description_field.send_keys("Updated description for the community.")

        # 3. Enviar el formulario de edición
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Esperar a que los cambios se reflejen
        time.sleep(4)

        try:
            # Verificar que los campos del formulario se hayan actualizado
            updated_name_value = driver.find_element(By.ID, "name").get_attribute(
                "value"
            )
            updated_description_value = driver.find_element(
                By.ID, "description"
            ).get_attribute("value")

            assert (
                updated_name_value == "Updated Test Community"
            ), "Test failed! Name not updated."
            assert (
                updated_description_value == "Updated description for the community."
            ), "Test failed! Description not updated."

        except NoSuchElementException:
            raise AssertionError("Test failed! Community not found after update.")

    finally:
        close_driver(driver)


def test_delete_community():

    from app import app

    with app.app_context():
        community = Community.query.filter_by(name="Updated Test Community").first()
        if not community:
            raise AssertionError("Test failed! Community not found.")

    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        driver.get(f"{host}/login")

        # Espera para asegurarse de que la página cargue completamente
        time.sleep(2)

        # 2. Rellenar el formulario de login
        email_field = driver.find_element(
            By.ID, "email"
        )  # Suponiendo que el campo es 'email'
        password_field = driver.find_element(
            By.ID, "password"
        )  # Suponiendo que el campo es 'password'

        # Ingresar las credenciales
        email_field.send_keys("uvlhub.reply@gmail.com")
        password_field.send_keys("uvl12hub34")

        # 3. Enviar el formulario de login
        password_field.send_keys(Keys.RETURN)  # Enviar el formulario con "Enter"

        # Esperar un poco para asegurarse de que el login sea exitoso y redirija a la página de creación de comunidad
        time.sleep(4)

        # Insert the email key
        clave = authentication_service.get_validation_email_key()
        print(clave)
        key_field = driver.find_element(By.NAME, "key")
        key_field.send_keys(clave)
        key_field.send_keys(Keys.RETURN)

        time.sleep(4)

        # 1. Abrir la página de edición de la comunidad
        driver.get(
            f"{host}/community/{community.id}/edit"
        )  # Suponiendo que la comunidad con ID=1 existe

        # Espera para asegurarse de que la página cargue completamente
        time.sleep(2)

        # 3. Enviar el formulario de edición
        submit_button = driver.find_element(By.ID, "delete-button")
        submit_button.click()

        alert = Alert(driver)
        alert.accept()

        # 4. Esperar a que los cambios se reflejen
        time.sleep(4)

        try:
            # Verificar que la comunidad ya no existe
            driver.find_element(
                By.XPATH, "//a[contains(text(), 'Updated Test Community')]"
            )
            raise AssertionError("Test failed! Community still exists after deletion.")

        except NoSuchElementException:
            print("Test passed! Community deleted successfully.")

    finally:
        close_driver(driver)
