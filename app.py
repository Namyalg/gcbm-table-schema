from flask import Flask, request
from config_table import rename_columns

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'


@app.route('/config', methods=['POST'])
def config_table():
    return {'response' : rename_columns(request.get_json())}


if __name__ == "__main__":
    app.run(debug=True)