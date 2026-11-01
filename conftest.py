import pytest
@pytest.fixture
def browser(request):
    from support.browser import chrome, RESULTS
    driver = chrome()
    try:
        yield driver
    finally:
        filename=''.join(c if c.isalnum() else '_' for c in request.node.nodeid)
        try:
            driver.save_screenshot(str(RESULTS/(filename+'.png')))
        finally:
            driver.quit()
@pytest.fixture
def portal_url():
    from support.hosting import serve
    from web.portal import build_portal
    with serve(build_portal()) as url:
        yield url
