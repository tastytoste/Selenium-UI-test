from selenium.common.exceptions import NoSuchElementException
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.exeption = NoSuchElementException

class ContactUsPage(BasePage):

    def enter_name(self, name):
        name_field = self.driver.find_element(*ContactUsLocators.NAME_FIELD)
        name_field.send_keys(name)

    def enter_email(self, email):
        email_field = self.driver.find_element(*ContactUsLocators.EMAIL_FIELD)
        email_field.send_keys(email)

    def enter_prefix(self, prefix):
        prefix_field = self.driver.find_element(*ContactUsLocators.PREFIX_FIELD)
        prefix_field.send_keys(prefix)

    def enter_phone(self, phone):
        phone_field = self.driver.find_element(*ContactUsLocators.PHONE_FIELD)
        phone_field.send_keys(phone)

    def enter_company(self, company):
        company_field = self.driver.find_element(*ContactUsLocators.COMPANY_FIELD)
        company_field.send_keys(company)

    def enter_message(self, message):
        message_field = self.driver.find_element(*ContactUsLocators.MESSAGE_FIELD)
        message_field.send_keys(message)

    def click_contact_us(self):
        contact_us_button = self.driver.find_element(*ContactUsLocators.CONTACT_US_BUTTON)
        contact_us_button.click()

    def wait_until_error_is_present(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((ContactUsLocators.REQUIRED_ERROR_MESSAGE))
            )
        finally:
            pass

    def get_all_required_fields(self):
        name_field = self.driver.find_element(*ContactUsLocators.EMPTY_NAME_FIELD_ERROR).text
        email_field = self.driver.find_element(*ContactUsLocators.EMPTY_EMAIL_FIELD_ERROR).text
        prefix_field = self.driver.find_element(*ContactUsLocators.EMPTY_PREFIX_PHONE_FIELD_ERROR).text
        phone_field = self.driver.find_element(*ContactUsLocators.EMPTY_PREFIX_PHONE_FIELD_ERROR).text
        return name_field, email_field, prefix_field, phone_field

    def contact_us(self, name, email, prefix, phone, company, message):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_prefix(prefix)
        self.enter_phone(phone)
        self.enter_company(company)
        self.enter_message(message)
        self.click_contact_us()

    def empty_email_error_displayed(self):
        emailErrorMessage = self.driver.find_element(*ContactUsLocators.EMPTY_EMAIL_FIELD_ERROR)
        return emailErrorMessage.text

    def empty_name_error_displayed(self):
        emptyNameError = self.driver.find_element(*ContactUsLocators.EMPTY_NAME_FIELD_ERROR)
        return emptyNameError.text

    def invalid_email_error_displayed(self):
        invalidEmailError = self.driver.find_element(*ContactUsLocators.EMPTY_EMAIL_FIELD_ERROR)
        return invalidEmailError.text

    def invalid_prefix_error_displayed(self):
        invalidPrefixError = self.driver.find_element(*ContactUsLocators.EMPTY_PREFIX_FIELD_ERROR)
        return invalidPrefixError.text

    def empty_prefix_error_displayed(self):
        emptyPrefixError = self.driver.find_element(*ContactUsLocators.EMPTY_PREFIX_FIELD_ERROR)
        return emptyPrefixError.text

    def invalid_phone_error_displayed(self):
        invalidPrefixError = self.driver.find_element(*ContactUsLocators.EMPTY_PREFIX_PHONE_FIELD_ERROR)
        return invalidPrefixError.text

    def empty_phone_error_displayed(self):
        emptyPrefixError = self.driver.find_element(*ContactUsLocators.EMPTY_PREFIX_PHONE_FIELD_ERROR)
        return emptyPrefixError.text

    def message_sent_displayed(self):
        try:
            messageSentAlert = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((ContactUsLocators.THANKS_ALERT))
            )
            return messageSentAlert.text
        finally:
            pass

    def fields_error_message_displayed(self):
        try:
            fieldsErrorMessageAlert = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((ContactUsLocators.FIELDS_ERROR_ALERT))
            )
            return fieldsErrorMessageAlert.text
        finally:
            pass
