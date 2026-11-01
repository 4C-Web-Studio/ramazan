import pytest
from lab03.registration import enroll
@pytest.mark.parametrize('name,mail,password,expected',[('Dice Master', 'dice@example.com', 'ValidSecret2026', True), ('X', 'x@example.com', 'ValidSecret2026', False), ('Player Two', 'short@example.com', '123', False), ('Player Three', 'demo@example.com', 'ValidSecret2026', False)])
def test_registration_cases(browser,portal_url,name,mail,password,expected):
    assert enroll(browser,portal_url,name,mail,password) is expected
