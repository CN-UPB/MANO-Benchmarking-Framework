from flask import Flask, render_template, request, redirect, jsonify, Response
app = Flask(__name__)

import json
import static_response
import uuid
import threading
import time

server_map = ["test"]

lock = threading.Lock()

# def update_thread():
#     global stack_map
#     while True:
#         with lock:
#             stack_map['uptime'] = stack_map.get('uptime', 0) + 1
#         time.sleep(1.0)

@app.route('/v2.1/<id>/flavors', methods=['POST'])
def flavors(id):
    _data = request.json

    return Response(json.dumps(static_response.flavor_create(_data)), 
                        status=200, 
                        mimetype='application/json')


@app.route('/v2.1/flavors/detail', methods=['GET'])
def flavors_detail():        
    return Response(json.dumps(static_response.flavors_detail), 
                        status=200, 
                        mimetype='application/json')

@app.route('/v2.1/<id>/flavors/detail', methods=['GET'])
def flavors_id_detail(id):        
    return Response(json.dumps(static_response.flavors_detail), 
                        status=200, 
                        mimetype='application/json')

@app.route('/v2.1/<id1>/flavors/<id>/os-extra_specs', methods=['GET'])
def flavors_extra(id1, id):
    return Response(json.dumps(static_response.flavor_extra), 
                        status=200, 
                        mimetype='application/json')


@app.route('/v2.1/<id>/servers', methods=['POST'])
def servers(id):
    global server_map
    _server_id = str(uuid.uuid4())
    app.logger.info('Server creation request Name : %s', _server_id)

    with lock:
        server_map.append(_server_id)
        
    return Response(json.dumps(static_response.servers(_server_id)), 
                        status=202, 
                        mimetype='application/json')


@app.route('/v2.1/<id>/servers/detail', methods=['GET'])
def servers_detail(id):        
    with lock:
        return Response(json.dumps(static_response.servers_details(server_map)), 
                            status=200, 
                            mimetype='application/json')


# @app.route('/v2.1/<id>/servers/<server_id>', methods=['GET'])
# def server_id(id, server_id):        
#     return Response(json.dumps(static_response.server_id(server_id)), 
#                         status=200, 
#                         mimetype='application/json')


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
    # threading.Thread(target=update_thread).start()
    app.run(debug=True, host='0.0.0.0', port=9775)

