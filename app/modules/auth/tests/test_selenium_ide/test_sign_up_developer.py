from selenium.webdriver.common.by import By
from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver


class TestSignupDeveloper:
    def setup_method(self, method):
        # Inicializa el controlador de Selenium (por ejemplo, ChromeDriver)
        self.driver = initialize_driver()
        self.vars = {}

    def teardown_method(self, method):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

    def test_signup_developer(self):
        # Accede a la página principal de sign up
        self.driver.get(get_host_for_selenium_testing() + "/signup")
        
        # Haz clic en el enlace "Click here" que te lleva a la página de registro como desarrollador
        self.driver.find_element(By.LINK_TEXT, "Click here").click()

        # Verifica que la URL sea la de /signup/developer
        assert "/signup/developer" in self.driver.current_url
        
        # Rellena los campos del formulario para registro de desarrollador
        self.driver.find_element(By.NAME, "name").send_keys("Juan")
        self.driver.find_element(By.NAME, "surname").send_keys("Perez")
        self.driver.find_element(By.NAME, "email").send_keys("juanperez@developer.com")
        self.driver.find_element(By.NAME, "github").send_keys("juanperezdev")
        self.driver.find_element(By.NAME, "team").send_keys("Development Team")
        self.driver.find_element(By.NAME, "password").send_keys("developerpassword123")
        
        # Envía el formulario
        self.driver.find_element(By.NAME, "submit").click()
