from flask import Flask, render_template, request
app = Flask(__name__)

import sys
import docker
import json
import subprocess
import re
import statistics

client = docker.DockerClient(base_url='unix://container/path/docker.sock')

DOCKER_EXCLUDE = ['experiment-runner']
METRICS_MOCK_FILE = ""

@app.route('/')
def index_html():
    # print(client.containers.list(), file=sys.stderr)
    docker_list = {}
    for _container in client.containers.list():        
        if not _container.attrs["Name"][1:] in DOCKER_EXCLUDE:
            docker_list[_container.attrs["Name"][1:]] = _container.attrs["Id"]
        
    return render_template('index.html', docker_list=docker_list)

@app.route('/interactive')
def interactive_html():
    # print(client.containers.list(), file=sys.stderr)
    docker_list = {}
    for _container in client.containers.list():
        
        if not _container.attrs["Name"][1:] in DOCKER_EXCLUDE:
            docker_list[_container.attrs["Name"][1:]] = _container.attrs["Id"]
        
    return render_template('index-interactive.html', docker_list=docker_list)

@app.route('/save-experiment-data')
def save_data():
    # Print GET data
    # Make a list_url_query = [] 

    # http://${host}:19999/api/v1/data?chart=system.cpu&after=${after}&before=${before}&format=datasource&options=nonzero
    # http://${host}:19999/api/v1/data?chart=system.load&after=${after}&before=${before}&format=datasource&options=nonzero
    # http://${host}:19999/api/v1/data?chart=system.ram&format=datasource&after=${after}&before=${before}&options=nonzero
    # http://${host}:19999/api/v1/data?chart=system.net&format=datasource&after=${after}&before=${before}&group=average&gtime=0&datasource&options=nonzeroseconds
    # http://${host}:19999/api/v1/data?chart=system.io&format=datasource&after=${after}&before=${before}&group=average&gtime=0&datasource&options=nonzeroseconds


    # http://${host}:19999/api/v1/data?chart=cgroup_{{ _name }}.cpu_per_core&format=datasource&after=${after}&before=${before}&group=average&gtime=0&datasource&options=nonzeroseconds
    # http://${host}:19999/api/v1/data?chart=cgroup_{{ _name }}.throttle_io&format=datasource&after=${after}&before=${before}&group=average&gtime=0&datasource&options=nonzeroseconds
    # http://${host}:19999/api/v1/data?chart=cgroup_{{ _name }}.mem_usage&format=datasource&after=${after}&before=${before}&group=average&gtime=0&datasource&options=nonzeroseconds


    docker_list = {}
    for _container in client.containers.list():        
        if not _container.attrs["Name"][1:] in DOCKER_EXCLUDE:
            docker_list[_container.attrs["Name"][1:]] = _container.attrs["Id"]
            # format url and list_url_query.append() 

    return render_template('index.html', docker_list=docker_list)


@app.route('/scale')
def scale_metrics():
    try:
        _scale_metrics = request.args.get('scale_metrics')
        with open('/debugscale', 'w') as _file:
            _file.write("{0}\n".format(_scale_metrics))
    except Exception as e:
        with open('/debugscale', 'w') as _file:
            _file.write("0.5,0.5,0.5\n")
        return "Error"

    return "Done"


@app.route('/get_docker_names')
def docker_names():
    try:
        # print(client.containers.list(), file=sys.stderr)
        docker_list = {}
        for _container in client.containers.list():
            
            if not _container.attrs["Name"][1:] in DOCKER_EXCLUDE:
                docker_list[_container.attrs["Name"][1:]] = _container.attrs["Id"]
            
        return json.dumps(docker_list)

    except Exception as e:
        return str(e)


@app.route('/del_requests')
def del_requests():
    try:
        result = subprocess.check_output(
            ['docker exec son-postgres psql -h localhost -U postgres -d gatekeeper -c "DELETE FROM requests"'], shell=True)
    except subprocess.CalledProcessError as e:
        return "An error occurred while trying to fetch task status updates."

    return 'Success %s' % (result)

@app.route('/restart_pishahang')
def restart_pishahang():
    try:
        result = subprocess.check_output(
            ['bash /home/thesismano4/MANO-Benchmarking-Framework/vim-mocker/run_docker_pishahang_os.sh'], shell=True)
        result = subprocess.check_output(
            ['bash /home/thesismano4/Pishahang/run_pishahang_changes.sh 131.234.28.240'], shell=True)
    except subprocess.CalledProcessError as e:
        return "An error occurred while trying to fetch task status updates."

    return 'Success %s' % (result)

@app.route('/get_pishahang_status')
def get_pishahang_status():
    try:
        result = subprocess.check_output(
            ['docker exec son-postgres psql -h localhost -U postgres -d gatekeeper -c "SELECT count(*) FILTER (WHERE status = \'READY\') AS active, count(*) FILTER (WHERE status = \'INSTANTIATING\') AS build, count(*) FILTER (WHERE status = \'ERROR\') AS error FROM requests;"'], shell=True)
        
        result = result.split()
        _result = '{ready},{init},{error}'.format(ready=int(result[6]), init=int(result[8]), error=int(result[10]))

    except subprocess.CalledProcessError as e:
        return "An error occurred while trying to fetch task status updates."

    return _result


@app.route('/get_pishahang_init_times')
def get_pishahang_init_times():
    try:
        cmd = 'docker exec son-postgres psql -h localhost -U postgres -d gatekeeper -c "Select extract(epoch from updated_at-created_at) from requests;"'

        result = subprocess.check_output([cmd], shell=True)
        result = result.split(b'\n')

        new_map = []
        for item in result:
            try:
                flitem = float(item)
            except ValueError:
                continue
            new_map.append(flitem)

        _result = "{mean},{std},{max},{min}".format(
            mean=statistics.stdev(new_map),
            std=statistics.mean(new_map),
            max=max(new_map),
            min=min(new_map)
        )

    except subprocess.CalledProcessError as e:
        return "An error occurred while trying to fetch task status updates."

    return _result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5055)


# sudo lsof -i :5055
# nohup sudo python3 -m flask run --host=0.0.0.0 --port 5055 &
# curl localhost:5055/restart_pishahang
# curl localhost:5055/del_requests