sudo docker stop vim-mocker
sudo docker rm vim-mocker
sudo docker build -t vim-mocker -f Dockerfile .
sudo docker run -d --name vim-mocker \
    -p 5000:5000 \
    -p 8004:8004 \
    -p 8774:8774 \
    -p 9292:9292 \
    -v $(pwd):/app \
    --env MANO=pishahang \
    vim-mocker
