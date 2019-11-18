
#Local Dependencies
import zlogger

#Package Dependencies

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route('/')
def output():
    print('Test Worked')
    return 'Hello World'

@app.route('/logging', methods = ['POST'])
def worker():
    data = request.get_json()

    # Call Archiver
    zlogger.archive_logs()

    return data

if __name__ == '__main__':
    app.run()
