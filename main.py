from flask import Flask
from routes.home import home
from routes.transactions import transaction
from routes.categoria import categoria


app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(transaction, url_prefix="/transaction")
app.register_blueprint(categoria, url_prefix="/categoria")


app.run(debug=True)
