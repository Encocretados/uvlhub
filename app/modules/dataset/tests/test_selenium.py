import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver

SAMPLE_DATASET_ROUTE = "/doi/10.1234/dataset1/"

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


def test_download_button():
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the dataset page
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(., 'Download All')]")))
        # Check presence of buttons
        assert driver.find_element(By.XPATH, "//a[contains(., 'Download All')]")

        print("The botton is present and correctly placed!")

    finally:
        close_driver(driver)


def test_table_UVLfiles():
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the dataset page
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        # Check the presence of file table and buttons
        rows = driver.find_elements(By.XPATH, "//div[@class='list-group-item']")
        assert len(rows) > 0, "No files are displayed in the table!"
        for row in rows:
            file_name = row.find_element(By.XPATH, ".//div[contains(@class, 'col-12')]")
            assert file_name.is_displayed(), "File name is not displayed!"
            view_button = row.find_element(By.XPATH, "//button[contains(., 'View')]")
            assert view_button.is_displayed(), "View button is not displayed!"

            # Verify "Check" button
            check_button = row.find_element(By.XPATH, "//button[contains(., 'Check')]")
            assert check_button.is_displayed(), "Check button is not displayed!"

            # Verify "Export" button
            export_button = row.find_element(By.XPATH, "//button[contains(., 'Export')]")
            assert export_button.is_displayed(), "Export button is not displayed!"

        print("File table and buttons are correctly displayed!")

    finally:
        close_driver(driver)

def test_inter_elements():
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the dataset page
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        # Test modal behavior
        view_button = driver.find_element(By.XPATH, "(//button[contains(., 'View')])[1]")
        view_button.click()
        time.sleep(1)  # Wait for modal to open
        modal = driver.find_element(By.ID, "fileViewerModal")
        assert modal.is_displayed(), "File viewer modal is not displayed!"
        close_button = driver.find_element(By.CLASS_NAME, "btn-close")
        close_button.click()
        time.sleep(1)  # Wait for modal to close
        assert not modal.is_displayed(), "File viewer modal did not close!"
        print("Interactive elements are working!")

    finally:
        close_driver(driver)


def test_button_explore_more_datasets():
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the dataset page
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        # Test the 'Explore more datasets' button
        explore_button = driver.find_element(By.XPATH, "//a[contains(., 'Explore more datasets')]")
        explore_button.click()
        wait_for_page_to_load(driver)

        # Verify the page navigated correctly
        expected_url = f"{host}/explore"
        current_url = driver.current_url
        assert driver.current_url == expected_url, f"Did not navigate to the explore page! Current URL: {current_url}"

        print("Explore more datasets button works!")

    finally:
        close_driver(driver)

# Call the test function
test_upload_dataset()
test_download_button()
test_table_UVLfiles()
test_inter_elements()
test_button_explore_more_datasets()
