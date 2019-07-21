from flask import Flask, request, redirect
from flasgger import Swagger
import radio_helper as rh
import os

app = Flask(__name__)
swagger = Swagger(app)
host_ip = 'localhost'
if 'host_ip' in os.environ.keys() and os.environ['host_ip'] is not None:
    host_ip = os.environ['host_ip']


@app.route('/radios/<int:id>', methods=["POST"])
def post_radio(id):
    """endpoint for saving radio
        This is using docstrings for specifications.
        ---
        parameters:
          - name: id
            type: int
            in: path
            required: true
          - name: alias
            type: string
            in: payload
            required: true
          - name : allowed_locations
            type: string array
            in: payload
            required: true
        responses:
          200:
            description: radio saved successfully
            schema:
            examples:
              { "Message": "success", "StatusCode": "200"}
          403:
            description: radio already exists
            schema:
            examples:
              {'StatusCode': '403', 'Message': 'radio with ID: ... already exists'}
        """
    data = request.get_json(force=True, silent=True)
    resp = rh.post_radio(data, id)

    return resp


@app.route('/radios/<int:id>/location', methods=["POST"])
def post_radio_location(id):
    """endpoint for saving radio location
            This is using docstrings for specifications.
            ---
            parameters:
              - name: id
                type: int
                in: path
                required: true
              - name: location
                type: string
                in: payload
                required: true
            responses:
              200:
                description: radio location saved successfully
                schema:
                examples:
                  { "Message": "success", "StatusCode": "200"}
              403:
                description: invalid location
                schema:
                examples:
                  {'StatusCode': '403', 'Message': 'invalid location'}
              404:
                description: invalid radio
                schema:
                examples:
                  {'StatusCode': '404', 'Message': 'No radio exist with id:...'}
            """
    data = request.get_json(force=True, silent=True)
    resp = rh.post_radio_location(data, id)

    return resp


@app.route('/radios/<int:id>/location', methods=["GET"])
def get_radio_location(id):
    """endpoint for getting radio location
                This is using docstrings for specifications.
                ---
                parameters:
                    - name: id
                      type: int
                      in: path
                      required: true
                responses:
                  200:
                    description: get radio location
                    schema:
                    examples:
                      { "Message": "success", "StatusCode": "200"}
                  404:
                    description: location not found
                    schema:
                    examples:
                      {'StatusCode': '404', 'Message': 'location not found'}
                  404:
                    description: invalid radio
                    schema:
                    examples:
                      {'StatusCode': '404', 'Message': 'No radio exist with id:...'}
                """
    resp = rh.get_radio_location(id)

    return resp


@app.route("/")
def spec():
    return redirect("/apidocs")


if __name__ == '__main__':
    app.run(host=host_ip, port=80)
