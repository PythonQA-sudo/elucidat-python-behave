from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from pages.base_page import DriverManager

class HomePage(DriverManager):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.driver.title

    def get_heading_text(self):
        try:
            heading = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1'))
            ).text
            return heading
        except TimeoutException:
            print("Timed out waiting for the heading to be visible.")
            return None
        except NoSuchElementException:
            print("Heading element not found.")
            return None

    def click_start_button(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='START']"))
            )
            button.click()
            return True
        except TimeoutException:
            print("Timed out waiting for START button to be clickable.")
            return False
        except NoSuchElementException:
            print("START button not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the START button and intercepting the click.")
            return False

    def click_on_case_against_kavin_button(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "pa_5c9126fe3f4fb_p179d7b273e1-card__image-1"))
            )
            button.click()
            return True
        except TimeoutException:
            print("Timed out waiting for case against Kavin button to be clickable.")
            return False
        except NoSuchElementException:
            print("Case against Kavin button not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the case against Kavin button and intercepting the click.")
            return False

    def click_judge_this(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@id="pa_5c9126fe434ba_p15564daa856-textButton"]')))
            button.click()
            return True
        except TimeoutException:
            print("Timed out waiting for JUDGE THIS button to be clickable.")
            return False
        except NoSuchElementException:
            print("JUDGE THIS button not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the JUDGE THIS button and intercepting the click.")
            return False

    def click_guilty_radio(self):
        try:
            radio = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//span[@id="pa_5c9126fe47260_p15515116385-itemInner-1"]'))
            )
            radio.click()
            return True
        except TimeoutException:
            print("Timed out waiting for GUILTY radio button to be clickable.")
            return False
        except NoSuchElementException:
            print("GUILTY radio button not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the GUILTY radio button and intercepting the click.")
            return False

    def click_vote_button(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//span[text()="VOTE"]'))
            )
            button.click()
            return True
        except TimeoutException:
            print("Timed out waiting for VOTE button to be clickable.")
            return False
        except NoSuchElementException:
            print("VOTE button not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the VOTE button and intercepting the click.")
            return False

    def verify_not_guilty(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//h2[@id="pa_5c9126fe47260_p1554e607e3b-modalTitle"]'))
            )
            return element.is_displayed()
        except TimeoutException:
            print("Timed out waiting for NOT GUILTY element to be visible.")
            return False
        except NoSuchElementException:
            print("NOT GUILTY element not found.")
            return False

    def click_continue_button_1(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@id="pa_5c9126fe47260_p15583b88249-dismiss_button"]'))
            )
            button.click()
            return True
        except TimeoutException:
            print("Timed out waiting for CONTINUE button 1 to be clickable.")
            return False
        except NoSuchElementException:
            print("CONTINUE button 1 not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the CONTINUE button 1 and intercepting the click.")
            return False


    def click_continue_button_on_our_expert_agree(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@id="pa_5c9126fe5331b_p155cc4e96eb-dismiss_button"]'))
            )
            button.click()
            return True
        except TimeoutException:
            print("Timed out waiting for CONTINUE button 1 to be clickable.")
            return False
        except NoSuchElementException:
            print("CONTINUE button 1 not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the CONTINUE button 1 and intercepting the click.")
            return False



    def click_continue_button_2(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@id="pa_5c9126fe4b742_p15550a254a1-textButton"]')))
            button.click()
            return True
        except TimeoutException:
            print("Timed out waiting for CONTINUE button 1 to be clickable.")
            return False
        except NoSuchElementException:
            print("CONTINUE button 1 not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the CONTINUE button 1 and intercepting the click.")
            return False



    def click_continue_button_2(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//span[text()="CONTINUE"]'))
            )
            button.click()
            return True
        except TimeoutException:
            print("Timed out waiting for CONTINUE button 2 to be clickable.")
            return False
        except NoSuchElementException:
            print("CONTINUE button 2 not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the CONTINUE button 2 and intercepting the click.")
            return False

    def verify_you_decide(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//h2[text()="YOU DECIDE"]'))
            )
            return element.is_displayed()
        except TimeoutException:
            print("Timed out waiting for YOU DECIDE element to be visible.")
            return False
        except NoSuchElementException:
            print("YOU DECIDE element not found.")
            return False

    def click_flip_button(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@id="pa_5c9126fe5331b_p15578a164ba-flip_button-front"]'))
            )
            button.click()
            return True
        except TimeoutException:
            print("Timed out waiting for FLIP button to be clickable.")
            return False
        except NoSuchElementException:
            print("FLIP button not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the FLIP button and intercepting the click.")
            return False

    def click_can_be_reliable_radio(self):
        try:
            radio = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@id="pa_5c9126fe5331b_p155cc4e94a5-caption__inner-3"]'))
            )
            radio.click()
            return True
        except TimeoutException:
            print("Timed out waiting for CAN BE RELIABLE radio button to be clickable.")
            return False
        except NoSuchElementException:
            print("CAN BE RELIABLE radio button not found.")
            return False
        except ElementClickInterceptedException:
            print("Another element is covering the CAN BE RELIABLE radio button and intercepting the click.")
            return False

    def verify_our_expert_agrees(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//h2[text()="Our expert agrees..."]'))
            )
            return element.is_displayed()
        except TimeoutException:
            print("Timed out waiting for OUR EXPERT AGREES element to be visible.")
            return False
        except NoSuchElementException:
            print("OUR EXPERT AGREES element not found.")
            return False

    def is_element_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except TimeoutException:
            print(f"Timed out waiting for element {locator} to be visible.")
            return False
        except NoSuchElementException:
            print(f"Element {locator} not found.")
            return False
