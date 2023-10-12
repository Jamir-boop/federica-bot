from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from utils import take_screenshot


class FedericaBot:
    def __init__(self, email, password, dashboard_url):
        """
        Initializes the FedericaBot with user credentials and dashboard URL.

        :param email: User's email address
        :param password: User's password
        :param dashboard_url: URL of the dashboard to navigate to
        """
        options = Options()
        # Uncomment the below line if you want to run Chrome headlessly
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.email = email
        self.password = password
        self.dashboard_url = dashboard_url
        self.wait = WebDriverWait(self.driver, 15)

    def login(self):
        """
        Logs in to the dashboard using the provided credentials.
        """
        self.driver.get(self.dashboard_url)

        # Entering email
        self.wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        ).send_keys(self.email)

        # Entering password
        self.wait.until(
            EC.presence_of_element_located((By.NAME, "password")),
        ).send_keys(self.password)

        # Clicking login button
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/section/div/form/button")),
        ).send_keys(Keys.ENTER)

        # Validating successful login
        try:
            self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".ui.error.message.error-message .content")))
            print('Error login')
            # TODO: Send error message for failed login
        except:
            print('Login exitoso')

        # Checking if navigated to dashboard
        current_url = self.driver.current_url
        if "dashboard" in current_url:
            print(current_url)
        else:
            print('Error login')
            # TODO: Send error message for failed login

    def record(self):
        # click new record
        self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "button.ui.blue.mini.circular.compact.button")),
        ).send_keys(Keys.ENTER)

        # insert amount
        self.wait.until(
            EC.presence_of_element_located((By.NAME, "amount"))
        ).send_keys("69.69")

        # select account
        self.wait.until(
            EC.element_to_be_clickable((By.NAME, "accountId"))
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='label' and text()='BCP PEN']"))
        ).click()

        # select category
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='default text' and text()='Choose']"))
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='label' and text()='Food & Drinks']"))
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='label' and text()='Food & Drinks']"))
        ).click()

        # select label
        self.wait.until(
            EC.element_to_be_clickable((By.NAME, "labels"))
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='federica-bot']"))
        ).click()

        # insert note
        self.wait.until(
            EC.element_to_be_clickable((By.NAME, "note"))
        ).send_keys("notas del correo si que si")

        # forma de pago
        self.wait.until(
            EC.element_to_be_clickable((By.NAME, "paymentType"))
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@role='option' and text()='Credit card']"))
        ).click()

        self.driver.implicitly_wait(2)
        take_screenshot(self.driver)

        # agregar record
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "ui.circular.fluid.primary.button"))
        ).click()

    def close(self):
        self.driver.quit()
