import flask
import os
flaskerr = flask.Flask(__name__)
@flaskerr.route('/')
def flaskerre():
      return '8₹83'


flaskerr.run(host='0.0.0.0',80)
