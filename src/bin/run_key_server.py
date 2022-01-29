from flask import Flask, make_response, jsonify

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/generate_keys', methods=['POST'])
def generate_keys():
    # TODO: execute Key generation here
    ret = {
        'public_key': 'key',
        'private_key': 'key'
    }
    return make_response(jsonify(ret))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='69')
