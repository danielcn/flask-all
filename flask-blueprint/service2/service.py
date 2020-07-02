from flask import Blueprint

service2 = Blueprint('service2', __name__)

@service2('/service2')
def service2():
  return 'service1'
