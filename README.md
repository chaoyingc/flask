## This repository provides an exemple of how to use flask to create an tweet detector API and dockerize it.
#### requirements:
- python3 (it's more simle with python3 than python2)
- flask ([documentation](https://flask.palletsprojects.com/en/1.1.x/installation/#) for the installation )
- docker
#### how it works:
1,download all files from this repository by command line:
```
$ git clone https://github.com/chaoyingc/flask.git
$ cd flask
```
2, execute app.py:
```
$ export FLASK_APP=app.py
$ flask run
```
Copy the link that it shows and paste it in your browser, you will get the flask api web page for testing the tweet sentiment.
