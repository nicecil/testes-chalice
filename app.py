from chalice import Chalice
from chalice import BadRequestError
from chalice import NotFoundError
import json
from urllib.parse import urlparse, parse_qs
from chalicelib.routes import root


app = Chalice(app_name='helloworld')
app.debug = True

app.experimental_feature_flags.update([
	'BLUEPRINTS'
])

app.register_blueprint(root)


@app.route('/introspect')
def introspect():
	return app.current_request.to_dict()

##@app.route('/', methods=['POST'],
##			content_types=['application/x-www-form-urlencoded'])
##def index():
##	parsed = parse_qs(app.current_request.raw_body_decode())
##		'states': parsed.get('states', [])
##	}
# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
