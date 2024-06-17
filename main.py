from flask import Flask
from routes.home import home
from routes.transactions import transaction
from routes.categoria import categoria


app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(transaction, url_prefix="/transaction")
app.register_blueprint(categoria, url_prefix="/categoria")

app.run(debug=True)

"""
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
"""