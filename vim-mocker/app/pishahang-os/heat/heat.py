from flask import Flask, render_template, request, jsonify, Response
app = Flask(__name__)

import json
import static_response
import uuid
import threading
import time

stack_map = {}

lock = threading.Lock()

def replace_in_dict(input, variables):
    result = {}
    for key, value in input.iteritems():
        if isinstance(value, dict):
            result[key] = replace_in_dict(value, variables)
        else:
            result[key] = value % variables
    return result

def update_thread():
    global stack_map
    while True:
        with lock:
            stack_map['uptime'] = stack_map.get('uptime', 0) + 1
        time.sleep(1.0)

@app.route('/v1/<project_id>/stacks', methods=['POST'])
def stacks(project_id):
    _data = request.json
    _response = static_response.stack_created

    # Create new stack ID
    _stack_id = str(uuid.uuid4())
    _stack_name = _data["stack_name"]

    app.logger.info('Stack creation request Name %s: %s', _stack_name, _stack_id)

    global stack_map
    with lock:
        stack_map[_stack_name] = {}
        stack_map[_stack_name]['id'] = _stack_id
        stack_map[_stack_name]['status'] = 0

    # with lock:
    #     app.logger.info(stack_map)

    _response["stack"]["id"] = _stack_id
    _response["stack"]["links"][0]["href"] = _response["stack"]["links"][0]["href"].format(
                                                stack_name = _stack_name,
                                                stack_id = _stack_id)

    return Response(json.dumps(_response), 
                        status=201, 
                        mimetype='application/json')


@app.route('/v1/<project_id>/stacks/<stack_name>', methods=['GET'])
def stack_find(project_id, stack_name):
    _response = static_response.found

    # Create new stack ID
    _stack_name = stack_name
    with lock:
        _stack_id = stack_map[_stack_name]['id']

    app.logger.info('Stack creation request: %s', _stack_id)

    _response = _response.format(
                                stack_name = _stack_name,
                                stack_id = _stack_id)

    return Response(_response, 
                        status=302, 
                        mimetype='text/plain')

# Send 'CREATE COMPLETE' first time
# then 'UPDATE_COMPLETE'
# then
@app.route('/v1/<project_id>/stacks/<stack_name>/<stack_id>', methods=['GET', 'PATCH'])
def stack_status(project_id, stack_name, stack_id):
    if request.method == 'GET':
        with lock:
            if stack_map[stack_name]['status'] == 0:
                stack_map[stack_name]['status'] += 1
                return Response(json.dumps(static_response.create_started_0(stack_id, stack_name)),
                                status=200,
                                mimetype='application/json')

            elif stack_map[stack_name]['status'] == 1:
                stack_map[stack_name]['status'] += 1
                return Response(json.dumps(static_response.create_complete_1(stack_id, stack_name)),
                                status=200,
                                mimetype='application/json')

            elif stack_map[stack_name]['status'] == 2:
                stack_map[stack_name]['status'] += 1
                return Response(json.dumps(static_response.stack_update_started_2(stack_id, stack_name)),
                                status=200,
                                mimetype='application/json')

            else:
                return Response(json.dumps(static_response.stack_update_completed_3(stack_id, stack_name)),
                                status=200,
                                mimetype='application/json')

    elif request.method == 'PATCH':
        return Response(json.dumps(static_response.patch),
                        status=202,
                        mimetype='text/plain')


@app.route('/v1/<project_id>/stacks/<stack_name>/<stack_id>/template', methods=['GET'])
def stack_template(project_id, stack_name, stack_id):
    return Response(json.dumps(static_response.template),
                        status=200,
                        mimetype='application/json')


@app.route('/v1/<project_id>/stacks/<stack_name>/<stack_id>/resources', methods=['GET'])
def stack_resources(project_id, stack_name, stack_id):
    return Response(json.dumps(static_response.resources),
                        status=200,
                        mimetype='application/json')


@app.route('/v1/<project_id>/stacks/<stack_name>/<stack_id>/resources/<resource_name>', methods=['GET'])
def stack_resources_status(project_id, stack_name, stack_id, resource_name):
    return Response(json.dumps(static_response.resources_status(stack_id, stack_name, resource_name)),
                        status=200,
                        mimetype='application/json')


if __name__ == '__main__':
    threading.Thread(target=update_thread).start()
    app.run(debug=True, host='0.0.0.0', port=8004)