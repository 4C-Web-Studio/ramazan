import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support.browser import chrome, RESULTS
def encyclopedia_lookup(query):
    driver=chrome()
    try:
        driver.set_window_size(1280,900)
        driver.get('https://en.wikipedia.org/w/index.php?title=Special:Search')
        wait=WebDriverWait(driver,20)
        field=wait.until(lambda d:next((node for node in d.find_elements(By.CSS_SELECTOR,'input[name="search"]')
                                      if node.is_displayed() and node.is_enabled()),False))
        field.clear();field.send_keys(query,Keys.ENTER)
        wait.until(lambda d:'search=' in d.current_url or '/wiki/' in d.current_url)
        content=wait.until(EC.visibility_of_element_located((By.ID,'mw-content-text')))
        assert query.casefold() in content.text.casefold() or driver.find_elements(By.CSS_SELECTOR,'.mw-search-result')
        driver.save_screenshot(str(RESULTS/'encyclopedia.png'))
        print('Открыта статья или поисковая выдача:',driver.title)
    except Exception:
        driver.save_screenshot(str(RESULTS/'encyclopedia_error.png'))
        (RESULTS/'encyclopedia_error.html').write_text(driver.page_source,encoding='utf-8')
        print('Search failed. Actual URL:',driver.current_url,'Title:',driver.title)
        raise
    finally:driver.quit()
if __name__=='__main__':encyclopedia_lookup(sys.argv[1] if len(sys.argv)>1 else 'Software testing')
