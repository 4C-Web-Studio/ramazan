from selenium.webdriver.common.by import By
from support.browser import ROOT
def prepare(browser):browser.get((ROOT/'lab07/index.html').as_uri())
def add(browser,name):browser.find_element(By.ID,'habit').send_keys(name);browser.find_element(By.ID,'create').click()
def test_completion(browser):
    prepare(browser);add(browser,'Прочитать главу');browser.find_element(By.CSS_SELECTOR,'#habits input').click()
    assert browser.find_element(By.ID,'completed').text=='1'
def test_reset(browser):
    prepare(browser);add(browser,'Прогулка');browser.find_element(By.CSS_SELECTOR,'#habits input').click();browser.find_element(By.ID,'reset').click()
    assert not browser.find_element(By.CSS_SELECTOR,'#habits input').is_selected()
    assert browser.find_element(By.ID,'completed').text=='0'
def test_remove_completed(browser):
    prepare(browser);add(browser,'Зарядка');browser.find_element(By.CSS_SELECTOR,'#habits input').click();browser.find_element(By.CSS_SELECTOR,'#habits button').click()
    assert browser.find_element(By.ID,'completed').text=='0'
    assert not browser.find_elements(By.CSS_SELECTOR,'#habits li')
