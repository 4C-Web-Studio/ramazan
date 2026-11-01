import os
import json
from pathlib import Path
from selenium import webdriver
ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'artifacts'
RESULTS.mkdir(exist_ok=True)
def chrome():
    # Keep the historical helper name used by the reports and callers.
    browser = os.environ.get('BROWSER', 'chrome' if os.environ.get('CI') else 'edge').lower()
    if browser not in ('edge', 'chrome'):
        raise ValueError('BROWSER must be edge or chrome')
    settings = webdriver.EdgeOptions() if browser == 'edge' else webdriver.ChromeOptions()
    if os.environ.get('HEADLESS') == '1':
        settings.add_argument('--headless=new')
    settings.add_argument('--window-size=1280,900')
    if browser == 'edge':
        from selenium.webdriver.edge.service import Service
        path = os.environ.get('EDGE_DRIVER')
        driver = webdriver.Edge(options=settings, service=Service(path) if path else Service())
    else:
        driver = webdriver.Chrome(options=settings)
    (RESULTS/'browser_capabilities.json').write_text(json.dumps(driver.capabilities,indent=2),encoding='utf-8')
    return driver
