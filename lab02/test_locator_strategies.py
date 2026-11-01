import pytest
from selenium.webdriver.common.by import By
@pytest.mark.parametrize('strategy,expression',[
    (By.ID,'nickname'),
    (By.CSS_SELECTOR,'input[data-testid="person"]'),
    (By.XPATH,"//form/label/input[@name='nickname']")])
def test_same_field_with_different_locators(browser,portal_url,strategy,expression):
    browser.get(portal_url+'/join')
    node=browser.find_element(strategy,expression)
    node.send_keys('Board Game Tester')
    assert node.get_attribute('value')=='Board Game Tester'
    assert node==browser.find_element(By.ID,'nickname')
    print(strategy,expression,'-> один и тот же DOM элемент')
