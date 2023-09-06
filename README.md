# ASK_Project
ASK subject - study course. Topic of project: Time-series database QuestDB for storing stock market data: examples, visualization using D3.js


## How to run

### Python - install dependencies
    python -m venv myenv
    .\myenv\Scripts\activate.bat
    pip install -r requirements.txt

### Docker - run questdb database
    docker run  -p 9000:9000 -p 9009:9009 -p 8812:8812 -p 9003:9003 questdb/questdb:7.3.1

### FLask app - launch app
    python -m flask run

### App website - visit website
    http://127.0.0.1:5000