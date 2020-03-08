from flask import Flask, render_template, request, Response
app = Flask(__name__)

import json
import static_response


@app.route('/v2/images', methods=['GET'])
def images():        
    return Response(json.dumps(static_response.images), 
                        status=200, 
                        mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=9292)

