from flask import Flask,request,render_template,redirect,url_for,send_from_directory
from flask_jwt import JWT
from flask_restful import Api
from werkzeug import security

import os

from resources.item import Item, ItemList
from resources.user import UserRegister
from security import authenticate,identity
from resources.store import StoreList,Store

from resources.post import sellpost,postList
from resources.seller import Seller,sellerLogin,sellerList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "soe"
api = Api(app)
jwt = JWT(app, authenticate, identity)
app.config['UPLOAD_FOLDER'] = 'imgs/'


# api.add_resource(Item, '/item/<string:name>')
# api.add_resource(UserRegister,'/register')
# api.add_resource(ItemList,'/items')
# api.add_resource(Store, '/store/<string:name>')
# api.add_resource(StoreList,'/stores')

api.add_resource(sellpost,'/create-post')
api.add_resource(postList,'/get-posts')
api.add_resource(Seller,'/register')
api.add_resource(sellerLogin,'/login')
api.add_resource(sellerList,'/get-sellers')


@app.route('/upload')
def upload_file1():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
      return url_for('uploaded_file',
                                filename=f.filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5001)

