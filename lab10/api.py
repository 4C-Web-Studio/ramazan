from copy import deepcopy
from flask import Flask,request,jsonify
def create_api():
    app=Flask(__name__)
    members={1:dict(id=1,name='Pavel',username='pavel',email='pavel@example.com')}
    sequence=2
    def parse_user():
        value=request.get_json(silent=True)
        if not isinstance(value,dict):return None
        if not all(isinstance(value.get(k),str) and value[k].strip() for k in ('name','username','email')):return None
        if '@' not in value['email'] or '.' not in value['email'].split('@')[-1]:return None
        return {k:value[k] for k in ('name','username','email')}
    @app.route('/users',methods=['GET','POST'])
    def collection():
        nonlocal sequence
        if request.method=='GET':return jsonify(deepcopy(list(members.values())))
        item=parse_user()
        if item is None:return jsonify(error='validation'),400
        item['id']=sequence;members[sequence]=item;sequence+=1
        return jsonify(item),201
    @app.route('/users/<int:uid>',methods=['GET','PUT','DELETE'])
    def entity(uid):
        if uid not in members:return jsonify(error='not found'),404
        if request.method=='DELETE':del members[uid];return '',204
        if request.method=='PUT':
            item=parse_user()
            if item is None:return jsonify(error='validation'),400
            members[uid]=dict(item,id=uid)
        return jsonify(members[uid])
    return app
