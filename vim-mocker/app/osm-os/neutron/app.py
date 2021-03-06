from flask import Flask, render_template, request, Response
app = Flask(__name__)

import json
import static_response
import uuid
import threading
import time

port_map = {}

lock = threading.Lock()

@app.route('/v2.0/networks', methods=['GET'])
def networks():
    if request.args:
        args = request.args

        if "id" in args:
            _id = args.get("id")

            app.logger.info('### Networks ID: %s', _id)

            return Response(json.dumps(static_response.networks_status(_id)), 
                                status=200, 
                                mimetype='application/json')

        if "admin_state_up" in args:
            _admin_state_up = args.get("admin_state_up")

            return Response(json.dumps(static_response.networks), 
                                status=200, 
                                mimetype='application/json')

    else:
        return "No query string received", 200 


@app.route('/v2.0/networks/<network_id>', methods=['GET'])
def networks_id(network_id):

    return Response(json.dumps(static_response.network), 
                        status=200, 
                        mimetype='application/json')


@app.route('/v2.0/ports', methods=['POST', 'GET'])
def ports():
    global port_map
    if request.method == 'POST':
        _data = request.json

        app.logger.info('### PORTS: %s', _data)

        with lock:
            port_map[_data["port"]["network_id"]] = ""

        return Response(json.dumps(static_response.port(_data)), 
                            status=201, 
                            mimetype='application/json')
    else:
        return Response(json.dumps(static_response.ports()), 
                            status=200, 
                            mimetype='application/json')



@app.route('/v2.0/subnets/<subnet_id>', methods=['GET'])
def subnet(subnet_id):

    app.logger.info('### Subnets ID: %s', subnet_id)

    return Response(json.dumps(static_response.subnets(subnet_id)), 
                        status=200, 
                        mimetype='application/json')


@app.route('/v2.0/<req_type>/<req_id>', methods=['DELETE'])
def delete_data(req_type, req_id):
    if req_type == "ports":
        return Response("", 
                        status=204, 
                        mimetype='application/json')

@app.route('/v2.0/floatingips', methods=['GET'])
def floatingips():
    return Response(json.dumps(static_response.floatingips), 
                        status=200, 
                        mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10697)