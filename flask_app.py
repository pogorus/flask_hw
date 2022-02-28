from flask import Flask, jsonify, request
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date


PG_DSN = 'postgresql://admin:1234@127.0.0.1:5431/flask_project'
app = Flask('flask_app')
app.config.from_mapping(SQLALCHEMY_DATABASE_URI=PG_DSN)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class AdModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), index=True, unique=True)
    description = db.Column(db.String(100), index=True)
    create_date = db.Column(db.Date, default=date.today)
    owner = db.Column(db.String(50), index=True)


class AdView(MethodView):

    def get(self, ad_id):
        ad = AdModel.query.get(int(ad_id))
        return jsonify(
            {
                'id': ad.id,
                'title': ad.title,
                'description': ad.description,
                'create date': ad.create_date,
                'owner': ad.owner
            }
        )

    def post(self):
        new_ad = AdModel(**request.json)
        db.session.add(new_ad)
        db.session.commit()
        return jsonify(
            {
                'id': new_ad.id,
                'title': new_ad.title,
                'description': new_ad.description,
                'create date': new_ad.create_date,
                'owner': new_ad.owner
            }
        )

    def patch(self, ad_id):
        ad = AdModel.query.get(int(ad_id))
        for key in request.json.keys():
            setattr(ad, key, request.json.get(key))
        db.session.commit()
        return f'Advertisement #{ad_id} was successfully updated'



    def delete(self, ad_id):
        ad = AdModel.query.get(int(ad_id))
        db.session.delete(ad)
        db.session.commit()
        return f'Advertisement #{ad_id} was successfully deleted'


app.add_url_rule('/ad', view_func=AdView.as_view('ad_create'), methods=['POST'])
app.add_url_rule('/ad/<int:ad_id>', view_func=AdView.as_view('ad_get'), methods=['GET'])
app.add_url_rule('/ad/<int:ad_id>', view_func=AdView.as_view('ad_update'), methods=['PATCH'])
app.add_url_rule('/ad/<int:ad_id>', view_func=AdView.as_view('ad_delete'), methods=['DELETE'])
app.run(host='0.0.0.0', port=8000)
