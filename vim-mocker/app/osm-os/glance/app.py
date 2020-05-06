from flask import Flask, render_template, request, Response
app = Flask(__name__)

import json
import static_response


@app.route('/v2/images', methods=['GET'])
def images():        
    return Response(json.dumps(static_response.images), 
                        status=200, 
                        mimetype='application/json')

@app.route('/v2/schemas/image', methods=['GET'])
def images_schemas():        
    resp = dict()
    resp['name'] = 'someImageName'
    resp['properties'] = dict()
    resp['links'] = list()

    return Response(json.dumps(resp), 
                        status=200, 
                        mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10243)

