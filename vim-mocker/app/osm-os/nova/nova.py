from flask import Flask, render_template, request, Response
app = Flask(__name__)

import json
import static_response
import uuid


@app.route('/v2.1/flavors', methods=['POST'])
def flavors():
    _data = request.json

    return Response(json.dumps(static_response.flavor_create(_data)), 
                        status=200, 
                        mimetype='application/json')


@app.route('/v2.1/flavors/detail', methods=['GET'])
def flavors_detail():        
    return Response(json.dumps(static_response.flavors_detail), 
                        status=200, 
                        mimetype='application/json')


@app.route('/v2.1/flavors/<id>/os-extra_specs', methods=['GET'])
def flavors_extra(id):
    return Response(json.dumps(static_response.flavor_extra), 
                        status=200, 
                        mimetype='application/json')


@app.route('/v2.1/servers', methods=['POST'])
def servers():
    _server_id = str(uuid.uuid4())
    return Response(json.dumps(static_response.servers(_server_id)), 
                        status=202, 
                        mimetype='application/json')


@app.route('/v2.1/servers/detail', methods=['GET'])
def servers_detail():        
    return Response(json.dumps(static_response.server_detail), 
                        status=200, 
                        mimetype='application/json')


@app.route('/v2.1/servers/<server_id>', methods=['GET'])
def server_id(server_id):        
    return Response(json.dumps(static_response.server_id(server_id)), 
                        status=200, 
                        mimetype='application/json')


@app.route('/v2.1/<req_type>/<req_id>', methods=['DELETE'])
def delete_data(req_type, req_id):
    if req_type == "flavors":
        return Response("", 
                        status=202, 
                        mimetype='application/json')
    elif req_type == "servers":
        return Response("",
                        status=204, 
                        mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8774)

