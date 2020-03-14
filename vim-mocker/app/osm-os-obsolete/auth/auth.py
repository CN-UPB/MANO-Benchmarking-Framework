from flask import Flask, render_template, request, Response
app = Flask(__name__)

import json
import static_response

@app.route('/identity/v3/auth/tokens', methods=['POST'])
def auth():
    resp = Response(json.dumps(static_response.auth_token), 
                        status=201, 
                        mimetype='application/json')
    resp.headers['X-Subject-Token'] = 'gAAAAABeZQ7ORzPsBzYtdwbX_u_DKruOwFCG1nQd47E2FqohvNPSbUcMlSpBYjeahxncF7sDYEoEs2BwEbQrmO0nUA2Ha88qWcWTDwwjnlG1_AtttlKz51gJj2l-ydH8Jozg8UFRWsvue5aDxsts5V7oa41zdBa82Q5f14udkCuhjIzO_DEf25w'

    return resp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

