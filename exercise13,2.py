# Implement a backend service that gets the ICAO code of an airport and then returns the name and location of 
# the airport in JSON format. The information is fetched from the airport database used on this course. For 
# example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK. The response must be in the 
# format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.


import mariadb
from flask import Flask

connection = mariadb.connect(
    host="localhost",
    database="flight_game",
    user="root",
    password="12345",
    autocommit=True
)

app = Flask(__name__)

@app.route('/airport/<icao>')
def get_airport(icao):
    try:
        sql = f"SELECT ident as ICAO, name, municipality as location FROM airport WHERE ident=%s"
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql, (icao,))
        response = cursor.fetchone()
        if response is None:
            error_response = {
                "message": "Airport not found"
            }
            return error_response, 404

        return response
    except TypeError:
        response = {
            'message': 'Invalid input',
            'status': 400
        }

        return response, 400

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint"
    }
    return response, 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)