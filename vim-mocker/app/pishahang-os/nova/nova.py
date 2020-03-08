from flask import Flask, render_template, request, Response
app = Flask(__name__)

import json
import static_response


@app.route('/v2.1/<project_id>/limits', methods=['GET'])
def limits(project_id):        
    return Response(json.dumps(static_response.limits), 
                        status=200, 
                        mimetype='application/json')


@app.route('/v2.1/<project_id>/flavors/detail', methods=['GET'])
def flavors(project_id):        
    return Response(json.dumps(static_response.flavors), 
                        status=200, 
                        mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=8774)

