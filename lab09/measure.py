import csv
from time import perf_counter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support.browser import chrome,ROOT,RESULTS
CASES={'enabled': ('submit', 'enabled'), 'gone': ('progress', 'gone')}
def condition(locator,kind):
    return {'present':lambda:EC.presence_of_element_located(locator),
             'text':lambda:EC.text_to_be_present_in_element(locator,'Готово'),
             'enabled':lambda:EC.element_to_be_clickable(locator),
             'gone':lambda:EC.invisibility_of_element_located(locator)}[kind]()
def sample(mode,case):
    driver=chrome()
    try:
        driver.implicitly_wait(4 if mode=='implicit' else 0)
        driver.get((ROOT/'lab09/dynamic.html').as_uri())
        driver.find_element(By.ID,'begin').click()
        identifier,kind=CASES[case];locator=(By.ID,identifier);start=perf_counter()
        if mode=='explicit':
            WebDriverWait(driver,4).until(condition(locator,kind));ok=True
        elif kind=='present':ok=driver.find_element(*locator).is_displayed()
        elif kind=='text':ok=driver.find_element(*locator).text=='Готово'
        elif kind=='enabled':ok=driver.find_element(*locator).is_enabled()
        else:ok=not driver.find_element(*locator).is_displayed()
        return bool(ok),round(perf_counter()-start,4)
    finally:driver.quit()
if __name__=='__main__':
    with (RESULTS/'wait_comparison.csv').open('w',newline='',encoding='utf-8') as stream:
        writer=csv.writer(stream);writer.writerow(['repeat','mode','case','ok','seconds'])
        for repeat in range(1,4):
            for mode in ['implicit','explicit']:
                for case in CASES:
                    passed,seconds=sample(mode,case);writer.writerow([repeat,mode,case,passed,seconds]);print(repeat,mode,case,passed,seconds)
