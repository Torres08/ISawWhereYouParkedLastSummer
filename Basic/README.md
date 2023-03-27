# ISawWhereYouParkedLastSummer

This API allows you to check whether a 30-minute free parking session has started for a given license plate number using waitress.

## Requirements

- Python 3.x
- Flask
- Flask-RESTful
- waitress
- (Optional) postman

## Installation

1. Clone this repository to your local machine:

```bash
    git clone https://github.com/Torres08/ISawWhereYouParkedLastSummer.git
```

2. Install the required packages:

```bash
  pip install flask flask_restful
  pip install waitress
```


## Usage

1. Start the Flask application:

```bash
  python main.py
```


2. Make a GET request to the API with the license plate number that you want to check, for example using Postman:

```bash
  http://localhost:8000/parking/<license_plate>
```

    Replace `<license_plate>` with the license plate number that you want to check. for example  http://localhost:8000/parking/ABC123

3. The API will return a success message saying that the 30-minute free parking session has started for the given license plate number:

```bash
    {
    "message": "30-minute free parking session has started for license plate ABC123."
    }
```


## Note

This implementation does not check for the existence of the license plate in a database or start a timer for the free parking session. It simply returns a success message for any valid license plate provided in the URL. You can modify this implementation to suit your specific needs.








