from flask import Flask

RESOURCE_FOLDER = 'C:\\git\\iquhack-2022\\resources'

app = Flask(__name__)
app.config['RESOURCE_FOLDER'] = RESOURCE_FOLDER
