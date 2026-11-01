from lab05.pages import SignInPage
def test_member_access(browser,portal_url):
    member=SignInPage(browser,portal_url).open().login('demo@example.com','ValidSecret2026')
    assert member.email()=='demo@example.com'
def test_denied_password(browser,portal_url):
    page=SignInPage(browser,portal_url).open();page.form.enter('demo@example.com','incorrect')
    assert page.message()=='Доступ отклонен'
def test_session_end(browser,portal_url):
    member=SignInPage(browser,portal_url).open().login('demo@example.com','ValidSecret2026');member.leave()
    browser.get(portal_url+'/member')
    assert browser.current_url.endswith('/signin')
