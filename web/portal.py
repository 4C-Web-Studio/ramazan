import re
import secrets
from flask import Flask, session, request, render_template_string, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from web.settings import CONFIG as C
from web.accounts import Accounts
FORM = """<!doctype html><html lang="ru"><meta charset="utf-8"><title>{{c.title}}</title>
<h1>{{c.title}}</h1><p id="{{c.error}}" role="alert">{{message}}</p>
<form method="post" novalidate>
{% if signup %}<label>Имя <input data-testid="person" id="{{c.name}}" name="{{c.name}}"></label>{% endif %}
<label>Email <input id="{{c.mail}}" name="{{c.mail}}" type="email"></label>
<label>Пароль <input id="{{c.secret}}" name="{{c.secret}}" type="password"></label>
<button data-action="send" type="submit">Продолжить</button></form></html>"""
def build_portal():
    app = Flask(__name__)
    app.secret_key = secrets.token_hex(24)
    accounts = Accounts()
    accounts.insert('Demo Member', 'demo@example.com', generate_password_hash('ValidSecret2026'))
    @app.route(C['route'], methods=['GET','POST'])
    def signup():
        message = ''
        if request.method == 'POST':
            name = request.form.get(C['name'], '').strip()
            mail = request.form.get(C['mail'], '').strip().casefold()
            password = request.form.get(C['secret'], '')
            if len(name) < C['name_min']:
                message = 'Слишком короткое имя'
            elif not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',mail):
                message = 'Неверный адрес почты'
            elif len(password) < C['password_min']:
                message = 'Слишком короткий пароль'
            elif accounts.exists(mail):
                message = 'Адрес уже используется'
            else:
                accounts.insert(name,mail,generate_password_hash(password))
                session['account'] = mail
                return redirect(C['end'])
        return render_template_string(FORM,c=C,signup=True,message=message)
    @app.route('/signin',methods=['GET','POST'])
    def signin():
        message=''
        if request.method=='POST':
            mail=request.form.get(C['mail'],'').strip().casefold()
            account=accounts.find(mail)
            if account and check_password_hash(account['hash'],request.form.get(C['secret'],'')):
                session['account']=mail
                return redirect(C['end'])
            message='Доступ отклонен'
        return render_template_string(FORM,c=C,signup=False,message=message)
    @app.get(C['end'])
    def profile():
        mail=session.get('account','')
        account=accounts.find(mail)
        if not account:return redirect('/signin')
        return render_template_string('<meta charset="utf-8"><h1 id="{{c.ok}}">{{name}}</h1><p data-testid="email">{{mail}}</p><a href="/signout" data-action="exit">Выход</a>',c=C,name=account['name'],mail=mail)
    @app.get('/signout')
    def signout():
        session.clear()
        return redirect('/signin')
    return app
if __name__=='__main__':
    build_portal().run('127.0.0.1',5050,debug=False)
