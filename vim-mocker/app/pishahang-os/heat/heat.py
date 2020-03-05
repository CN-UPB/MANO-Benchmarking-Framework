from flask import Flask, render_template, request, Response
app = Flask(__name__)

import json
import static_response


@app.route('/v1/<project_id>/stacks', methods=['POST'])
def stacks(project_id):
    return Response(json.dumps(static_response.stack_created), 
                        status=201, 
                        mimetype='application/json')


@app.route('/v1/<project_id>/stacks/<sonata_service>', methods=['GET'])
def stack_find(project_id, sonata_service):
    return Response(static_response.found, 
                        status=302, 
                        mimetype='text/plain')

# Send 'CREATE COMPLETE' first time
# then 'UPDATE_COMPLETE'
# then
@app.route('/v1/<project_id>/stacks/<sonata_service>/<sonata_id>', methods=['GET', 'PATCH'])
def stack_status(project_id, sonata_service, sonata_id):
    if request.method == 'GET':

        # return Response(json.dumps(static_response.create_complete),
        #                 status=200,
        #                 mimetype='application/json')

        return Response(json.dumps(static_response.stack_update_completed),
                        status=200,
                        mimetype='application/json')

    elif request.method == 'PATCH':
        return Response(json.dumps(static_response.patch),
                        status=202,
                        mimetype='text/plain')


@app.route('/v1/<project_id>/stacks/<sonata_service>/<sonata_id>/template', methods=['GET'])
def stack_template(project_id, sonata_service, sonata_id):
    return Response(json.dumps(static_response.template),
                        status=200,
                        mimetype='application/json')


@app.route('/v1/<project_id>/stacks/<sonata_service>/<sonata_id>/resources', methods=['GET'])
def stack_resources(project_id, sonata_service, sonata_id):
    return Response(json.dumps(static_response.resources),
                        status=200,
                        mimetype='application/json')


@app.route('/v1/<project_id>/stacks/<sonata_service>/<sonata_id>/resources/<resource_type>', methods=['GET'])
def stack_resources_status(project_id, sonata_service, sonata_id, resource_type):
    return Response(json.dumps(static_response.resources_status),
                        status=200,
                        mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8004)