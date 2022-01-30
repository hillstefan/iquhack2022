from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

Bootstrap(app)

@app.route('/')
def start_screen():
    return render_template('')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='42')
