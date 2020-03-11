from flask import Flask, render_template, request, Response
app = Flask(__name__)

import json
import static_response

@app.route('/v2.0/networks', methods=['GET'])
def networks():
    if request.args:
        args = request.args

        if "id" in args:
            _id = args.get("id")

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


@app.route('/v2.0/ports', methods=['POST'])
def ports():
    _data = request.json

    return Response(json.dumps(static_response.ports(_data)), 
                        status=201, 
                        mimetype='application/json')


@app.route('/v2.0/subnets/<subnet_id>', methods=['GET'])
def subnet(subnet_id):
    return Response(json.dumps(static_response.subnets(subnet_id)), 
                        status=201, 
                        mimetype='application/json')


@app.route('/v2.0/<req_type>/<req_id>', methods=['DELETE'])
def delete_data(req_type, req_id):
    if req_type == "ports":
        return Response("", 
                        status=204, 
                        mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)