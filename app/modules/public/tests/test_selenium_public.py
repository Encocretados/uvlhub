import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import close_driver, initialize_driver


def test_check_motivational_phrase_exists():
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # 1. Abrir la página de login
        driver.get(f"{host}/")

        # Espera para asegurarse de que la página cargue completamente
        time.sleep(2)

        # 2. Verificar que la frase motivacional exista
        motivational_phrase = driver.find_element(By.ID, "motivational-phrase")

        assert motivational_phrase is not None

    finally:
        close_driver(driver)
