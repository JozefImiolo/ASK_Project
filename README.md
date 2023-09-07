# ASK_Project
ASK subject - study course. Topic of project: Time-series database QuestDB for storing stock market data: examples, visualization using D3.js


## How to run
### Docker - build / compose questdb database - to build the vm or to restart previously stopped vm
    docker-compose up -d
### how to stop the container - however keep the data
    docker-compose stop
### how to delete the container
    docker-compose down

### Python - install dependencies
    python -m venv myenv
    .\myenv\Scripts\activate.bat
    pip install -r requirements.txt

### FLask app - launch app
    python -m flask run

### App website - visit website
    http://127.0.0.1:5000