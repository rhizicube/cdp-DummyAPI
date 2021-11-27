from flask import Flask, request, jsonify
from flask_cors import CORS
from pprint import pprint as pp
import os
import time

app = Flask(__name__)
cors = CORS(app, resources={"/*": {"origins": "*", "methods": ["GET", "POST"]},
                            "/*/*": {"origins": "*", "methods": ["GET", "POST"]}})


@app.route("/")
def index():
    return "<p>nc-cdp-backend (5002) Application Server Start...</p>"

#My code starts here 

@app.route("/get_ids_count_by_client", methods=["POST"])
def get_ids_count_by_client():
    response = {
        "status": "success"
        "code": 200
    }
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('client_id')
        if client_id == 100001:
            response["data"] = [
                {
                    "deterministic": 15255, 
                    "conflicting": 56434
                }
            ]
        else:
            response["status"] = "Error"
            response["status"] = 500
            response["message"] = "Wrong Client Id"
    except Exception as err:
        response["status"] = "Error"
        response["status"] = 500
        response["status"] = "Something Went Wrong"

    print('get_ids_count_by_client response', response)
    return response


@app.route("/get_users_by_segment", methods=["POST"])
def get_users_by_segment():
    response = {
        "status": "success"
        "code": 200
    }
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('client_id')
        block_relation = req_obj.get('block_relation')
        condition_relation = req_obj.get('condition_relation')
        condition = req_obj.get('condition')
        data_type = req_obj.get('data_type')
        name = req_obj.get('name')
        value = req_obj.get('value')

        if client_id == 100001:
            if block_relation.lower() == "or" or block_relation.lower() == "and":
                if condition_relation.lower() == "or" or condition_relation.lower() == "and":
                    if (condition.lower() in ["eq","gt", "lt", "startwith", "contains", "neq"]) and data_type.lower() == "string" and name.lower() =="ort_cross_street" and value.upper =="MOA":
                        response["data"] = [
                            {
                                "Uid": 15255, 
                                "attr1": "abc"
                                "attr2": "def"
                            }
                            {
                                "uid": 54654,
                                "attr1" : "value1"
                            }
                        ]
        else:
            response["status"] = "Error"
            response["status"] = 500
            response["message"] = "Wrong Client Id"
    except Exception as err:
        response["status"] = "Error"
        response["status"] = 500
        response["status"] = "Something Went Wrong"

    print('get_users_by_segment response', response)
    return response


@app.route("/get_user_attributes", methods=["POST"])
def get_user_attributes():
    response = {
        "status": "success"
        "code": 200
    }
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('client_id')
        user_id = req_obj.get('userid')
        if client_id == 100001 or user_id == 5432:
            response["data"] = [
                {
                    "cid": 100001, 
                    "uid": 5432, 
                    "profile_attrs": {
                        "name": "krishan", 
                        "age": "20"
                    }
                    "derived_attrs": {
                        "total_order_count": 100 
                        "total_order_value": 15780, 
                        "average_order_value": 157.80
                    }
                        
                }
            ]
        else:
            response["status"] = "Error"
            response["status"] = 500
            response["message"] = "Wrong Client Id or User ID"
    except Exception as err:
        response["status"] = "Error"
        response["status"] = 500
        response["status"] = "Something Went Wrong"

    print('get_ids_count_by_client response', response)
    return response


@app.route("/get_products_by_event", methods=["POST"])
def get_products_by_event():
    response = {
        "status": "success"
        "code": 200
    }
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('client_id')
        user_id = req_obj.get('userid')
        event_name = req.obj('event_name')
        order_by_date = req.obj('order_by_date')
        nrecs = req.obj('nrecs')
        if client_id == 100001 or user_id == 1:
            response["data"] = [
                {
                    "product_id" = "ab123"
                    "product_name" = "Stethoscope"
                    "product_desc" = "Health"
                    "image_url" = "www.image.com/abc1"
                    "event_date_time" = "19:09:34 26/11/2021 "
                }
                {
                    "product_id" = "dbvb154"
                    "product_name" = "Basketball"
                    "product_desc" = "Sports"
                    "image_url" = "www.image.com/dbb"
                    "event_date_time" = "12:03:24 12/01/2021 "
                }
            ]
        else:
            response["status"] = "Error"
            response["status"] = 500
            response["message"] = "Wrong Client Id or User ID"
    except Exception as err:
        response["status"] = "Error"
        response["status"] = 500
        response["status"] = "Something Went Wrong"

    print('get_products_by_event response', response)
    return response


