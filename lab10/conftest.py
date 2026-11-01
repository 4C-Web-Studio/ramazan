import pytest
from support.hosting import serve
from lab10.api import create_api
@pytest.fixture
def api_url():
    app=create_api()
    with serve(app) as address:yield address+'/users'
    if 'db' in app.extensions:app.extensions['db'].close()
