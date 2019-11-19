
#Local Dependencies
import zlogger
import config

#Package Dependencies

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route('/')
def output():
    print('Test Worked')
    return 'Hello World'

@app.route('/logging')
def worker():
    # Call Archiver
    zlogger.archive_logs()

    return 'Process Completed'

def main():

    #Global Variables init
    config.init()

if __name__ == '__main__':
    main()
    app.run()
