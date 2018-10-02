from flask import Flask, Response
from line_service import LineService
from api_error import ApiError
from line_service_basic import LineServiceBasic
from out_of_range_exception import OutOfRangeException

app = Flask(__name__)
filepath = 'odyssey.txt'
line_service = LineService(filepath=filepath, cachesize=100000)
basic_line_service = LineServiceBasic(filepath=filepath)


@app.route('/lines', methods=['GET'])
def lines():
    result = ""
    for key, val in line_service.index.items():
        result += "Line %d: pos %d<br/>" % (key, val)

    return result


@app.route('/lines/<line_id>', methods=['GET'])
def line(line_id):
    try:
        return Response(line_service.get_line(int(line_id)), headers={'Content-Type': 'text/html'}, status=200)
    except OutOfRangeException as e:
        raise ApiError(e, status_code=413)


@app.route('/lines_basic', methods=['GET'])
def lines():
    result = ""
    for l in basic_line_service.get_lines():
        result += l + "<br/>"

    return result


@app.route('/lines_basic/<line_id>', methods=['GET'])
def line(line_id):
    try:
        return Response(basic_line_service.get_line(int(line_id)), headers={'Content-Type': 'text/html'}, status=200)
    except IndexError as e:
        raise ApiError(e, status_code=413)


@app.errorhandler(ApiError)
def handle_api_error(error):
    return Response(error.message, headers={'Content-Type': 'text/html'}, status=error.status_code)


