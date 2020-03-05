from flask import Flask, render_template, request, Response
app = Flask(__name__)

import json
import static_response

@app.route('/v3/auth/tokens', methods=['POST'])
def auth():        
    return Response(json.dumps(static_response.auth_token), 
                        status=201, 
                        mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

