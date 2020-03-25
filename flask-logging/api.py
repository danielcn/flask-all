import os
import logging

from src.logger.logger.logger_handler import LoggerHandler

from flask import Flask

@app.route('/')
def index():
    LoggerHandler.log_info('Hello, world!')
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)