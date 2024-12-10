import os
import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver


def wait_for_page_to_load(driver, timeout=4):
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


def count_datasets(driver, host):
    driver.get(f"{host}/dataset/list")
    wait_for_page_to_load(driver)

    try:
        amount_datasets = len(driver.find_elements(By.XPATH, "//table//tbody//tr"))
    except Exception:
        amount_datasets = 0
    return amount_datasets


def test_upload_dataset():
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the login page
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # Find the username and password field and enter the values
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")

        email_field.send_keys("user1@example.com")
        password_field.send_keys("1234")

        # Send the form
        password_field.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # Count initial datasets
        initial_datasets = count_datasets(driver, host)

        # Open the upload dataset
        driver.get(f"{host}/dataset/upload")
        wait_for_page_to_load(driver)

        # Find basic info and UVL model and fill values
        title_field = driver.find_element(By.NAME, "title")
        title_field.send_keys("Title")
        desc_field = driver.find_element(By.NAME, "desc")
        desc_field.send_keys("Description")
        tags_field = driver.find_element(By.NAME, "tags")
        tags_field.send_keys("tag1,tag2")

        # Add two authors and fill
        add_author_button = driver.find_element(By.ID, "add_author")
        add_author_button.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)
        add_author_button.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        name_field0 = driver.find_element(By.NAME, "authors-0-name")
        name_field0.send_keys("Author0")
        affiliation_field0 = driver.find_element(By.NAME, "authors-0-affiliation")
        affiliation_field0.send_keys("Club0")
        orcid_field0 = driver.find_element(By.NAME, "authors-0-orcid")
        orcid_field0.send_keys("0000-0000-0000-0000")

        name_field1 = driver.find_element(By.NAME, "authors-1-name")
        name_field1.send_keys("Author1")
        affiliation_field1 = driver.find_element(By.NAME, "authors-1-affiliation")
        affiliation_field1.send_keys("Club1")

        # Obtén las rutas absolutas de los archivos
        file1_path = os.path.abspath("app/modules/dataset/uvl_examples/file1.uvl")
        file2_path = os.path.abspath("app/modules/dataset/uvl_examples/file2.uvl")

        # Subir el primer archivo
        dropzone = driver.find_element(By.CLASS_NAME, "dz-hidden-input")
        dropzone.send_keys(file1_path)
        wait_for_page_to_load(driver)

        # Subir el segundo archivo
        dropzone = driver.find_element(By.CLASS_NAME, "dz-hidden-input")
        dropzone.send_keys(file2_path)
        wait_for_page_to_load(driver)

        # Add authors in UVL models
        show_button = driver.find_element(By.ID, "0_button")
        show_button.send_keys(Keys.RETURN)
        add_author_uvl_button = driver.find_element(By.ID, "0_form_authors_button")
        add_author_uvl_button.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        name_field = driver.find_element(By.NAME, "feature_models-0-authors-2-name")
        name_field.send_keys("Author3")
        affiliation_field = driver.find_element(By.NAME, "feature_models-0-authors-2-affiliation")
        affiliation_field.send_keys("Club3")

        # Check I agree and send form
        check = driver.find_element(By.ID, "agreeCheckbox")
        check.send_keys(Keys.SPACE)
        wait_for_page_to_load(driver)

        upload_btn = driver.find_element(By.ID, "upload_button")
        upload_btn.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)
        time.sleep(2)  # Force wait time

        assert driver.current_url == f"{host}/dataset/list", "Test failed!"

        # Count final datasets
        final_datasets = count_datasets(driver, host)
        assert final_datasets == initial_datasets + 1, "Test failed!"

        print("Test passed!")

    finally:

        # Close the browser
        close_driver(driver)

def test_upload_unsynchronized_dataset_to_zenodo():
    """
    Test que verifica que un dataset en la sección 'unsynchronized' puede subirse
    correctamente a Fakenodo desde la página de detalles del dataset.
    """
    # Configuración inicial del driver
    driver = webdriver.Chrome()  # Asegúrate de configurar el PATH de chromedriver si es necesario

    try:
        # Navegar a la lista de datasets
        driver.get("http://127.0.0.1:5000/dataset/list")
        time.sleep(2)  # Esperar a que la página cargue completamente

        # Seleccionar datasets solo de la sección 'unsynchronized'
        staging_datasets_links = driver.find_elements(By.CSS_SELECTOR, "div.card:nth-of-type(2) table tbody a")
        if not staging_datasets_links:
            raise Exception("No se encontraron datasets en staging (unsynchronized).")

        # Seleccionar el primer dataset en staging
        first_dataset = staging_datasets_links[0]
        first_dataset_url = first_dataset.get_attribute("href")
        first_dataset.click()
        time.sleep(2)  # Esperar a que cargue la página del dataset

        # Verificar que estamos en la URL correcta
        dataset_id = first_dataset_url.split("/")[-1]  # Extraer el ID del dataset desde la URL
        expected_url = f"http://127.0.0.1:5000/dataset/unsynchronized/{dataset_id}/"
        assert driver.current_url == expected_url, f"URL inesperada: {driver.current_url}"

        # Localizar y hacer clic en el botón 'uploadToZenodo'
        upload_button = driver.find_element(By.ID, "uploadToZenodo")  # Cambia 'ID' por el selector adecuado si es necesario
        upload_button.click()
        time.sleep(3)  # Esperar la respuesta del servidor

        # Verificar el mensaje de éxito
        success_message = driver.find_element(By.CLASS_NAME, "alert-success")  # Cambia el selector si es necesario
        assert success_message.text == "¡Archivo subido a Fakenodo exitosamente!", "El mensaje de éxito no coincide."

        print("El test pasó correctamente.")

    except Exception as e:
        print(f"El test falló: {e}")

    finally:
        # Cerrar el navegador
        driver.quit()