@app.route("/get_user_count_by_client ", methods=["POST"])
def get_user_count_by_client ():
    response = {
        "status": "success"
        "code": 200
    }
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('client_id')
        if client_id == 100001:
            response["data"] = [
                {
                    "users" : 11000
                }
            ]
        else:
            response["status"] = "Error"
            response["status"] = 500
            response["message"] = "Wrong Client Id"
    except Exception as err:
        response["status"] = "Error"
        response["status"] = 500
        response["status"] = "Something Went Wrong"

    print('get_user_count_by_client response', response)
    return response


@app.route("/get_identifiers_by_user", methods=["POST"])
def get_identifiers_by_user():
    response = {
        "status": "success"
        "code": 200
    }
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('client_id')
        user_id = req_obj.get('userid')
        if client_id == 100001 or user_id == 559:
            response["data"] = [
                {
                    "deterministic": [
                        { 
                            "id": "udit@gmail.com", 
                            "type": "em" 
                        }, 
                        { 
                            "id": "9734747658", 
                            "type": "mo" 
                        }
                        ], 
                    "conflicting": [
                        {
                            "id": "9734747659", 
                             "type": "mo" 
                        }, 
                        { 
                            "id": "euf87347dsf87df", 
                            "type": "ck" 
                        }
                    ]
                }
            ]
        else:
            response["status"] = "Error"
            response["status"] = 500
            response["message"] = "Wrong Client Id or User ID"
    except Exception as err:
        response["status"] = "Error"
        response["status"] = 500
        response["status"] = "Something Went Wrong"

    print('get_identifiers_by_user response', response)
    return response


@app.route("/get_events_by_user", methods=["POST"])
def get_events_by_user():
    response = {
        "status": "success"
        "code": 200
    }
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('client_id')
        user_id = req_obj.get('userid')
        if client_id == 100001 or user_id == 5432:
            response["data"] = [
                {                    
                    "client_id" : 100002,
                    "users_id" : 5432,
                    "name" : "krishan"
                    "age" : "20"
                }
            ]
        else:
            response["status"] = "Error"
            response["status"] = 500
            response["message"] = "Wrong Client Id or User ID"
    except Exception as err:
        response["status"] = "Error"
        response["status"] = 500
        response["status"] = "Something Went Wrong"

    print('get_events_by_user response', response)
    return response


@app.route("/get_group_counts_by_user", methods=["POST"])
def get_group_counts_by_user():
    response = {
        "status": "success"
        "code": 200
    }
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('client_id')
        user_id = req_obj.get('userid')
        da_name = req_obj.get('da_name')
        if client_id == 100001 or user_id == 5432 or da_name == "total_order_value":
            response["data"] = [
                {                    
                    "client_id" : 100002,
                    "users_id" : 5432,
                    "values" : 11089,
                    "group_values" : {
                        "Basketball" : 110,
                        "Football" : 324,
                        "Volleyball" : 573,
                    }
                }
            ]
        else:
            response["status"] = "Error"
            response["status"] = 500
            response["message"] = "Wrong Client Id or User ID or da_name"
    except Exception as err:
        response["status"] = "Error"
        response["status"] = 500
        response["status"] = "Something Went Wrong"

    print('get_group_counts_by_user response', response)
    return response


@app.route("/get_best_day_time", methods=["POST"])
def get_best_day_time():
    response = {
        "status": "success"
        "code": 200
    }
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('client_id')
        user_id = req_obj.get('userid')
        if client_id == 100001 or user_id == 5432:
            response["data"] = [
                {                    
                    "client_id" : 100001,
                    "users_id" : 5432,
                    "day" : "Friday"
                    "time_Window" : "15:24:10 PM - 15:34:52 PM"
                }
            ]
        else:
            response["status"] = "Error"
            response["status"] = 500
            response["message"] = "Wrong Client Id or User ID"
    except Exception as err:
        response["status"] = "Error"
        response["status"] = 500
        response["status"] = "Something Went Wrong"

    print('get_best_day_time response', response)
    return response


#My code Ends here


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5002)
    app.run(debug=True, port=5002)
