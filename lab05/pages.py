from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CredentialForm:
    def __init__(self,driver):self.driver=driver
    def enter(self,email,password):
        form=self.driver.find_element(By.TAG_NAME,'form')
        for name,value in [('mailbox',email),('passphrase',password)]:
            item=self.driver.find_element(By.NAME,name);item.clear();item.send_keys(value)
        self.driver.find_element(By.CSS_SELECTOR,'[data-action="send"]').click()
        WebDriverWait(self.driver,5).until(EC.staleness_of(form))
class MemberPage:
    def __init__(self,driver):self.driver=driver
    def email(self):return self.driver.find_element(By.CSS_SELECTOR,'[data-testid="email"]').text
    def leave(self):self.driver.find_element(By.CSS_SELECTOR,'[data-action="exit"]').click()
class SignInPage:
    def __init__(self,driver,base):self.driver,self.base=driver,base;self.form=CredentialForm(driver)
    def open(self):self.driver.get(self.base+'/signin');return self
    def login(self,email,password):
        self.form.enter(email,password)
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,'member-title')))
        return MemberPage(self.driver)
    def message(self):return self.driver.find_element(By.ID,'form-message').text
