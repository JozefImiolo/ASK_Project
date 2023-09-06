# ASK_Project_2023
ASK subject - study course. Topic of project: Time-series database QuestDB for storing stock market data: examples, visualization using D3.js


## How to run

### Python
pip install -r requirements.txt

### Docker 
    docker run  -p 9000:9000 -p 9009:9009 -p 8812:8812 -p 9003:9003 questdb/questdb:7.3.1


### WINDOWS - installing native questdb

    How to install questdb:
    1) downolad the binaries and follow the instructions in:
    https://questdb.io/docs/get-started/binaries/

    unpack the file
    tar -xvf questdb-7.3.1-no-jre-bin.tar.gz

    -- To run the instance as a windows service (preferably as a privileged account):
    questdb.exe install
    questdb.exe start

    ______________________________________________________