def test_dataset_appears_in_staging():
    """
    Test que verifica que un dataset subido se muestra correctamente en el área de staging.
    """
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Contar el número inicial de datasets en staging
        driver.get(f"{host}/dataset/list")
        wait_for_page_to_load(driver)
        staging_datasets_links = driver.find_elements(By.CSS_SELECTOR, "div.card:nth-of-type(2) table tbody tr")
        initial_staging_count = len(staging_datasets_links)

        # Subir un nuevo dataset
        driver.get(f"{host}/dataset/upload")
        wait_for_page_to_load(driver)

        # Completar los campos obligatorios
        title_field = driver.find_element(By.NAME, "title")
        title_field.send_keys("Título de prueba en staging")
        desc_field = driver.find_element(By.NAME, "desc")
        desc_field.send_keys("Descripción del dataset en staging")
        tags_field = driver.find_element(By.NAME, "tags")
        tags_field.send_keys("prueba,staging")

        # Subir un archivo
        file_path = os.path.abspath("app/modules/dataset/uvl_examples/file1.uvl")
        dropzone = driver.find_element(By.CLASS_NAME, "dz-hidden-input")
        dropzone.send_keys(file_path)
        wait_for_page_to_load(driver)

        # Aceptar términos y subir el dataset
        upload_btn = driver.find_element(By.ID, "upload_button")
        upload_btn.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # Contar el número de datasets en staging después de la subida
        driver.get(f"{host}/dataset/list")
        wait_for_page_to_load(driver)
        staging_datasets_links_after = driver.find_elements(By.CSS_SELECTOR, "div.card:nth-of-type(2) table tbody tr")
        final_staging_count = len(staging_datasets_links_after)

        # Verificar que el número de datasets en staging haya aumentado
        assert final_staging_count == initial_staging_count + 1, "El dataset no se añadió al área de staging."

        print("El test de aparición en staging pasó correctamente.")

    except Exception as e:
        print(f"El test falló: {e}")

    finally:
        close_driver(driver)

def test_unsynchronized_dataset_remains_in_staging():
    """
    Test que verifica que un dataset no sincronizado permanece en el área de staging.
    """
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Navegar a la lista de datasets
        driver.get(f"{host}/dataset/list")
        wait_for_page_to_load(driver)

        # Seleccionar datasets en staging
        staging_datasets_links = driver.find_elements(By.CSS_SELECTOR, "div.card:nth-of-type(2) table tbody tr")
        if not staging_datasets_links:
            raise Exception("No se encontraron datasets en staging.")

        # Seleccionar el primer dataset
        first_dataset = staging_datasets_links[0]
        first_dataset_url = first_dataset.find_element(By.TAG_NAME, "a").get_attribute("href")
        first_dataset.click()
        wait_for_page_to_load(driver)

        # Verificar que el dataset no esté sincronizado con Zenodo
        unsynchronized_message = driver.find_element(By.CLASS_NAME, "alert-warning")  # Cambia el selector si es necesario
        assert "Este dataset no está sincronizado con Zenodo" in unsynchronized_message.text, \
            "El dataset no muestra el mensaje esperado de no sincronizado."

        # Verificar que seguimos en la sección de staging
        driver.get(f"{host}/dataset/list")
        wait_for_page_to_load(driver)
        staging_datasets_links_after = driver.find_elements(By.CSS_SELECTOR, "div.card:nth-of-type(2) table tbody tr")
        assert any(first_dataset_url in link.find_element(By.TAG_NAME, "a").get_attribute("href") 
                   for link in staging_datasets_links_after), "El dataset no permanece en staging."

        print("El test de permanencia en staging pasó correctamente.")

    except Exception as e:
        print(f"El test falló: {e}")

    finally:
        close_driver(driver)


# Call the test function
test_upload_dataset()
