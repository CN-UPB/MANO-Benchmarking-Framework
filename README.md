# Experiment Runner

MANO Benchmarking Framework (MBF) is a result of a small script that was used to run the experiments as part of the pg-scramble project. The idea of MBF is to provide MANO developers with a generic framework for running experiments on MANO. MBF mainly provides the following 


1. Easy interfacing with MANO instances by using `python-mano-wrappers`
2. Ability to run experiments with different service descriptors
3. Collection of performance metrics in convenient data format
4. Flexible graphing mechanism of the collected data. 


# Steps to run an experiment

## 1. Setup Pishahang and supporting software

1. Setup regular pishahang installation

2. Install netdata on the same vm using the following commands

        sudo su

        apt-get install zlib1g-dev uuid-dev libuv1-dev liblz4-dev libjudy-dev libssl-dev libmnl-dev gcc make git autoconf autoconf-archive autogen automake pkg-config curl python

        git clone --branch v1.19.0 https://github.com/netdata/netdata.git --depth=100
        cd netdata

        ./netdata-installer.sh

        # use browser and see <IP>:19999 to verify
                

3. Install supporting flask server to fetch metrics like deployment times and cleanup operations

        git clone https://github.com/CN-UPB/MANO-Benchmarking-Framework.git
        cd MANO-Benchmarking-Framework/experiment-runner/

        # Run flask server
        ./start_flask_helper_server.sh


## 2. Start vim-mocker on another machine and add vim to pishahang

Detailed info [here](MANO-Benchmarking-Framework/vim-mocker/README.md)


        git clone https://github.com/CN-UPB/MANO-Benchmarking-Framework.git
        cd MANO-Benchmarking-Framework
        cd vim-mocker
    
        ./build_run_docker_pishahang_os_remote.sh


## 3. Start experiment runner

        cd MANO-Benchmarking-Framework/experiment-runner

        # build experiment container
        ./build_experiment_runner.sh

        # run experiment container
        ./run_experiment_runner.sh


Once terminal is open inside the container, run one of the following experiment

        python run-emu-experiment-pishahang.py
        python run-emu-experiment-osm.py

        # or in background to avoid process from quitting after disconnection

        nohup python -u ./run-emu-experiment-sonata.py > emu-experiment.log &

## 4. Results

+ Data is stored in the EXP_RESULTS folder with the given name

+ Parsing and plotting are done with the files `csv-result-parser-rpm-v2.py` and `plot-graphs-v2.py`

# Additional commands

    # To show logs 
    sudo docker logs experiment-runner -f

    # This is for testing scaling plugin

# Add vim-mocker vims

+ Enter vim address as `vim-mocker`.
+ Other details can be anything

![add vim](/MANO-Benchmarking-Framework/vim-mocker/docs/vim-details.png)