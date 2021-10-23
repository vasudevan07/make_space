from flask import Flask, request, jsonify
from scheduler import main
from meeting_rooms import Cave, Tower, Mansion
import json

app = Flask(__name__)
#cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST")
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

@app.route('/meeting/vacancy', methods=['GET'])
def get_vacant_rooms():
    try:
        start_time = request.args.get('startTime')
        end_time = request.args.get("endTime")
        print(start_time)
        input_val = f"VACANCY {start_time} {end_time}"
        response = main(rooms_dict=rooms, input_val=input_val)
        if "VACANT" in response:
            return jsonify({'rooms': [], 'message': 'Sorry! No Vacant Room available'}), 400
        elif "INCORRECT" in response:
            return jsonify({'rooms': [], 'message': 'Error Occured. Please check the input'}), 500
        else:
            vacant_rooms = response.split()
            return jsonify({'rooms': vacant_rooms, 'message': 'Successfull!'}), 200

    except Exception as e:

        return jsonify({'rooms': [], 'message': f"Error Occured. {repr(e)}"}), 500

@app.route('/meeting/book', methods=['POST'])
def book_room():
    print(request.data)
    input_payload = json.loads(request.data)
    start_time = input_payload.get("startTime")
    if not start_time:
        response =  jsonify({'rooms': [], 'message': "startTime value cannot be empty"})
        # response.headers.add("Access-Control-Allow-Origin", "*")
        # response.headers.add("Access-Control-Allow-Methods", "POST")
        return  response, 400
    end_time = input_payload.get("endTime")
    if not end_time:
        response = jsonify({'rooms': [], 'message': "endTime value cannot be empty"})
        # response.headers.add("Access-Control-Allow-Origin", "*")
        # response.headers.add("Access-Control-Allow-Methods", "POST")
        return response, 400
    capacity = input_payload.get("capacity")
    if not capacity:
        response = jsonify({'rooms': [], 'message': "capacity value cannot be empty"})
        # response.headers.add("Access-Control-Allow-Origin", "*")
        # response.headers.add("Access-Control-Allow-Methods", "POST")
        return response, 400

    input_val = f"BOOK {start_time} {end_time} {capacity}"
    response = main(rooms_dict=rooms, input_val=input_val)
    if "VACANT" in response:
        response = jsonify({'rooms': [], 'message': 'Sorry! No Vacant Room available'})
        # response.headers.add("Access-Control-Allow-Origin", "*")
        # response.headers.add("Access-Control-Allow-Methods", "POST")
        return response, 400
    elif "INCORRECT" in response:
        # response = jsonify({'rooms': [], 'message': 'Error Occured. Please check the input'})
        # response.headers.add("Access-Control-Allow-Origin", "*")
        # response.headers.add("Access-Control-Allow-Methods", "POST")
        return response, 500
    else:
        booked_room = response
        response = jsonify({'rooms': [booked_room], 'message': f"You've booked {booked_room} room for {capacity} people"})
        # response.headers.add("Access-Control-Allow-Origin", "*")
        # response.headers.add("Access-Control-Allow-Methods", "POST")
        # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        return response, 200


if __name__ == '__main__':
    rooms = dict(cave=Cave(), tower=Tower(), mansion=Mansion())
    app.run(debug=True)
