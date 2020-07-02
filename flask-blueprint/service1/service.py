from flask import Blueprint

service1 = Blueprint('service1', __name__)

@service1('/service1')
def service1():
  return 'service1'
