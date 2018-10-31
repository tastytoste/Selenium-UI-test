from selenium.webdriver.common.by import By

class ContactUsLocators(object):
    NAME_FIELD = (By.XPATH,"//*[@id='wpcf7-f173-p11-o1']/form/span[1]/input")
    EMAIL_FIELD = (By.XPATH,"//*[@id='wpcf7-f173-p11-o1']/form/span[2]/input")
    PREFIX_FIELD = (By.XPATH,"//*[@id='wpcf7-f173-p11-o1']/form/span[3]/input")
    PHONE_FIELD = (By.XPATH,"//*[@id='wpcf7-f173-p11-o1']/form/span[4]/input")
    COMPANY_FIELD = (By.XPATH,"//*[@id='wpcf7-f173-p11-o1']/form/span[5]/input")
    MESSAGE_FIELD = (By.XPATH,"//*[@id='wpcf7-f173-p11-o1']/form/span[6]/textarea")
    EMPTY_NAME_FIELD_ERROR = (By.XPATH,"//*[@id='wpcf7-f173-p11-o1']/form/span[1]/span")
    EMPTY_EMAIL_FIELD_ERROR = (By.XPATH,"//*[@id='wpcf7-f173-p11-o1']/form/span[2]/span")
    EMPTY_PREFIX_FIELD_ERROR = (By.XPATH, "//*[@id='wpcf7-f173-p11-o1']/form/span[3]/span")
    EMPTY_PREFIX_PHONE_FIELD_ERROR = (By.XPATH,"//*[@id='wpcf7-f173-p11-o1']/form/span[4]/span")
    CONTACT_US_BUTTON = (By.XPATH, "//*[@id='wpcf7-f173-p11-o1']/form/input[5]")
    ALERT_MESSAGE = (By.XPATH, "//*[@id='wpcf7-f173-p11-o1']/form/div[2]")
    REQUIRED_ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'The field is required.')]")
    THANKS_ALERT = (By.XPATH, "//*[contains(text(), 'Thank you for your message. It has been sent.')]")
    FIELDS_ERROR_ALERT = (By.XPATH, "//*[contains(text(), 'One or more fields have an error. Please check and try again.')]")
    
