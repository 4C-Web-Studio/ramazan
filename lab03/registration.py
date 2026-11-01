import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from web.settings import CONFIG as C
from support.browser import RESULTS
class RegistrationFlow:
    def __init__(self,driver,origin):
        self.driver,self.origin=driver,origin
        self.log=logging.getLogger('club.registration')
        self.log.setLevel(logging.INFO)
        if not self.log.handlers:
            handler=logging.FileHandler(RESULTS/'membership.log',encoding='utf-8')
            handler.setFormatter(logging.Formatter('%(asctime)s | %(message)s'))
            self.log.addHandler(handler)
    def execute(self,person,mailbox,passphrase):
        self.driver.get(self.origin+C['route'])
        values={C['name']:person,C['mail']:mailbox,C['secret']:passphrase}
        for name,value in values.items():
            self.driver.find_element(By.NAME,name).send_keys(value)
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        WebDriverWait(self.driver,5,ignored_exceptions=(StaleElementReferenceException,)).until(
            lambda d: (d.find_element(By.ID,C['ok']).is_displayed() if d.current_url.endswith(C['end'])
                       else bool(d.find_element(By.ID,C['error']).text)))
        accepted=self.driver.current_url.endswith(C['end'])
        self.log.info('Результат вступления: %s', 'принято' if accepted else self.driver.find_element(By.ID,C['error']).text)
        return accepted
def enroll(driver,base,name,mail,password):
    return RegistrationFlow(driver,base).execute(name,mail,password)
