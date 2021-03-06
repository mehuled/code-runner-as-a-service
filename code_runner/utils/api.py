import json

from flask import Response


def response_data(data):
    response = {
        'data': data
    }

    return Response(response=json.dumps(response), status=200, content_type='application/json')


def error_response(status_code: int, error_message: str):
    response = {
        'error': error_message
    }
    return Response(response=json.dumps(response), status=status_code, content_type='application/json')


def request_data(body):
    body_dict = json.loads(body)
    return body_dict
