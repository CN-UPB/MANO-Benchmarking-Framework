sudo docker stop vim-mocker
sudo docker rm vim-mocker
sudo docker build -t vim-mocker -f Dockerfile .
sudo docker run -d --name vim-mocker \
    -v $(pwd):/app \
    --env MANO=pishahang
    vim-mocker
