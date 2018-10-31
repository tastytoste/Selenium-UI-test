import time
import unittest
from selenium import webdriver
import contactUsPage

class ContacUs(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'https://ipninja.io/#contact'
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)

    def tearDown(self):
        self.driver.close()

    def test_contact_us_opened(self):
        contact_us_page = contactUsPage.ContactUsPage(self.driver)
        assert "Contact us" in self.driver.page_source

    def test_required_fields(self):
        contact_us_page = contactUsPage.ContactUsPage(self.driver)
        contact_us_page.click_contact_us()
        assert "One or more fields have an error. Please check and try again." in contact_us_page.fields_error_message_displayed()
        assert "The field is required." in contact_us_page.get_all_required_fields()

    def test_valid_data(self):
        contact_us_page = contactUsPage.ContactUsPage(self.driver)
        contact_us_page.contact_us("test", "test@test.com", "+38", "0933332211", "test", "test_message")

    def test_empty_name(self):
        contact_us_page = contactUsPage.ContactUsPage(self.driver)
        contact_us_page.contact_us(" ", "test@email.com", "+38", "0933332211", "test", "test_message")
        assert "One or more fields have an error. Please check and try again." in contact_us_page.fields_error_message_displayed()
        assert "The field is required." in contact_us_page.empty_name_error_displayed()

    def test_invalid_email(self):
        contact_us_page = contactUsPage.ContactUsPage(self.driver)
        contact_us_page.contact_us("test", "test@", "+38", "0933332211", "test", "test_message")
        assert "One or more fields have an error. Please check and try again." in contact_us_page.fields_error_message_displayed()
        assert "The e-mail address entered is invalid." in contact_us_page.invalid_email_error_displayed()

    def test_empty_email(self):
        contact_us_page = contactUsPage.ContactUsPage(self.driver)
        contact_us_page.contact_us("test", " ", "+38", "0933332211", "test", "test_message")
        assert "One or more fields have an error. Please check and try again." in contact_us_page.fields_error_message_displayed()
        assert "The field is required." in contact_us_page.empty_email_error_displayed()

    def test_invalid_prefix(self):
        contact_us_page = contactUsPage.ContactUsPage(self.driver)
        contact_us_page.contact_us("test", "test@email.com", "abc", "0933332211", "test", "test_message")
        assert "One or more fields have an error. Please check and try again." in contact_us_page.fields_error_message_displayed()
        assert "The telephone number is invalid." in contact_us_page.invalid_prefix_error_displayed()

    def test_empty_prefix(self):
        contact_us_page = contactUsPage.ContactUsPage(self.driver)
        contact_us_page.contact_us("test", "test@email.com", " ", "0933332211", "test", "test_message")
        assert "One or more fields have an error. Please check and try again." in contact_us_page.fields_error_message_displayed()
        assert "The field is required." in contact_us_page.empty_prefix_error_displayed()

    def test_invalid_phone(self):
        contact_us_page = contactUsPage.ContactUsPage(self.driver)
        contact_us_page.contact_us("test", "test@email.com", "+38", "abc", "test", "test_message")
        assert "One or more fields have an error. Please check and try again." in contact_us_page.fields_error_message_displayed()
        assert "The telephone number is invalid." in contact_us_page.invalid_phone_error_displayed()

    def test_empty_phone(self):
        contact_us_page = contactUsPage.ContactUsPage(self.driver)
        contact_us_page.contact_us("test", "test@email.com", "+38", " ", "test", "test_message")
        assert "One or more fields have an error. Please check and try again." in contact_us_page.fields_error_message_displayed()
        assert "The field is required." in contact_us_page.empty_phone_error_displayed()


    def test_blank_company_and_message(self):
        contact_us_page = contactUsPage.ContactUsPage(self.driver)
        contact_us_page.contact_us("test", "test@email.com", "+38", "0933332211", " ", " ")
        assert "Thank you for your message. It has been sent." in contact_us_page.message_sent_displayed()

    def test_blank_company(self):
        contact_us_page = contactUsPage.ContactUsPage(self.driver)
        contact_us_page.contact_us("test", "test@email.com", "+38", "0933332211", " ", "test_message")
        assert "Thank you for your message. It has been sent." in contact_us_page.message_sent_displayed()

    def test_blank_message(self):
        contact_us_page = contactUsPage.ContactUsPage(self.driver)
        contact_us_page.contact_us("test", "test@email.com", "+38", "0933332211", "test", " ")
        assert "Thank you for your message. It has been sent." in contact_us_page.message_sent_displayed()

if __name__ == '__main__':
    unittest.main()



