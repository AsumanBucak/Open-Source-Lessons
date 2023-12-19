from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pandas
import requests

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get (self):
        url = ""
        response = requests.get(url)
        data = response.json()
        return {'data' : data}, 200
    
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=6767)
    app.run()
