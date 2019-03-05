#!/usr/bin/python3
'''App_views routes'''
from api.v1.views import app_views
#from models import storage
from models import *
from flask import jsonify, abort, make_response, request
import json, math

def calcualteValues(values):
    a, b, c, d, x = int(values.get('a')), int(values.get('b')), int(values.get('c')), \
                    int(values.get('d')), int(values.get('x'))

    y1 = (a * (x * x)) + (b * x) + c
    y2 = d * math.sin(x)
    obj = {
            'a'  : a,
            'b'  : b,
            'c'  : c,
            'd'  : d,
            'x'  : x,
            'y1' : y1,
            'y2' : round(y2, 2),
            'y3' : round(y1/y2, 2)
    }
    return obj



def validateValues(values):
    letters = ('a', 'b', 'c', 'd', 'x')
    for x in letters:
        if not values.get(x) or values.get(x) == "0" or values.get(x) == 0:
            return False
    return True


@app_views.route('/standardc', methods=["GET", "POST"], strict_slashes=False)
def return_math():
    '''Build an API to take in the following values: a, b, c, d and x and returns:
    y1 = (a * x^2) + (b * x) + c
    y2 = (d * sin(x))
    y3 = y1/y2
        '''
    if request.method == "POST":    
        values = request.get_json()
        if not validateValues(values):
            abort(400, 'Not a JSON')

        values = calcualteValues(values)
        StandardC = classes.get("StandardC")
        new_obj = StandardC(**values)
        
        print("NEW OBJECTS", new_obj.__dict__)
        new_obj.save()
        return jsonify({"message":"Success"}), 201

    if request.method == "GET":
        values = request.args
        if not validateValues(values):
           return make_response(jsonify({'error': 'Input correct value to calculate whatever'}), 400) 

        obj = calcualteValues(values)
        return jsonify(obj)

@app_views.route("/standardc/<date1>/<date2>", methods=["GET"], strict_slashes=False)
def return_math_timeperiod():
    pass

@app_views.route("/standardc/<amount>", methods=["GET"], strict_slashes=False)
def return_math_amount(amount=None):
    all_objs = storage.get("StandardC", amount)
    if not all_objs:
        abort(404, "Not Found")

    return jsonify(all_objs.to_json())













