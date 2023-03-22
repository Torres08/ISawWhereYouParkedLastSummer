from waitress import serve
from flask import Flask
from flask_restful import Resource, Api

# Create a Flask application instance and an API instance
app = Flask(__name__)
api = Api(app)

# Define a Resource class called Parking
class Parking(Resource):
    def get(self, license_plate):
        # Start a 30-minute free parking session for the given license plate
        # Just return a success message
        return {'message': f'30-minute free parking session has started for license plate {license_plate}.'}, 200


# Associate the Parking class with the endpoint /parking/<string:license_plate>
api.add_resource(Parking, '/parking/<string:license_plate>')

if __name__ == '__main__':
    # Basic server, localhost
    #app.run(debug=True) # no comments = default values = localhost 5000
                        # app.run(debug=True, port=8080)
                        # app.run(debug=True, host='0.0.0.0')
   
    host = 'localhost'
    port = 8000
    print(f'Starting server at http://{host}:{port}')
    serve(app, host=host, port=port) # using waitress
    