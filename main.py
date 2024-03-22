# Import the necessary modules
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound
from waitress import serve

# Create a Flask application instance
app = Flask(__name__)

# Define a dictionary to store parking sessions
parking_sessions = {}

# Define a route for starting a parking session
@app.route('/parking', methods=['POST'])
def start_parking_session():
    # Get the license plate number from the request body
    license_plate = request.json.get('license_plate')
    if not license_plate:
        # Return a 400 Bad Request error if the license plate is not provided
        raise BadRequest('License plate number is missing')

    # Check if a parking session already exists for the given license plate
    if license_plate in parking_sessions:
        # Return a 400 Bad Request error if a parking session already exists
        raise BadRequest('Parking session already exists for this license plate')

    # Start a new parking session for the given license plate
    parking_sessions[license_plate] = True

    # Return a success message with the license plate number
    return jsonify({'message': f'Parking session started for license plate {license_plate}.'}), 201

# Define a route for ending a parking session
@app.route('/parking/<string:license_plate>', methods=['DELETE'])
def end_parking_session(license_plate):
    # Check if a parking session exists for the given license plate
    if license_plate not in parking_sessions:
        # Return a 404 Not Found error if a parking session doesn't exist
        raise NotFound('No parking session found for this license plate')

    # End the parking session for the given license plate
    del parking_sessions[license_plate]

    # Return a success message with the license plate number
    return jsonify({'message': f'Parking session ended for license plate {license_plate}.'}), 200

# Run the server if the script is run directly
if __name__ == '__main__':
    # Define the host and port
    host = 'localhost'
    port = 8000

    # Print a message to indicate that the server is starting
    print(f'Starting server at http://{host}:{port}')

    # Start the server using waitress
    serve(app, host=host, port=port)

