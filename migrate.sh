export FLASK_APP=flask_app.py
flask db init
flask db migrate
flask db upgrade