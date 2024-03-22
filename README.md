# ISawWhereYouParkedLastSummer

This is a simple REST API for starting a 30-minute free parking session for a given license plate. Basic folder is an old version of the API.

## Requirements

- Python 3.x
- Flask
- Flask-RESTful
- waitress
- (Optional) postman

## Installation

1. Clone the repository: `git clone https://github.com/username/free-parking-api.git`
2. Install the required packages: `pip install flask flask_restful waitress`

## Usage

Start the server by running `python main.py`. The API will be available at `http://localhost:8000`.

### Endpoint

#### `GET /parking`

Starts a 30-minute free parking session for the given license plate. Returns a success message.

In postman, 
Set the request method to "POST" and the request URL to "http://localhost:8000/parking".
go to body, select raw and JSON and copy  and send it

```bash
{
    "license_plate": "ABC1234"
}
```

If the request is successful, you will receive a JSON response with a success message:

```bash
{
    "message": "30-minute free parking session has started for license plate ABC123."
}
```

to delete it send a "DELETE" http://localhost:8000/parking/ABC1234


### Error handling
If you make a request with an invalid license plate (e.g. a license plate that is too long), you will receive a JSON response with an error message and a status code of 400:
```bash
{
    "error": "License plate ABC123 already has an active parking session."
}
```

### Restful Rules
1. Use HTTP methods correctly: Uses the GET method

2. Use resource URIs:  The API endpoint /parking <string:license_plate> is a resource URI

3. Use HTTP status codes: The API returns HTTP status codes (such as 200 for success and 404 for resource not found) to indicate the success or failure

4. Uses JSON data format: The API returns data in the JSON format

5. Use meaningful and consistent naming convention: For example, the resource URI /parking/<string:license_plate> is consistent with the method name get





