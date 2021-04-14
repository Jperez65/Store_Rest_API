from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store= StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {'Message': 'Store not found'}, 404


    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'Message': 'A store with name {} already exits'.format(name)}, 400
        
        store = StoreModel(name)

        try :
            store.save_to_db()
        except:
            return {'message': 'An error ocurred inside the database'}, 500

        return store.json()

    def delete(self, name):
        store= StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'Message': 'store already deleted'}


class StoreList(Resource):
       
        def get(self):
            return {'Stores': [Store.json() for store in StoreModel.query.all()]}