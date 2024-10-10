from flask import Blueprint, request, jsonify
from utils.dates_f import time_based_data
from services import accidents_service
import services.accidents_service as ser

accidents_bp = Blueprint('accidents', __name__)


def get_request_info():
    return {
        "ip": request.remote_addr,
        "endpoint": request.url,
        "method": request.method
    }


@accidents_bp.route('/test')
def test():
    return jsonify({'msg': 'It works!'})


@accidents_bp.route('/<int:beat_of_occurrence>', methods=['GET'])
def get_sum_of_accidents_by_beat_of_occurrence(beat_of_occurrence):
    request_info = get_request_info()
    num_accidents = ser.get_sum_of_accidents_by_beat_of_occurrence(beat_of_occurrence, request_info)
    return jsonify({'beat_of_occurrence': beat_of_occurrence, 'num_accidents': num_accidents})


@accidents_bp.route('/time/<string:unit>/<int:number>/<int:beat_of_occurrence>', methods=['GET'])
def get_sum_of_accidents_by_beat_end_date(unit, number, beat_of_occurrence):
    request_info = get_request_info()

    if unit not in time_based_data:
        return jsonify({"error": "Invalid time unit. Use 'day', 'week', or 'month'."}), 400

    num_accidents = ser.get_sum_of_accidents_by_beat_end_date(unit, number, beat_of_occurrence, request_info)
    return jsonify({'beat_of_occurrence': beat_of_occurrence, f'{unit}': number, 'num_accidents': num_accidents})


@accidents_bp.route('/contributory_cause/<int:beat_of_occurrence>', methods=['GET'])
def get_sum_of_contributory_cause_by_beat(beat_of_occurrence):
    request_info = get_request_info()
    num_accidents = ser.get_sum_of_contributory_cause_by_beat(beat_of_occurrence, request_info)
    return jsonify(num_accidents)


@accidents_bp.route('/injuries/<int:beat_of_occurrence>', methods=['GET'])
def get_injuries_by_beat(beat_of_occurrence):
    request_info = get_request_info()
    num_accidents = ser.get_injuries_by_beat(beat_of_occurrence, request_info)
    return jsonify(num_accidents)
