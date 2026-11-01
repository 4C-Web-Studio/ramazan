import unittest
from contextlib import ExitStack
from selenium.webdriver.common.by import By
from support.browser import chrome, RESULTS
from support.hosting import serve
from web.portal import build_portal
from lab03.registration import RegistrationFlow
class MembershipTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        resources=ExitStack()
        cls.addClassCleanup(resources.close)
        cls.base=resources.enter_context(serve(build_portal()))
    def setUp(self):
        self.driver=chrome()
        self.addCleanup(self.driver.quit)
        self.addCleanup(lambda: self.driver.save_screenshot(str(RESULTS / (self.id() + '.png'))))
        self.form=RegistrationFlow(self.driver,self.base)
    def assert_rejected(self,name,email,password,message):
        self.assertFalse(self.form.execute(name,email,password))
        self.assertEqual(self.driver.find_element(By.ID,'form-message').text,message)
    def test_accept_member(self):
        self.assertTrue(self.form.execute('Club Captain','captain@example.com','ValidSecret2026'))
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR,'[data-testid="email"]').text,'captain@example.com')
    def test_email_format(self):
        self.assert_rejected('Club Player','invalid','ValidSecret2026','Неверный адрес почты')
    def test_nickname_size(self):
        self.assert_rejected('X','player@example.com','ValidSecret2026','Слишком короткое имя')
    def test_existing_member(self):
        self.assert_rejected('Club Player','demo@example.com','ValidSecret2026','Адрес уже используется')
if __name__=='__main__':unittest.main(verbosity=2)
