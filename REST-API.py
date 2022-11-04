from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Games(Resource):
    def get(self):
        data = pd.read_csv('games.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('game', required=True)
        parser.add_argument('releaseYear', required=True)
        parser.add_argument('platform', required=True)
        args = parser.parse_args()

        data = pd.read_csv('games.csv')

        new_data = pd.DataFrame({
            'game'      : [args['game']],
            'releaseYear'       : [args['releaseYear']],
            'platform'      : [args['platform']]
        })

        data = data.append(new_data, ignore_index = True)
        data.to_csv('games.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('game', required=True)
        args = parser.parse_args()

        data = pd.read_csv('games.csv')

        data = data[data['game'] != args['game']]

        data.to_csv('games.csv', index=False)
        return {'message' : 'Record deleted successfully.'}, 200

class ReleaseYear(Resource):
    def get(self,releaseYear):
        data = pd.read_csv('games.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['releaseYear'] == releaseYear :
                return {'data' : entry}, 200
        return {'message' : 'No entry found with this year !'}, 200
    
class Game(Resource):
    def get(self,game):
        data = pd.read_csv('games.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['game'] == game :
                return {'data' : entry}, 200
        return {'message' : 'No entry found with this game !'}, 200

class Welcome(Resource):
    def get(self):
        return {'message' : 'Welcome to Games Rest Api !'}, 200
    
class Number(Resource):
    def get(self,number):
        result = number*5
        return {'result' : result }, 200          

api.add_resource(Welcome, '/')
api.add_resource(Games, '/Games')
api.add_resource(ReleaseYear, '/<int:releaseYear>')
api.add_resource(Game, '/<string:game>')
api.add_resource(Number, '/Number/<int:number>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    app.run()