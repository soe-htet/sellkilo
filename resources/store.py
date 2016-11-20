from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.get_by_name(name)
        if store:
            return store
        else:
            return {'message', 'store not found'}, 404

    def post(self, name):
        if StoreModel.get_by_name(name):
            return {'messge','store alerady exit'}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'error occur while inserting'}, 500

        return store.json(), 201

    def delete(self, name):
        if StoreModel.get_by_name(name) is None:
            return {'messge','store doesn\'t exit'}, 404
        store = StoreModel.get_by_name(name)
        store.delete_from_db()
        return {'message','store deleted'}, 200


class StoreList(Resource):
    def get(self):
        return [{'stores': [store.json() for store in StoreModel.query.all()]}]