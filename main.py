from flask import Flask
from routes.home import home
from routes.transactions import transaction


app = Flask(__name__)
app.register_blueprint(home, url_prefix="/")
app.register_blueprint(transaction, url_prefix="/transaction")


app.run(debug=True)
