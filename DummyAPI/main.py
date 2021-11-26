from flask import Flask, request, jsonify
from flask_cors import CORS
from pprint import pprint as pp
import os
import time
from customer_list_data import CUSTOMER_LIST, CUSTOMER_LIST_KEYS
from layout_data import LAYOUT_ID_100, LAYOUT_ID_106, LAYOUT_ID_107, LAYOUT_ID_108, LAYOUT_ID_109

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

@app.route("/client_data", methods=["POST"])
def client_data():
    response = {
        "status": "success",
        "code": 200
    }
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('client_id')
        if client_id == "cl-1":
            response["data"] = [
                {
                    "layout_name": "Customers",
                    "layout_icon": "fa fa-fw fa-user",
                    "layout_id": "lay-1"
                },
                {
                    "layout_name": "Data Health",
                    "layout_icon": "fa fa-fw fa-heartbeat",
                    "layout_id": "layout_id_100"
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

    print('client_data response', response)
    return response


@app.route("/layout_data", methods=["POST"])
def layout_data():
    # time.sleep(5)
    try:
        req_obj = request.get_json()
        layout_id = req_obj.get('layout_id')
        layout_type = req_obj.get('layout_type')

        apiData = {}

        if layout_id == "layout_id_100" or layout_type == "health":
            apiData = LAYOUT_ID_100
        elif layout_id == "layout_id_106":
            apiData = LAYOUT_ID_106
        elif layout_id == "layout_id_107":
            apiData = LAYOUT_ID_107
        elif layout_id == "layout_id_108" or layout_type == "customer":
            apiData = LAYOUT_ID_108
        elif layout_id == "layout_id_109":
            apiData = LAYOUT_ID_109
        else:
            apiData = {
                "status": "Error",
                "message": "Something Went Wrong",
                "code": 500
            }

        print('layout_data response', apiData)
        return jsonify(apiData)
    except Exception as e:
        print(e)
        return jsonify({
            "status": "Error",
            "message": "Something Went Wrong",
            "code": 500
        })


@app.route("/metric_layout_data", methods=["POST"])
def metric_layout_data():
    try:
        req_obj = request.get_json()
        metric_layout_id = req_obj.get('metric_layout_id')
        metadata = req_obj.get('metadata')

        apiData = {}

        if metric_layout_id == "metric_layout_300":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_300",
                    "title": "Data Points Processed",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_400": {
                            "metric_id": "metric_id_400",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }

        elif metric_layout_id == "metric_layout_301":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_301",
                    "title": "Total Connections",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_401": {
                            "metric_id": "metric_id_401",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }

        elif metric_layout_id == "metric_layout_302":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_302",
                    "title": "Data ingestion metrics",
                    "metric_layout_icon_url": "",
                    "help_text": "Data ingestion metrics",
                    "description": "How is your ingested Data's health",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_402": {
                            "metric_id": "metric_id_402",
                            "metric_name": "",
                            "filter": [
                                {
                                    "filter_id": "filter_id_501",
                                    "filter_values": [
                                        "2016-01-01",
                                        "2022-01-01"
                                    ],
                                    "filter_label": "Date Range",
                                    "filter_type": "date_range",
                                    "selected_values": [
                                        "2017-01-01",
                                        "2019-01-01"
                                    ]
                                },
                                {
                                    "filter_id": "filter_id_503",
                                    "filter_values": [
                                        {"id": "Hourly", "name": "Hourly"},
                                        {"id": "Monthly", "name": "Monthly"},
                                        {"id": "Quaterly", "name": "Quaterly"},
                                        {"id": "Yearly", "name": "Yearly"}
                                    ],
                                    "filter_label": "Time Period",
                                    "filter_type": "dropdown_timeperiod",
                                    "selected_values": [
                                        {"id": "Quaterly", "name": "Quaterly"}
                                    ]
                                }
                            ],
                            "metadata": None
                        }
                    }
                }
            }

        elif metric_layout_id == "metric_layout_303":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_303",
                    "title": "Data exported metrics",
                    "metric_layout_icon_url": "",
                    "help_text": "Data exported metrics",
                    "description": "How is your exported Data's health",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_403": {
                            "metric_id": "metric_id_403",
                            "metric_name": "",
                            "filter": [
                                {
                                    "filter_id": "filter_id_502",
                                    "filter_values": [
                                        "2016-01-01",
                                        "2022-01-01"
                                    ],
                                    "filter_label": "Date Range",
                                    "filter_type": "date_range",
                                    "selected_values": [
                                        "2017-01-01",
                                        "2019-01-01"
                                    ]
                                },
                                {
                                    "filter_id": "filter_id_504",
                                    "filter_values": [
                                        {"id": "Hourly", "name": "Hourly"},
                                        {"id": "Monthly", "name": "Monthly"},
                                        {"id": "Quaterly", "name": "Quaterly"},
                                        {"id": "Yearly", "name": "Yearly"}
                                    ],
                                    "filter_label": "Time Period",
                                    "filter_type": "dropdown_timeperiod",
                                    "selected_values": [
                                        {"id": "Quaterly", "name": "Quaterly"}
                                    ]
                                }
                            ],
                            "metadata": None
                        }
                    }
                }
            }

        elif metric_layout_id == "metric_layout_304" and metadata["id"] == "103":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_304",
                    "title": "Android SDK",
                    "metric_layout_icon_url": "https://dummyimage.com/25x25/000/fff",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "components": None,
                    "metrics": {
                        "metric_id_404": {
                            "metric_id": "metric_id_404",
                            "metric_name": "",
                            "filter": [
                                {
                                    "filter_id": "filter_id_505",
                                    "filter_values": [
                                        {"id": "Hourly", "name": "Hourly"},
                                        {"id": "Monthly", "name": "Monthly"},
                                        {"id": "Quaterly", "name": "Quaterly"},
                                        {"id": "Yearly", "name": "Yearly"}
                                    ],
                                    "filter_label": "Time Period",
                                    "filter_type": "dropdown_timeperiod",
                                    "selected_values": [
                                        {"id": "Quaterly", "name": "Quaterly"}
                                    ]
                                },
                                {
                                    "filter_id": "filter_id_506",
                                    "filter_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ],
                                    "filter_label": "Select Events (upto 5)",
                                    "filter_type": "multi_dropdown",
                                    "max_select_limit" : 5,
                                    "selected_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ]
                                }
                            ],
                            "metadata": {
                                "connection_status": "operational",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Mobile App",
                                "custom_connection_name": "Android SDK",
                                "description": "Integrate SDK with your android app",
                                "display_image_url": "android.svg",
                                "id": "103",
                                "original_id": "metric_id_404",
                                "original_type": "metrics",
                                "type": "connector"
                            }
                        }
                    }
                }
            }

        elif metric_layout_id == "metric_layout_304" and metadata["id"] == "101":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_304",
                    "title": "Shopify",
                    "metric_layout_icon_url": "https://dummyimage.com/25x25/000/fff",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "components": None,
                    "metrics": {
                        "metric_id_404": {
                            "metric_id": "metric_id_404",
                            "metric_name": "",
                            "filter": [
                                {
                                    "filter_id": "filter_id_505",
                                    "filter_values": [
                                        {"id": "Hourly", "name": "Hourly"},
                                        {"id": "Monthly", "name": "Monthly"},
                                        {"id": "Quaterly", "name": "Quaterly"},
                                        {"id": "Yearly", "name": "Yearly"}
                                    ],
                                    "filter_label": "Time Period",
                                    "filter_type": "dropdown_timeperiod",
                                    "selected_values": [
                                        {"id": "Quaterly", "name": "Quaterly"}
                                    ]
                                },
                                {
                                    "filter_id": "filter_id_506",
                                    "filter_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ],
                                    "filter_label": "Select Events (upto 5)",
                                    "filter_type": "multi_dropdown",
                                    "max_select_limit" : 5,
                                    "selected_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ]
                                }
                            ],
                            "metadata": {
                                "connection_status": "operational",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "101",
                                "original_id": "metric_id_404",
                                "original_type": "metrics",
                                "type": "connector"
                            }
                        }
                    }
                }
            }

        elif metric_layout_id == "metric_layout_304" and metadata["id"] == "102":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_304",
                    "title": "Amazon S3",
                    "metric_layout_icon_url": "https://dummyimage.com/25x25/000/fff",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "components": {
                        "known_issues": True,
                        "known_issues_layout_id": "layout_id_107"
                    },
                    "metrics": {
                        "metric_id_404": {
                            "metric_id": "metric_id_404",
                            "metric_name": "",
                            "filter": [
                                {
                                    "filter_id": "filter_id_505",
                                    "filter_values": [
                                        {"id": "Hourly", "name": "Hourly"},
                                        {"id": "Monthly", "name": "Monthly"},
                                        {"id": "Quaterly", "name": "Quaterly"},
                                        {"id": "Yearly", "name": "Yearly"}
                                    ],
                                    "filter_label": "Time Period",
                                    "filter_type": "dropdown_timeperiod",
                                    "selected_values": [
                                        {"id": "Quaterly", "name": "Quaterly"}
                                    ]
                                },
                                {
                                    "filter_id": "filter_id_506",
                                    "filter_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ],
                                    "filter_label": "Select Events (upto 5)",
                                    "filter_type": "multi_dropdown",
                                    "max_select_limit" : 5,
                                    "selected_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ]
                                }
                            ],
                            "metadata": {
                                "connection_status": "operational",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "102",
                                "original_id": "metric_id_404",
                                "original_type": "metrics",
                                "type": "connector"
                            }
                        }
                    }
                }
            }

        elif metric_layout_id == "metric_layout_304" and metadata["id"] == "106":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_304",
                    "title": "Android SDK",
                    "metric_layout_icon_url": "https://dummyimage.com/25x25/000/fff",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "components": None,
                    "metrics": {
                        "metric_id_404": {
                            "metric_id": "metric_id_404",
                            "metric_name": "",
                            "filter": [
                                {
                                    "filter_id": "filter_id_505",
                                    "filter_values": [
                                        {"id": "Hourly", "name": "Hourly"},
                                        {"id": "Monthly", "name": "Monthly"},
                                        {"id": "Quaterly", "name": "Quaterly"},
                                        {"id": "Yearly", "name": "Yearly"}
                                    ],
                                    "filter_label": "Time Period",
                                    "filter_type": "dropdown_timeperiod",
                                    "selected_values": [
                                        {"id": "Quaterly", "name": "Quaterly"}
                                    ]
                                },
                                {
                                    "filter_id": "filter_id_506",
                                    "filter_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ],
                                    "filter_label": "Select Events (upto 5)",
                                    "filter_type": "multi_dropdown",
                                    "max_select_limit" : 5,
                                    "selected_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ]
                                }
                            ],
                            "metadata": {
                                "connection_status": "blocked",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Mobile App",
                                "custom_connection_name": "Android SDK",
                                "description": "Integrate SDK with your android app",
                                "display_image_url": "android.svg",
                                "id": "106",
                                "original_id": "metric_id_404",
                                "original_type": "metrics",
                                "type": "connector"
                            }
                        }
                    }
                }
            }

        elif metric_layout_id == "metric_layout_304" and metadata["id"] == "104":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_304",
                    "title": "Shopify",
                    "metric_layout_icon_url": "https://dummyimage.com/25x25/000/fff",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "components": None,
                    "metrics": {
                        "metric_id_404": {
                            "metric_id": "metric_id_404",
                            "metric_name": "",
                            "filter": [
                                {
                                    "filter_id": "filter_id_505",
                                    "filter_values": [
                                        {"id": "Hourly", "name": "Hourly"},
                                        {"id": "Monthly", "name": "Monthly"},
                                        {"id": "Quaterly", "name": "Quaterly"},
                                        {"id": "Yearly", "name": "Yearly"}
                                    ],
                                    "filter_label": "Time Period",
                                    "filter_type": "dropdown_timeperiod",
                                    "selected_values": [
                                        {"id": "Quaterly", "name": "Quaterly"}
                                    ]
                                },
                                {
                                    "filter_id": "filter_id_506",
                                    "filter_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ],
                                    "filter_label": "Select Events (upto 5)",
                                    "filter_type": "multi_dropdown",
                                    "max_select_limit" : 5,
                                    "selected_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ]
                                }
                            ],
                            "metadata": {
                                "connection_status": "blocked",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "104",
                                "original_id": "metric_id_404",
                                "original_type": "metrics",
                                "type": "connector"
                            }
                        }
                    }
                }
            }

        elif metric_layout_id == "metric_layout_304" and metadata["id"] == "105":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_304",
                    "title": "Amazon S3",
                    "metric_layout_icon_url": "https://dummyimage.com/25x25/000/fff",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "components": {
                        "known_issues": True,
                        "known_issues_layout_id": "layout_id_107"
                    },
                    "metrics": {
                        "metric_id_404": {
                            "metric_id": "metric_id_404",
                            "metric_name": "",
                            "filter": [
                                {
                                    "filter_id": "filter_id_505",
                                    "filter_values": [
                                        {"id": "Hourly", "name": "Hourly"},
                                        {"id": "Monthly", "name": "Monthly"},
                                        {"id": "Quaterly", "name": "Quaterly"},
                                        {"id": "Yearly", "name": "Yearly"}
                                    ],
                                    "filter_label": "Time Period",
                                    "filter_type": "dropdown_timeperiod",
                                    "selected_values": [
                                        {"id": "Quaterly", "name": "Quaterly"}
                                    ]
                                },
                                {
                                    "filter_id": "filter_id_506",
                                    "filter_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ],
                                    "filter_label": "Select Events (upto 5)",
                                    "filter_type": "multi_dropdown",
                                    "max_select_limit" : 5,
                                    "selected_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ]
                                }
                            ],
                            "metadata": {
                                "connection_status": "operational",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "105",
                                "original_id": "metric_id_404",
                                "original_type": "metrics",
                                "type": "connector"
                            }
                        }
                    }
                }
            }

        elif metric_layout_id == "metric_layout_304" and metadata["id"] == "107":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_304",
                    "title": "Shopify",
                    "metric_layout_icon_url": "https://dummyimage.com/25x25/000/fff",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "components": None,
                    "metrics": {
                        "metric_id_404": {
                            "metric_id": "metric_id_404",
                            "metric_name": "",
                            "filter": [
                                {
                                    "filter_id": "filter_id_505",
                                    "filter_values": [
                                        {"id": "Hourly", "name": "Hourly"},
                                        {"id": "Monthly", "name": "Monthly"},
                                        {"id": "Quaterly", "name": "Quaterly"},
                                        {"id": "Yearly", "name": "Yearly"}
                                    ],
                                    "filter_label": "Time Period",
                                    "filter_type": "dropdown_timeperiod",
                                    "selected_values": [
                                        {"id": "Quaterly", "name": "Quaterly"}
                                    ]
                                },
                                {
                                    "filter_id": "filter_id_506",
                                    "filter_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ],
                                    "filter_label": "Select Events (upto 5)",
                                    "filter_type": "multi_dropdown",
                                    "max_select_limit" : 5,
                                    "selected_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ]
                                }
                            ],
                            "metadata": {
                                "connection_status": "blocked",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "107",
                                "original_id": "metric_id_404",
                                "original_type": "metrics",
                                "type": "connector"
                            }
                        }
                    }
                }
            }

        elif metric_layout_id == "metric_layout_304" and metadata["id"] == "108":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_304",
                    "title": "Amazon S3",
                    "metric_layout_icon_url": "https://dummyimage.com/25x25/000/fff",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "components": {
                        "known_issues": True,
                        "known_issues_layout_id": "layout_id_107"
                    },
                    "metrics": {
                        "metric_id_404": {
                            "metric_id": "metric_id_404",
                            "metric_name": "",
                            "filter": [
                                {
                                    "filter_id": "filter_id_505",
                                    "filter_values": [
                                        {"id": "Hourly", "name": "Hourly"},
                                        {"id": "Monthly", "name": "Monthly"},
                                        {"id": "Quaterly", "name": "Quaterly"},
                                        {"id": "Yearly", "name": "Yearly"}
                                    ],
                                    "filter_label": "Time Period",
                                    "filter_type": "dropdown_timeperiod",
                                    "selected_values": [
                                        {"id": "Quaterly", "name": "Quaterly"}
                                    ]
                                },
                                {
                                    "filter_id": "filter_id_506",
                                    "filter_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ],
                                    "filter_label": "Select Events (upto 5)",
                                    "filter_type": "multi_dropdown",
                                    "max_select_limit" : 5,
                                    "selected_values": [
                                        {"id": "Account Created", "name": "Account Created"},
                                        {"id": "Abandon Cart", "name": "Abandon Cart"},
                                        {"id": "Profile Push", "name": "Profile Push"},
                                        {"id": "Complete Purchase", "name": "Complete Purchase"},
                                        {"id": "Browse", "name": "Browse"}
                                    ]
                                }
                            ],
                            "metadata": {
                                "connection_status": "blocked",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "108",
                                "original_id": "metric_id_404",
                                "original_type": "metrics",
                                "type": "connector"
                            }
                        }
                    }
                }
            }

        elif metric_layout_id == "metric_layout_305":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_305",
                    "title": "Known Issues",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "This connector's issue known to us",
                    "is_multi_tab": False,
                    "type": "information",
                    "on_action": "",
                    "components": None,
                    "metrics": {
                        "metric_id_405": {
                            "metric_id": "metric_id_405",
                            "metric_name": "",
                            "filter": None,
                            "metadata": {
                                "connection_status": "operational",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "102",
                                "original_id": "metric_id_405",
                                "original_type": "metrics",
                                "type": "connector"
                            }
                        }
                    }
                }
            }

        elif metric_layout_id == "metric_layout_306":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_306",
                    "title": "Error Logs",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "table",
                    "on_action": "",
                    "components": None,
                    "metrics": {
                        "metric_id_406": {
                            "metric_id": "metric_id_406",
                            "metric_name": "",
                            "filter": None,
                            "metadata": {
                                "connection_status": "operational",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "102",
                                "original_id": "metric_id_406",
                                "original_type": "metrics",
                                "type": "connector"
                            }
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_307":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_307",
                    "title": "Total customers identified",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "click",
                    "on_action_id": "metric_layout_311",
                    "components": None,
                    "metrics": {
                        "metric_id_407": {
                            "metric_id": "metric_id_407",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_308":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_308",
                    "title": "No. of IDs stitched",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "click",
                    "on_action_id": "metric_layout_312",
                    "components": None,
                    "metrics": {
                        "metric_id_408": {
                            "metric_id": "metric_id_408",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_309":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_309",
                    "title": "Data points processed",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "click",
                    "on_action_id": "metric_layout_313",
                    "components": None,
                    "metrics": {
                        "metric_id_409": {
                            "metric_id": "metric_id_409",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_310":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_310",
                    "title": "Reachable customers per channel",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "click",
                    "on_action_id": "metric_layout_314",
                    "components": None,
                    "metrics": {
                        "metric_id_410": {
                            "metric_id": "metric_id_410",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_311":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_311",
                    "title": "Total customers identified",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_411": {
                            "metric_id": "metric_id_411",
                            "metric_name": "",
                            "filter": [
                                {
                                    "filter_id": "filter_id_513",
                                    "filter_values": [
                                        "2016-01-01",
                                        "2022-01-01"
                                    ],
                                    "filter_label": "Date Range",
                                    "filter_type": "date_range",
                                    "selected_values": [
                                        "2017-01-01",
                                        "2019-01-01"
                                    ]
                                },
                                {
                                    "filter_id": "filter_id_514",
                                    "filter_values": [
                                        {"id": "Hourly", "name": "Hourly"},
                                        {"id": "Monthly", "name": "Monthly"},
                                        {"id": "Quaterly", "name": "Quaterly"},
                                        {"id": "Yearly", "name": "Yearly"}
                                    ],
                                    "filter_label": "Time Period",
                                    "filter_type": "dropdown_timeperiod",
                                    "selected_values": [
                                        {"id": "Quaterly", "name": "Quaterly"}
                                    ]
                                }
                            ],
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_312":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_312",
                    "title": "Number of IDs stitched",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_412": {
                            "metric_id": "metric_id_412",
                            "metric_name": "",
                            "filter": [
                                {
                                    "filter_id": "filter_id_515",
                                    "filter_values": [
                                        "2016-01-01",
                                        "2022-01-01"
                                    ],
                                    "filter_label": "Date Range",
                                    "filter_type": "date_range",
                                    "selected_values": [
                                        "2017-01-01",
                                        "2019-01-01"
                                    ]
                                },
                                {
                                    "filter_id": "filter_id_516",
                                    "filter_values": [
                                        {"id": "Hourly", "name": "Hourly"},
                                        {"id": "Monthly", "name": "Monthly"},
                                        {"id": "Quaterly", "name": "Quaterly"},
                                        {"id": "Yearly", "name": "Yearly"}
                                    ],
                                    "filter_label": "Time Period",
                                    "filter_type": "dropdown_timeperiod",
                                    "selected_values": [
                                        {"id": "Quaterly", "name": "Quaterly"}
                                    ]
                                }
                            ],
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_313":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_313",
                    "title": "Data points processed",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_413": {
                            "metric_id": "metric_id_413",
                            "metric_name": "",
                            "filter": [
                                {
                                    "filter_id": "filter_id_517",
                                    "filter_values": [
                                        "2016-01-01",
                                        "2022-01-01"
                                    ],
                                    "filter_label": "Date Range",
                                    "filter_type": "date_range",
                                    "selected_values": [
                                        "2017-01-01",
                                        "2019-01-01"
                                    ]
                                },
                                {
                                    "filter_id": "filter_id_518",
                                    "filter_values": [
                                        {"id": "Hourly", "name": "Hourly"},
                                        {"id": "Monthly", "name": "Monthly"},
                                        {"id": "Quaterly", "name": "Quaterly"},
                                        {"id": "Yearly", "name": "Yearly"}
                                    ],
                                    "filter_label": "Time Period",
                                    "filter_type": "dropdown_timeperiod",
                                    "selected_values": [
                                        {"id": "Quaterly", "name": "Quaterly"}
                                    ]
                                }
                            ],
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_314":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_314",
                    "title": "Customers per channel",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_414": {
                            "metric_id": "metric_id_414",
                            "metric_name": "",
                            "filter": [
                                {
                                    "filter_id": "filter_id_519",
                                    "filter_values": [
                                        "2016-01-01",
                                        "2022-01-01"
                                    ],
                                    "filter_label": "Date Range",
                                    "filter_type": "date_range",
                                    "selected_values": [
                                        "2017-01-01",
                                        "2019-01-01"
                                    ]
                                },
                                {
                                    "filter_id": "filter_id_520",
                                    "filter_values": [
                                        {"id": "Hourly", "name": "Hourly"},
                                        {"id": "Monthly", "name": "Monthly"},
                                        {"id": "Quaterly", "name": "Quaterly"},
                                        {"id": "Yearly", "name": "Yearly"}
                                    ],
                                    "filter_label": "Time Period",
                                    "filter_type": "dropdown_timeperiod",
                                    "selected_values": [
                                        {"id": "Quaterly", "name": "Quaterly"}
                                    ]
                                }
                            ],
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_315":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_315",
                    "title": "",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "table",
                    "on_action": "",
                    "components": None,
                    "metrics": {
                        "metric_id_415": {
                            "metric_id": "metric_id_415",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_316":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_316",
                    "title": "Customer lifetime value",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_416": {
                            "metric_id": "metric_id_416",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_317":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_317",
                    "title": "Total orders",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_417": {
                            "metric_id": "metric_id_417",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_318":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_318",
                    "title": "Total revenue",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_418": {
                            "metric_id": "metric_id_418",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_319":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_319",
                    "title": "Average order value",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_419": {
                            "metric_id": "metric_id_419",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_320":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_320",
                    "title": "Overall likelihood to engage",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_420": {
                            "metric_id": "metric_id_420",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_321":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_321",
                    "title": "Preffered channel",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics":{
                        "metric_id_421": {
                            "metric_id": "metric_id_421",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                        }
                    }
                }
        elif metric_layout_id == "metric_layout_322":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_322",
                    "title": "Customer lifetime value",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_422": {
                            "metric_id": "metric_id_422",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_323":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_323",
                    "title": "Total orders",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "",
                    "on_action_id": "",
                    "components": None,
                    "metrics": {
                        "metric_id_423": {
                            "metric_id": "metric_id_423",
                            "metric_name": "",
                            "filter":None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_324":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_324",
                    "title": "Total revenue",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "",
                    "components": None,
                    "metrics": {
                        "metric_id_424": {
                            "metric_id": "metric_id_424",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_325":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_325",
                    "title": "Average order value",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "card",
                    "on_action": "",
                    "components": None,
                    "metrics": {
                        "metric_id_425": {
                            "metric_id": "metric_id_425",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_326":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_326",
                    "title": "Category preference",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "",
                    "components": None,
                    "metrics": {
                        "metric_id_426": {
                            "metric_id": "metric_id_426",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_327":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_327",
                    "title": "Product preference",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "non-timeseries",
                    "on_action": "",
                    "components": None,
                    "metrics": {
                        "metric_id_427": {
                            "metric_id": "metric_id_427",
                            "metric_name": "",
                            "filter": None,
                            "metadata": None
                        }
                    }
                }
            }
        elif metric_layout_id == "metric_layout_328":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_328",
                    "title": "Revenue trends",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "components": None,
                    "metrics": {
                        "metric_id_428": {
                            "metric_id": "metric_id_428",
                            "metric_name": "Overall",
                            "filter": None,
                            "metadata": None
                        },
                        "metric_id_429": {
                            "metric_id": "metric_id_429",
                            "metric_name": "Category wise",
                            "filter": None,
                            "metadata": None
                        },
                        "metric_id_430": {
                            "metric_id": "metric_id_430",
                            "metric_name": "Product wise",
                            "filter": None,
                            "metadata": None
                        },
                        "metric_id_431": {
                            "metric_id": "metric_id_431",
                            "metric_name": "Across channel",
                            "filter": None,
                            "metadata": None
                        },
                        "metric_id_432": {
                            "metric_id": "metric_id_432",
                            "metric_name": "Across order type",
                            "filter": None,
                            "metadata": None
                        }

                    }
                }
            }
        elif metric_layout_id == "metric_layout_329":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "metric_layout_329",
                    "title": "Transaction split",
                    "metric_layout_icon_url": "",
                    "help_text": "",
                    "description": "",
                    "is_multi_tab": False,
                    "type": "timeseries",
                    "on_action": "",
                    "components": None,
                    "metrics": {
                        "metric_id_433": {
                            "metric_id": "metric_id_433",
                            "metric_name": "Category wise",
                            "filter": None,
                            "metadata": None
                        },
                        "metric_id_434": {
                            "metric_id": "metric_id_434",
                            "metric_name": "Product wise",
                            "filter": None,
                            "metadata": None
                        },
                        
                    }
                }
            }
        else:
            apiData = {
                "status": "Error",
                "message": "Something Went Wrong",
                "code": 500
            }

        print('metric_layout_data response', apiData)
        return jsonify(apiData)
    except Exception as e:
        print(e)
        return jsonify({
            "status": "Error",
            "message": "Something Went Wrong",
            "code": 500
        })


@app.route("/metric_data", methods=["POST"])
def metric_data():
    time.sleep(5)
    try:
        req_obj = request.get_json()
        metric_id = req_obj.get('metric_id')
        metadata = req_obj.get('metadata')

        apiData = {}

        if metric_id == "metric_id_400":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_400",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "Ingested",
                            "value": "69557"
                        },
                        {
                            "key": "Exported",
                            "value": "66496"
                        }
                    ]
                }
            }

        elif metric_id == "metric_id_401":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_401",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "Ingested",
                            "value": "69557"
                        },
                        {
                            "key": "Exported",
                            "value": "66496"
                        }
                    ]
                }
            }

        elif metric_id == "metric_id_402":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_402",
                    "metric_type": "line",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "count",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_505",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        {
                            "filter_id": "filter_id_506",
                            "values": "Profile Push, Account Created, Abandon Cart, Profile Push, Complete Purchase, Browse",
                            "filter_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ],
                            "filter_label": "Select Events (upto 5)",
                            "filter_type": "multi_dropdown",
                            "max_select_limit" : 5,
                            "selected_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ]
                        }
                    ],
                    "metric_data": [
                        {
                            "color": "blue",
                            "name": "In Record",
                            "data": [
                                110,
                                175,
                                151,
                                129,
                                190,
                                60,
                                52,
                                129,
                                241,
                                203,
                                120,
                                180,
                                183,
                                84,
                                194,
                                39
                            ]
                        },
                        {
                            "color": "green",
                            "name": "Out Record",
                            "data": [
                                93,
                                164,
                                145,
                                129,
                                186,
                                51,
                                50,
                                112,
                                229,
                                184,
                                116,
                                173,
                                182,
                                81,
                                182,
                                25
                            ]
                        }
                    ],
                    "axis_data": [
                        "2021-06-28T21:00:00+08:00",
                        "2021-03-28T01:00:00+08:00",
                        "2021-04-09T21:00:00+08:00",
                        "2021-03-01T10:00:00+08:00",
                        "2021-03-27T04:00:00+08:00",
                        "2021-03-27T13:00:00+08:00",
                        "2021-05-20T09:00:00+08:00",
                        "2021-06-10T14:00:00+08:00",
                        "2021-06-15T19:00:00+08:00",
                        "2021-05-05T01:00:00+08:00",
                        "2021-03-11T07:00:00+08:00",
                        "2021-03-31T01:00:00+08:00",
                        "2021-04-10T13:00:00+08:00",
                        "2021-06-12T10:00:00+08:00",
                        "2021-06-22T23:00:00+08:00",
                        "2021-04-08T15:00:00+08:00"
                    ]
                }
            }

        elif metric_id == "metric_id_403":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_403",
                    "metric_type": "bar",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "count",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_505",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        {
                            "filter_id": "filter_id_506",
                            "values": "Profile Push, Account Created, Abandon Cart, Profile Push, Complete Purchase, Browse",
                            "filter_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ],
                            "filter_label": "Select Events (upto 5)",
                            "filter_type": "multi_dropdown",
                            "max_select_limit" : 5,
                            "selected_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ]
                        }
                    ],
                    "metric_data": [
                        {
                            "name": "Account Created",
                            "data": [
                                1782,
                                200,
                                2785,
                                964,
                                403,
                                831,
                                227,
                                1709,
                                56,
                                2715,
                                140,
                                82,
                                1611,
                                356,
                                311,
                                529,
                                1049,
                                1685,
                                392,
                                1551,
                                296,
                                2214,
                                129,
                                3059
                            ],
                            "color": "#030bfc"
                        }
                    ],
                    "axis_data": [
                        "2021-06-30T00:00:00+08:000",
                        "2021-06-30T01:00:00+08:00",
                        "2021-06-30T02:00:00+08:00",
                        "2021-06-30T03:00:00+08:00",
                        "2021-06-30T04:00:00+08:00",
                        "2021-06-30T05:00:00+08:00",
                        "2021-06-30T06:00:00+08:00",
                        "2021-06-30T07:00:00+08:00",
                        "2021-06-30T08:00:00+08:00",
                        "2021-06-30T09:00:00+08:00",
                        "2021-06-30T10:00:00+08:00",
                        "2021-06-30T11:00:00+08:00",
                        "2021-06-30T12:00:00+08:00",
                        "2021-06-30T13:00:00+08:00",
                        "2021-06-30T14:00:00+08:00",
                        "2021-06-30T15:00:00+08:00",
                        "2021-06-30T16:00:00+08:00",
                        "2021-06-30T17:00:00+08:00",
                        "2021-06-30T18:00:00+08:00",
                        "2021-06-30T19:00:00+08:00",
                        "2021-06-30T20:00:00+08:00",
                        "2021-06-30T21:00:00+08:00",
                        "2021-06-30T22:00:00+08:00",
                        "2021-06-30T23:00:00+08:00"
                    ]
                }
            }

        elif metric_id == "metric_id_404" and metadata["id"] == "101":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_404",
                    "metric_type": "line",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "count",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_505",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        {
                            "filter_id": "filter_id_506",
                            "values": "Profile Push, Account Created, Abandon Cart, Profile Push, Complete Purchase, Browse",
                            "filter_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ],
                            "filter_label": "Select Events (upto 5)",
                            "filter_type": "multi_dropdown",
                            "max_select_limit" : 5,
                            "selected_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ]
                        }
                    ],
                    "metric_data": [
                        {
                            "name": "Account Created",
                            "data": [
                                1782,
                                200,
                                2785,
                                964,
                                403,
                                831,
                                227,
                                1709,
                                56,
                                2715,
                                140,
                                82,
                                1611,
                                356,
                                311,
                                529,
                                1049,
                                1685,
                                392,
                                1551,
                                296,
                                2214,
                                129,
                                3059
                            ],
                            "color": "#030bfc"
                        },
                        {
                            "name": "Browse",
                            "data": [
                                280,
                                906,
                                246,
                                1650,
                                1647,
                                268,
                                417,
                                250,
                                1928,
                                288,
                                274,
                                189,
                                439,
                                1560,
                                794,
                                231,
                                281,
                                994,
                                508,
                                1888,
                                2545,
                                741,
                                2109,
                                895
                            ],
                            "color": "#e303fc"
                        },
                        {
                            "name": "Complete Purchase",
                            "data": [
                                1324,
                                671,
                                144,
                                373,
                                769,
                                1791,
                                106,
                                145,
                                468,
                                489,
                                943,
                                119,
                                1161,
                                66,
                                195,
                                1136,
                                199,
                                2244,
                                78,
                                481,
                                158,
                                767,
                                2127,
                                545
                            ],
                            "color": "#fc032d"
                        },
                        {
                            "name": "Abandon Cart",
                            "data": [
                                684,
                                78,
                                1984,
                                131,
                                214,
                                1117,
                                738,
                                172,
                                82,
                                1448,
                                211,
                                100,
                                2043,
                                927,
                                210,
                                1306,
                                206,
                                92,
                                1354,
                                237,
                                130,
                                123,
                                234,
                                345
                            ],
                            "color": "#52fc03"
                        },
                        {
                            "name": "Profile Push",
                            "data": [
                                198,
                                167,
                                1079,
                                1937,
                                999,
                                178,
                                253,
                                1040,
                                257,
                                1088,
                                500,
                                1722,
                                400,
                                2993,
                                673,
                                58,
                                992,
                                413,
                                53,
                                1467,
                                202,
                                1517,
                                147,
                                1722
                            ],
                            "color": "#fca103"
                        }
                    ],
                    "axis_data": [
                        "2021-06-30T00:00:00+08:000",
                        "2021-06-30T01:00:00+08:00",
                        "2021-06-30T02:00:00+08:00",
                        "2021-06-30T03:00:00+08:00",
                        "2021-06-30T04:00:00+08:00",
                        "2021-06-30T05:00:00+08:00",
                        "2021-06-30T06:00:00+08:00",
                        "2021-06-30T07:00:00+08:00",
                        "2021-06-30T08:00:00+08:00",
                        "2021-06-30T09:00:00+08:00",
                        "2021-06-30T10:00:00+08:00",
                        "2021-06-30T11:00:00+08:00",
                        "2021-06-30T12:00:00+08:00",
                        "2021-06-30T13:00:00+08:00",
                        "2021-06-30T14:00:00+08:00",
                        "2021-06-30T15:00:00+08:00",
                        "2021-06-30T16:00:00+08:00",
                        "2021-06-30T17:00:00+08:00",
                        "2021-06-30T18:00:00+08:00",
                        "2021-06-30T19:00:00+08:00",
                        "2021-06-30T20:00:00+08:00",
                        "2021-06-30T21:00:00+08:00",
                        "2021-06-30T22:00:00+08:00",
                        "2021-06-30T23:00:00+08:00"
                    ]
                }
            }

        elif metric_id == "metric_id_404" and metadata["id"] == "102":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_404",
                    "metric_type": "line",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "count",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_505",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        {
                            "filter_id": "filter_id_506",
                            "values": "Profile Push, Account Created, Abandon Cart, Profile Push, Complete Purchase, Browse",
                            "filter_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ],
                            "filter_label": "Select Events (upto 5)",
                            "filter_type": "multi_dropdown",
                            "max_select_limit" : 5,
                            "selected_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ]
                        }
                    ],
                    "metric_data": [
                        {
                            "name": "Account Created",
                            "data": [
                                1782,
                                200,
                                2785,
                                964,
                                403,
                                831,
                                227,
                                1709,
                                56,
                                2715,
                                140,
                                82,
                                1611,
                                356,
                                311,
                                529,
                                1049,
                                1685,
                                392,
                                1551,
                                296,
                                2214,
                                129,
                                3059
                            ],
                            "color": "#030bfc"
                        },
                        {
                            "name": "Browse",
                            "data": [
                                280,
                                906,
                                246,
                                1650,
                                1647,
                                268,
                                417,
                                250,
                                1928,
                                288,
                                274,
                                189,
                                439,
                                1560,
                                794,
                                231,
                                281,
                                994,
                                508,
                                1888,
                                2545,
                                741,
                                2109,
                                895
                            ],
                            "color": "#e303fc"
                        },
                        {
                            "name": "Complete Purchase",
                            "data": [
                                1324,
                                671,
                                144,
                                373,
                                769,
                                1791,
                                106,
                                145,
                                468,
                                489,
                                943,
                                119,
                                1161,
                                66,
                                195,
                                1136,
                                199,
                                2244,
                                78,
                                481,
                                158,
                                767,
                                2127,
                                545
                            ],
                            "color": "#fc032d"
                        },
                        {
                            "name": "Abandon Cart",
                            "data": [
                                684,
                                78,
                                1984,
                                131,
                                214,
                                1117,
                                738,
                                172,
                                82,
                                1448,
                                211,
                                100,
                                2043,
                                927,
                                210,
                                1306,
                                206,
                                92,
                                1354,
                                237,
                                130,
                                123,
                                234,
                                345
                            ],
                            "color": "#52fc03"
                        },
                        {
                            "name": "Profile Push",
                            "data": [
                                198,
                                167,
                                1079,
                                1937,
                                999,
                                178,
                                253,
                                1040,
                                257,
                                1088,
                                500,
                                1722,
                                400,
                                2993,
                                673,
                                58,
                                992,
                                413,
                                53,
                                1467,
                                202,
                                1517,
                                147,
                                1722
                            ],
                            "color": "#fca103"
                        }
                    ],
                    "axis_data": [
                        "2021-06-30T00:00:00+08:000",
                        "2021-06-30T01:00:00+08:00",
                        "2021-06-30T02:00:00+08:00",
                        "2021-06-30T03:00:00+08:00",
                        "2021-06-30T04:00:00+08:00",
                        "2021-06-30T05:00:00+08:00",
                        "2021-06-30T06:00:00+08:00",
                        "2021-06-30T07:00:00+08:00",
                        "2021-06-30T08:00:00+08:00",
                        "2021-06-30T09:00:00+08:00",
                        "2021-06-30T10:00:00+08:00",
                        "2021-06-30T11:00:00+08:00",
                        "2021-06-30T12:00:00+08:00",
                        "2021-06-30T13:00:00+08:00",
                        "2021-06-30T14:00:00+08:00",
                        "2021-06-30T15:00:00+08:00",
                        "2021-06-30T16:00:00+08:00",
                        "2021-06-30T17:00:00+08:00",
                        "2021-06-30T18:00:00+08:00",
                        "2021-06-30T19:00:00+08:00",
                        "2021-06-30T20:00:00+08:00",
                        "2021-06-30T21:00:00+08:00",
                        "2021-06-30T22:00:00+08:00",
                        "2021-06-30T23:00:00+08:00"
                    ]
                }
            }

        elif metric_id == "metric_id_404" and metadata["id"] == "103":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_404",
                    "metric_type": "line",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "count",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_505",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        {
                            "filter_id": "filter_id_506",
                            "values": "Profile Push, Account Created, Abandon Cart, Profile Push, Complete Purchase, Browse",
                            "filter_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ],
                            "filter_label": "Select Events (upto 5)",
                            "filter_type": "multi_dropdown",
                            "max_select_limit" : 5,
                            "selected_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ]
                        }
                    ],
                    "metric_data": [
                        {
                            "name": "Account Created",
                            "data": [
                                1782,
                                200,
                                2785,
                                964,
                                403,
                                831,
                                227,
                                1709,
                                56,
                                2715,
                                140,
                                82,
                                1611,
                                356,
                                311,
                                529,
                                1049,
                                1685,
                                392,
                                1551,
                                296,
                                2214,
                                129,
                                3059
                            ],
                            "color": "#030bfc"
                        },
                        {
                            "name": "Browse",
                            "data": [
                                280,
                                906,
                                246,
                                1650,
                                1647,
                                268,
                                417,
                                250,
                                1928,
                                288,
                                274,
                                189,
                                439,
                                1560,
                                794,
                                231,
                                281,
                                994,
                                508,
                                1888,
                                2545,
                                741,
                                2109,
                                895
                            ],
                            "color": "#e303fc"
                        },
                        {
                            "name": "Complete Purchase",
                            "data": [
                                1324,
                                671,
                                144,
                                373,
                                769,
                                1791,
                                106,
                                145,
                                468,
                                489,
                                943,
                                119,
                                1161,
                                66,
                                195,
                                1136,
                                199,
                                2244,
                                78,
                                481,
                                158,
                                767,
                                2127,
                                545
                            ],
                            "color": "#fc032d"
                        },
                        {
                            "name": "Abandon Cart",
                            "data": [
                                684,
                                78,
                                1984,
                                131,
                                214,
                                1117,
                                738,
                                172,
                                82,
                                1448,
                                211,
                                100,
                                2043,
                                927,
                                210,
                                1306,
                                206,
                                92,
                                1354,
                                237,
                                130,
                                123,
                                234,
                                345
                            ],
                            "color": "#52fc03"
                        },
                        {
                            "name": "Profile Push",
                            "data": [
                                198,
                                167,
                                1079,
                                1937,
                                999,
                                178,
                                253,
                                1040,
                                257,
                                1088,
                                500,
                                1722,
                                400,
                                2993,
                                673,
                                58,
                                992,
                                413,
                                53,
                                1467,
                                202,
                                1517,
                                147,
                                1722
                            ],
                            "color": "#fca103"
                        }
                    ],
                    "axis_data": [
                        "2021-06-30T00:00:00+08:000",
                        "2021-06-30T01:00:00+08:00",
                        "2021-06-30T02:00:00+08:00",
                        "2021-06-30T03:00:00+08:00",
                        "2021-06-30T04:00:00+08:00",
                        "2021-06-30T05:00:00+08:00",
                        "2021-06-30T06:00:00+08:00",
                        "2021-06-30T07:00:00+08:00",
                        "2021-06-30T08:00:00+08:00",
                        "2021-06-30T09:00:00+08:00",
                        "2021-06-30T10:00:00+08:00",
                        "2021-06-30T11:00:00+08:00",
                        "2021-06-30T12:00:00+08:00",
                        "2021-06-30T13:00:00+08:00",
                        "2021-06-30T14:00:00+08:00",
                        "2021-06-30T15:00:00+08:00",
                        "2021-06-30T16:00:00+08:00",
                        "2021-06-30T17:00:00+08:00",
                        "2021-06-30T18:00:00+08:00",
                        "2021-06-30T19:00:00+08:00",
                        "2021-06-30T20:00:00+08:00",
                        "2021-06-30T21:00:00+08:00",
                        "2021-06-30T22:00:00+08:00",
                        "2021-06-30T23:00:00+08:00"
                    ]
                }
            }

        elif metric_id == "metric_id_404" and metadata["id"] == "104":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_404",
                    "metric_type": "line",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "count",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_505",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        {
                            "filter_id": "filter_id_506",
                            "values": "Profile Push, Account Created, Abandon Cart, Profile Push, Complete Purchase, Browse",
                            "filter_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ],
                            "filter_label": "Select Events (upto 5)",
                            "filter_type": "multi_dropdown",
                            "max_select_limit" : 5,
                            "selected_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ]
                        }
                    ],
                    "metric_data": [
                        {
                            "name": "Account Created",
                            "data": [
                                1782,
                                200,
                                2785,
                                964,
                                403,
                                831,
                                227,
                                1709,
                                56,
                                2715,
                                140,
                                82,
                                1611,
                                356,
                                311,
                                529,
                                1049,
                                1685,
                                392,
                                1551,
                                296,
                                2214,
                                129,
                                3059
                            ],
                            "color": "#030bfc"
                        },
                        {
                            "name": "Browse",
                            "data": [
                                280,
                                906,
                                246,
                                1650,
                                1647,
                                268,
                                417,
                                250,
                                1928,
                                288,
                                274,
                                189,
                                439,
                                1560,
                                794,
                                231,
                                281,
                                994,
                                508,
                                1888,
                                2545,
                                741,
                                2109,
                                895
                            ],
                            "color": "#e303fc"
                        },
                        {
                            "name": "Complete Purchase",
                            "data": [
                                1324,
                                671,
                                144,
                                373,
                                769,
                                1791,
                                106,
                                145,
                                468,
                                489,
                                943,
                                119,
                                1161,
                                66,
                                195,
                                1136,
                                199,
                                2244,
                                78,
                                481,
                                158,
                                767,
                                2127,
                                545
                            ],
                            "color": "#fc032d"
                        },
                        {
                            "name": "Abandon Cart",
                            "data": [
                                684,
                                78,
                                1984,
                                131,
                                214,
                                1117,
                                738,
                                172,
                                82,
                                1448,
                                211,
                                100,
                                2043,
                                927,
                                210,
                                1306,
                                206,
                                92,
                                1354,
                                237,
                                130,
                                123,
                                234,
                                345
                            ],
                            "color": "#52fc03"
                        },
                        {
                            "name": "Profile Push",
                            "data": [
                                198,
                                167,
                                1079,
                                1937,
                                999,
                                178,
                                253,
                                1040,
                                257,
                                1088,
                                500,
                                1722,
                                400,
                                2993,
                                673,
                                58,
                                992,
                                413,
                                53,
                                1467,
                                202,
                                1517,
                                147,
                                1722
                            ],
                            "color": "#fca103"
                        }
                    ],
                    "axis_data": [
                        "2021-06-30T00:00:00+08:000",
                        "2021-06-30T01:00:00+08:00",
                        "2021-06-30T02:00:00+08:00",
                        "2021-06-30T03:00:00+08:00",
                        "2021-06-30T04:00:00+08:00",
                        "2021-06-30T05:00:00+08:00",
                        "2021-06-30T06:00:00+08:00",
                        "2021-06-30T07:00:00+08:00",
                        "2021-06-30T08:00:00+08:00",
                        "2021-06-30T09:00:00+08:00",
                        "2021-06-30T10:00:00+08:00",
                        "2021-06-30T11:00:00+08:00",
                        "2021-06-30T12:00:00+08:00",
                        "2021-06-30T13:00:00+08:00",
                        "2021-06-30T14:00:00+08:00",
                        "2021-06-30T15:00:00+08:00",
                        "2021-06-30T16:00:00+08:00",
                        "2021-06-30T17:00:00+08:00",
                        "2021-06-30T18:00:00+08:00",
                        "2021-06-30T19:00:00+08:00",
                        "2021-06-30T20:00:00+08:00",
                        "2021-06-30T21:00:00+08:00",
                        "2021-06-30T22:00:00+08:00",
                        "2021-06-30T23:00:00+08:00"
                    ]
                }
            }

        elif metric_id == "metric_id_404" and metadata["id"] == "105":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_404",
                    "metric_type": "line",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "count",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_505",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        {
                            "filter_id": "filter_id_506",
                            "values": "Profile Push, Account Created, Abandon Cart, Profile Push, Complete Purchase, Browse",
                            "filter_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ],
                            "filter_label": "Select Events (upto 5)",
                            "filter_type": "multi_dropdown",
                            "max_select_limit" : 5,
                            "selected_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ]
                        }
                    ],
                    "metric_data": [
                        {
                            "name": "Account Created",
                            "data": [
                                1782,
                                200,
                                2785,
                                964,
                                403,
                                831,
                                227,
                                1709,
                                56,
                                2715,
                                140,
                                82,
                                1611,
                                356,
                                311,
                                529,
                                1049,
                                1685,
                                392,
                                1551,
                                296,
                                2214,
                                129,
                                3059
                            ],
                            "color": "#030bfc"
                        },
                        {
                            "name": "Browse",
                            "data": [
                                280,
                                906,
                                246,
                                1650,
                                1647,
                                268,
                                417,
                                250,
                                1928,
                                288,
                                274,
                                189,
                                439,
                                1560,
                                794,
                                231,
                                281,
                                994,
                                508,
                                1888,
                                2545,
                                741,
                                2109,
                                895
                            ],
                            "color": "#e303fc"
                        },
                        {
                            "name": "Complete Purchase",
                            "data": [
                                1324,
                                671,
                                144,
                                373,
                                769,
                                1791,
                                106,
                                145,
                                468,
                                489,
                                943,
                                119,
                                1161,
                                66,
                                195,
                                1136,
                                199,
                                2244,
                                78,
                                481,
                                158,
                                767,
                                2127,
                                545
                            ],
                            "color": "#fc032d"
                        },
                        {
                            "name": "Abandon Cart",
                            "data": [
                                684,
                                78,
                                1984,
                                131,
                                214,
                                1117,
                                738,
                                172,
                                82,
                                1448,
                                211,
                                100,
                                2043,
                                927,
                                210,
                                1306,
                                206,
                                92,
                                1354,
                                237,
                                130,
                                123,
                                234,
                                345
                            ],
                            "color": "#52fc03"
                        },
                        {
                            "name": "Profile Push",
                            "data": [
                                198,
                                167,
                                1079,
                                1937,
                                999,
                                178,
                                253,
                                1040,
                                257,
                                1088,
                                500,
                                1722,
                                400,
                                2993,
                                673,
                                58,
                                992,
                                413,
                                53,
                                1467,
                                202,
                                1517,
                                147,
                                1722
                            ],
                            "color": "#fca103"
                        }
                    ],
                    "axis_data": [
                        "2021-06-30T00:00:00+08:000",
                        "2021-06-30T01:00:00+08:00",
                        "2021-06-30T02:00:00+08:00",
                        "2021-06-30T03:00:00+08:00",
                        "2021-06-30T04:00:00+08:00",
                        "2021-06-30T05:00:00+08:00",
                        "2021-06-30T06:00:00+08:00",
                        "2021-06-30T07:00:00+08:00",
                        "2021-06-30T08:00:00+08:00",
                        "2021-06-30T09:00:00+08:00",
                        "2021-06-30T10:00:00+08:00",
                        "2021-06-30T11:00:00+08:00",
                        "2021-06-30T12:00:00+08:00",
                        "2021-06-30T13:00:00+08:00",
                        "2021-06-30T14:00:00+08:00",
                        "2021-06-30T15:00:00+08:00",
                        "2021-06-30T16:00:00+08:00",
                        "2021-06-30T17:00:00+08:00",
                        "2021-06-30T18:00:00+08:00",
                        "2021-06-30T19:00:00+08:00",
                        "2021-06-30T20:00:00+08:00",
                        "2021-06-30T21:00:00+08:00",
                        "2021-06-30T22:00:00+08:00",
                        "2021-06-30T23:00:00+08:00"
                    ]
                }
            }

        elif metric_id == "metric_id_404" and metadata["id"] == "106":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_404",
                    "metric_type": "line",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "count",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_505",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        {
                            "filter_id": "filter_id_506",
                            "values": "Profile Push, Account Created, Abandon Cart, Profile Push, Complete Purchase, Browse",
                            "filter_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ],
                            "filter_label": "Select Events (upto 5)",
                            "max_select_limit" : 5,
                            "filter_type": "multi_dropdown",
                            "selected_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ]
                        }
                    ],
                    "metric_data": [
                        {
                            "name": "Account Created",
                            "data": [
                                1782,
                                200,
                                2785,
                                964,
                                403,
                                831,
                                227,
                                1709,
                                56,
                                2715,
                                140,
                                82,
                                1611,
                                356,
                                311,
                                529,
                                1049,
                                1685,
                                392,
                                1551,
                                296,
                                2214,
                                129,
                                3059
                            ],
                            "color": "#030bfc"
                        },
                        {
                            "name": "Browse",
                            "data": [
                                280,
                                906,
                                246,
                                1650,
                                1647,
                                268,
                                417,
                                250,
                                1928,
                                288,
                                274,
                                189,
                                439,
                                1560,
                                794,
                                231,
                                281,
                                994,
                                508,
                                1888,
                                2545,
                                741,
                                2109,
                                895
                            ],
                            "color": "#e303fc"
                        },
                        {
                            "name": "Complete Purchase",
                            "data": [
                                1324,
                                671,
                                144,
                                373,
                                769,
                                1791,
                                106,
                                145,
                                468,
                                489,
                                943,
                                119,
                                1161,
                                66,
                                195,
                                1136,
                                199,
                                2244,
                                78,
                                481,
                                158,
                                767,
                                2127,
                                545
                            ],
                            "color": "#fc032d"
                        },
                        {
                            "name": "Abandon Cart",
                            "data": [
                                684,
                                78,
                                1984,
                                131,
                                214,
                                1117,
                                738,
                                172,
                                82,
                                1448,
                                211,
                                100,
                                2043,
                                927,
                                210,
                                1306,
                                206,
                                92,
                                1354,
                                237,
                                130,
                                123,
                                234,
                                345
                            ],
                            "color": "#52fc03"
                        },
                        {
                            "name": "Profile Push",
                            "data": [
                                198,
                                167,
                                1079,
                                1937,
                                999,
                                178,
                                253,
                                1040,
                                257,
                                1088,
                                500,
                                1722,
                                400,
                                2993,
                                673,
                                58,
                                992,
                                413,
                                53,
                                1467,
                                202,
                                1517,
                                147,
                                1722
                            ],
                            "color": "#fca103"
                        }
                    ],
                    "axis_data": [
                        "2021-06-30T00:00:00+08:000",
                        "2021-06-30T01:00:00+08:00",
                        "2021-06-30T02:00:00+08:00",
                        "2021-06-30T03:00:00+08:00",
                        "2021-06-30T04:00:00+08:00",
                        "2021-06-30T05:00:00+08:00",
                        "2021-06-30T06:00:00+08:00",
                        "2021-06-30T07:00:00+08:00",
                        "2021-06-30T08:00:00+08:00",
                        "2021-06-30T09:00:00+08:00",
                        "2021-06-30T10:00:00+08:00",
                        "2021-06-30T11:00:00+08:00",
                        "2021-06-30T12:00:00+08:00",
                        "2021-06-30T13:00:00+08:00",
                        "2021-06-30T14:00:00+08:00",
                        "2021-06-30T15:00:00+08:00",
                        "2021-06-30T16:00:00+08:00",
                        "2021-06-30T17:00:00+08:00",
                        "2021-06-30T18:00:00+08:00",
                        "2021-06-30T19:00:00+08:00",
                        "2021-06-30T20:00:00+08:00",
                        "2021-06-30T21:00:00+08:00",
                        "2021-06-30T22:00:00+08:00",
                        "2021-06-30T23:00:00+08:00"
                    ]
                }
            }

        elif metric_id == "metric_id_404" and metadata["id"] == "107":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_404",
                    "metric_type": "line",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "count",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_505",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        {
                            "filter_id": "filter_id_506",
                            "values": "Profile Push, Account Created, Abandon Cart, Profile Push, Complete Purchase, Browse",
                            "filter_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ],
                            "filter_label": "Select Events (upto 5)",
                            "filter_type": "multi_dropdown",
                            "max_select_limit" : 5,
                            "selected_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ]
                        }
                    ],
                    "metric_data": [
                        {
                            "name": "Account Created",
                            "data": [
                                1782,
                                200,
                                2785,
                                964,
                                403,
                                831,
                                227,
                                1709,
                                56,
                                2715,
                                140,
                                82,
                                1611,
                                356,
                                311,
                                529,
                                1049,
                                1685,
                                392,
                                1551,
                                296,
                                2214,
                                129,
                                3059
                            ],
                            "color": "#030bfc"
                        },
                        {
                            "name": "Browse",
                            "data": [
                                280,
                                906,
                                246,
                                1650,
                                1647,
                                268,
                                417,
                                250,
                                1928,
                                288,
                                274,
                                189,
                                439,
                                1560,
                                794,
                                231,
                                281,
                                994,
                                508,
                                1888,
                                2545,
                                741,
                                2109,
                                895
                            ],
                            "color": "#e303fc"
                        },
                        {
                            "name": "Complete Purchase",
                            "data": [
                                1324,
                                671,
                                144,
                                373,
                                769,
                                1791,
                                106,
                                145,
                                468,
                                489,
                                943,
                                119,
                                1161,
                                66,
                                195,
                                1136,
                                199,
                                2244,
                                78,
                                481,
                                158,
                                767,
                                2127,
                                545
                            ],
                            "color": "#fc032d"
                        },
                        {
                            "name": "Abandon Cart",
                            "data": [
                                684,
                                78,
                                1984,
                                131,
                                214,
                                1117,
                                738,
                                172,
                                82,
                                1448,
                                211,
                                100,
                                2043,
                                927,
                                210,
                                1306,
                                206,
                                92,
                                1354,
                                237,
                                130,
                                123,
                                234,
                                345
                            ],
                            "color": "#52fc03"
                        },
                        {
                            "name": "Profile Push",
                            "data": [
                                198,
                                167,
                                1079,
                                1937,
                                999,
                                178,
                                253,
                                1040,
                                257,
                                1088,
                                500,
                                1722,
                                400,
                                2993,
                                673,
                                58,
                                992,
                                413,
                                53,
                                1467,
                                202,
                                1517,
                                147,
                                1722
                            ],
                            "color": "#fca103"
                        }
                    ],
                    "axis_data": [
                        "2021-06-30T00:00:00+08:000",
                        "2021-06-30T01:00:00+08:00",
                        "2021-06-30T02:00:00+08:00",
                        "2021-06-30T03:00:00+08:00",
                        "2021-06-30T04:00:00+08:00",
                        "2021-06-30T05:00:00+08:00",
                        "2021-06-30T06:00:00+08:00",
                        "2021-06-30T07:00:00+08:00",
                        "2021-06-30T08:00:00+08:00",
                        "2021-06-30T09:00:00+08:00",
                        "2021-06-30T10:00:00+08:00",
                        "2021-06-30T11:00:00+08:00",
                        "2021-06-30T12:00:00+08:00",
                        "2021-06-30T13:00:00+08:00",
                        "2021-06-30T14:00:00+08:00",
                        "2021-06-30T15:00:00+08:00",
                        "2021-06-30T16:00:00+08:00",
                        "2021-06-30T17:00:00+08:00",
                        "2021-06-30T18:00:00+08:00",
                        "2021-06-30T19:00:00+08:00",
                        "2021-06-30T20:00:00+08:00",
                        "2021-06-30T21:00:00+08:00",
                        "2021-06-30T22:00:00+08:00",
                        "2021-06-30T23:00:00+08:00"
                    ]
                }
            }

        elif metric_id == "metric_id_404" and metadata["id"] == "108":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_404",
                    "metric_type": "line",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "count",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_505",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        {
                            "filter_id": "filter_id_506",
                            "values": "Profile Push, Account Created, Abandon Cart, Profile Push, Complete Purchase, Browse",
                            "filter_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ],
                            "filter_label": "Select Events (upto 5)",
                            "filter_type": "multi_dropdown",
                            "max_select_limit" : 5,
                            "selected_values": [
                                {"id": "Account Created", "name": "Account Created"},
                                {"id": "Abandon Cart", "name": "Abandon Cart"},
                                {"id": "Profile Push", "name": "Profile Push"},
                                {"id": "Complete Purchase", "name": "Complete Purchase"},
                                {"id": "Browse", "name": "Browse"}
                            ]
                        }
                    ],
                    "metric_data": [
                        {
                            "name": "Account Created",
                            "data": [
                                1782,
                                200,
                                2785,
                                964,
                                403,
                                831,
                                227,
                                1709,
                                56,
                                2715,
                                140,
                                82,
                                1611,
                                356,
                                311,
                                529,
                                1049,
                                1685,
                                392,
                                1551,
                                296,
                                2214,
                                129,
                                3059
                            ],
                            "color": "#030bfc"
                        },
                        {
                            "name": "Browse",
                            "data": [
                                280,
                                906,
                                246,
                                1650,
                                1647,
                                268,
                                417,
                                250,
                                1928,
                                288,
                                274,
                                189,
                                439,
                                1560,
                                794,
                                231,
                                281,
                                994,
                                508,
                                1888,
                                2545,
                                741,
                                2109,
                                895
                            ],
                            "color": "#e303fc"
                        },
                        {
                            "name": "Complete Purchase",
                            "data": [
                                1324,
                                671,
                                144,
                                373,
                                769,
                                1791,
                                106,
                                145,
                                468,
                                489,
                                943,
                                119,
                                1161,
                                66,
                                195,
                                1136,
                                199,
                                2244,
                                78,
                                481,
                                158,
                                767,
                                2127,
                                545
                            ],
                            "color": "#fc032d"
                        },
                        {
                            "name": "Abandon Cart",
                            "data": [
                                684,
                                78,
                                1984,
                                131,
                                214,
                                1117,
                                738,
                                172,
                                82,
                                1448,
                                211,
                                100,
                                2043,
                                927,
                                210,
                                1306,
                                206,
                                92,
                                1354,
                                237,
                                130,
                                123,
                                234,
                                345
                            ],
                            "color": "#52fc03"
                        },
                        {
                            "name": "Profile Push",
                            "data": [
                                198,
                                167,
                                1079,
                                1937,
                                999,
                                178,
                                253,
                                1040,
                                257,
                                1088,
                                500,
                                1722,
                                400,
                                2993,
                                673,
                                58,
                                992,
                                413,
                                53,
                                1467,
                                202,
                                1517,
                                147,
                                1722
                            ],
                            "color": "#fca103"
                        }
                    ],
                    "axis_data": [
                        "2021-06-30T00:00:00+08:000",
                        "2021-06-30T01:00:00+08:00",
                        "2021-06-30T02:00:00+08:00",
                        "2021-06-30T03:00:00+08:00",
                        "2021-06-30T04:00:00+08:00",
                        "2021-06-30T05:00:00+08:00",
                        "2021-06-30T06:00:00+08:00",
                        "2021-06-30T07:00:00+08:00",
                        "2021-06-30T08:00:00+08:00",
                        "2021-06-30T09:00:00+08:00",
                        "2021-06-30T10:00:00+08:00",
                        "2021-06-30T11:00:00+08:00",
                        "2021-06-30T12:00:00+08:00",
                        "2021-06-30T13:00:00+08:00",
                        "2021-06-30T14:00:00+08:00",
                        "2021-06-30T15:00:00+08:00",
                        "2021-06-30T16:00:00+08:00",
                        "2021-06-30T17:00:00+08:00",
                        "2021-06-30T18:00:00+08:00",
                        "2021-06-30T19:00:00+08:00",
                        "2021-06-30T20:00:00+08:00",
                        "2021-06-30T21:00:00+08:00",
                        "2021-06-30T22:00:00+08:00",
                        "2021-06-30T23:00:00+08:00"
                    ]
                }
            }

        elif metric_id == "metric_id_406" and metadata['start'] == 1 and metadata['end'] == 10:
            apiData = {
                    "code": 200,
                    "msg": "Success",
                    "status": "success",
                    "data": {
                        "metric_id": "metric_id_406",
                        "metric_type": "",
                        "metric_sub_type": "",
                        "metric_layout": "horizontal",
                        "category_key": "table",
                        "keys": [
                        "event",
                        "error",
                        "cdp_id",
                        "description",
                        "date_time",
                        "count",
                        "image",
                        "customer_id"
                        ],
                        "metric_data": [
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        }
                        ]
                    }
                    }

        elif metric_id == "metric_id_406" and metadata['start'] == 11 and metadata['end'] == 20:
            apiData = {
                    "code": 200,
                    "msg": "Success",
                    "status": "success",
                    "data": {
                        "metric_id": "metric_id_406",
                        "metric_type": "",
                        "metric_sub_type": "",
                        "metric_layout": "horizontal",
                        "category_key": "table",
                        "keys": [
                        "event",
                        "error",
                        "cdp_id",
                        "description",
                        "date_time",
                        "count",
                        "image",
                        "customer_id"
                        ],
                        "metric_data": [
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        }
                        ]
                    }
                    }

        elif metric_id == "metric_id_406" and metadata['start'] == 21 and metadata['end'] == 30:
            apiData = {
                    "code": 200,
                    "msg": "Success",
                    "status": "success",
                    "data": {
                        "metric_id": "metric_id_406",
                        "metric_type": "",
                        "metric_sub_type": "",
                        "metric_layout": "horizontal",
                        "category_key": "table",
                        "keys": [
                        "event",
                        "error",
                        "cdp_id",
                        "description",
                        "date_time",
                        "count",
                        "image",
                        "customer_id"
                        ],
                        "metric_data": [
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        }
                        ]
                    }
                    }

        elif metric_id == "metric_id_406":  
            apiData = {
                    "code": 200,
                    "msg": "Success",
                    "status": "success",
                    "data": {
                        "metric_id": "metric_id_406",
                        "metric_type": "",
                        "metric_sub_type": "",
                        "metric_layout": "horizontal",
                        "category_key": "table",
                        "keys": [
                        "event",
                        "error",
                        "cdp_id",
                        "description",
                        "date_time",
                        "count",
                        "image",
                        "customer_id"
                        ],
                        "metric_data": [
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        },
                        {
                            "event": "Page browse",
                            "error": "ERR10018",
                            "cdp_id": "deacknkdnkcd23",
                            "date_time": "2021/07/15 10:47:20 pm",
                            "description": "The maximum length of payload parameter value for key [items[].url] is 512 characters",
                            "count": "36662",
                            "image": "android.svg",
                            "customer_id": "989898989898"
                        }
                        ]
                    }
                    }  

        elif metric_id == "metric_id_405":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_405",
                    "metric_type": "",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "category_key": "information",
                    "keys": [
                        "connectionid",
                        "title",
                        "description",
                        "client_id"
                    ],
                    "metric_data": [
                        {
                            "client_id": "1001",
                            "connectionid": "101",
                            "description": "description 1",
                            "title": "title 1"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "102",
                            "description": "description 1",
                            "title": "title 1"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "103",
                            "description": "description 1",
                            "title": "title 1"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "101",
                            "description": "description 2",
                            "title": "title 2"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "102",
                            "description": "description 2",
                            "title": "title 2"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "103",
                            "description": "description 2",
                            "title": "title 2"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "101",
                            "description": "description 3",
                            "title": "title 3"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "102",
                            "description": "description 3",
                            "title": "title 3"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "103",
                            "description": "description 3",
                            "title": "title 3"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "101",
                            "description": "description 4",
                            "title": "title 4"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "102",
                            "description": "description 4",
                            "title": "title 4"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "103",
                            "description": "description 4",
                            "title": "title 4"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "101",
                            "description": "description 5",
                            "title": "title 5"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "102",
                            "description": "description 5",
                            "title": "title 5"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "103",
                            "description": "description 5",
                            "title": "title 5"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "101",
                            "description": "description 6",
                            "title": "title 6"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "102",
                            "description": "description 6",
                            "title": "title 6"
                        },
                        {
                            "client_id": "1001",
                            "connectionid": "103",
                            "description": "description 6",
                            "title": "title 6"
                        }
                    ]
                }
            }
        elif metric_id == "metric_id_407":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_407",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "",
                            "value": "20500"
                        }
                        
                    ]
                }
            }

        elif metric_id == "metric_id_408":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_408",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "Deterministic",
                            "value": "5000"
                        },
                        {
                            "key": "Shared",
                            "value": "2000"
                        }
                    ]
                }
            }
        elif metric_id == "metric_id_409":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_409",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "Ingested",
                            "value": "5000"
                        },
                        {
                            "key": "Exported",
                            "value": "2000"
                        }
                    ]
                }
            }
        elif metric_id == "metric_id_410":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_410",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "Email",
                            "value": "10000"
                        },
                        {
                            "key": "SMS",
                            "value": "5500"
                        },
                        {
                            "key": "APN",
                            "value": "2500"
                        },
                        {
                            "key": "WPN",
                            "value": "2500"
                        }
                    ]
                }
            }
        elif metric_id == "metric_id_411":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_411",
                    "metric_type": "bar",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "Total Customers",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_521",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        {
                            "filter_id": "filter_id_522",
                            "filter_type": "date_range",
                            "filter_values": "",
                            "selected_values": [
                                "2020-11-09",
                                "2021-11-09"
                            ]
                        }
                    ],
                    "metric_data": [
                        {
                            "color": "blue",
                            "name": "In Record",
                            "data": [
                                110,
                                175,
                                151,
                                129,
                                190,
                                60,
                                52,
                                129,
                                241,
                                203,
                                120,
                                180,
                                183,
                                84,
                                194,
                                39
                            ]
                        },
                        {
                            "color": "green",
                            "name": "Out Record",
                            "data": [
                                93,
                                164,
                                145,
                                129,
                                186,
                                51,
                                50,
                                112,
                                229,
                                184,
                                116,
                                173,
                                182,
                                81,
                                182,
                                25
                            ]
                        }
                    ],
                    "axis_data": [
                        "2010",
                        "2011",
                        "2012",
                        "2013",
                        "2014",
                        "2015",
                        "2016",
                        "2017",
                        "2018",
                        "2019",
                        "2020",
                        "2021"
                    ]
                }
            }
        elif metric_id == "metric_id_412":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_412",
                    "metric_type": "bar",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "Total IDs stitched",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_523",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        {
                            "filter_id": "filter_id_524",
                            "filter_type": "date_range",
                            "filter_values": "",
                            "selected_values": [
                                "2020-11-09",
                                "2021-11-09"
                            ]
                        }
                    ],
                    "metric_data": [
                        {
                            "color": "blue",
                            "name": "In Record",
                            "data": [
                                110,
                                175,
                                151,
                                129,
                                190,
                                60,
                                52,
                                129,
                                241,
                                203,
                                120,
                                180,
                                183,
                                84,
                                194,
                                39
                            ]
                        },
                        {
                            "color": "green",
                            "name": "Out Record",
                            "data": [
                                93,
                                164,
                                145,
                                129,
                                186,
                                51,
                                50,
                                112,
                                229,
                                184,
                                116,
                                173,
                                182,
                                81,
                                182,
                                25
                            ]
                        }
                    ],
                    "axis_data": [
                        "2010",
                        "2011",
                        "2012",
                        "2013",
                        "2014",
                        "2015",
                        "2016",
                        "2017",
                        "2018",
                        "2019",
                        "2020",
                        "2021"
                    ]
                }
            }
        elif metric_id == "metric_id_413":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_413",
                    "metric_type": "bar",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "Total Data Points",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_525",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        {
                            "filter_id": "filter_id_526",
                            "filter_type": "date_range",
                            "filter_values": "",
                            "selected_values": [
                                "2020-11-09",
                                "2021-11-09"
                            ]
                        }
                    ],
                    "metric_data": [
                        {
                            "color": "blue",
                            "name": "In Record",
                            "data": [
                                110,
                                175,
                                151,
                                129,
                                190,
                                60,
                                52,
                                129,
                                241,
                                203,
                                120,
                                180,
                                183,
                                84,
                                194,
                                39
                            ]
                        },
                        {
                            "color": "green",
                            "name": "Out Record",
                            "data": [
                                93,
                                164,
                                145,
                                129,
                                186,
                                51,
                                50,
                                112,
                                229,
                                184,
                                116,
                                173,
                                182,
                                81,
                                182,
                                25
                            ]
                        }
                    ],
                    "axis_data": [
                        "2010",
                        "2011",
                        "2012",
                        "2013",
                        "2014",
                        "2015",
                        "2016",
                        "2017",
                        "2018",
                        "2019",
                        "2020",
                        "2021"
                    ]
                }
            }
        elif metric_id == "metric_id_414":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_414",
                    "metric_type": "bar",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "Total Customers",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_527",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        {   "filter_id": "filter_id_528",
                            "filter_type": "date_range",
                            "filter_values": "",
                            "selected_values": [
                                "2020-11-09",
                                "2021-11-09"
                            ]
                        }
                    ],
                    "metric_data": [
                        {
                            "color": "blue",
                            "name": "In Record",
                            "data": [
                                110,
                                175,
                                151,
                                129,
                                190,
                                60,
                                52,
                                129,
                                241,
                                203,
                                120,
                                180,
                                183,
                                84,
                                194,
                                39
                            ]
                        },
                        {
                            "color": "green",
                            "name": "Out Record",
                            "data": [
                                93,
                                164,
                                145,
                                129,
                                186,
                                51,
                                50,
                                112,
                                229,
                                184,
                                116,
                                173,
                                182,
                                81,
                                182,
                                25
                            ]
                        }
                    ],
                    "axis_data": [
                        "2010",
                        "2011",
                        "2012",
                        "2013",
                        "2014",
                        "2015",
                        "2016",
                        "2017",
                        "2018",
                        "2019",
                        "2020",
                        "2021"
                    ]
                }
            }
        elif metric_id == "metric_id_415":  
            apiData = {
                    "code": 200,
                    "msg": "Success",
                    "status": "success",
                    "data": {
                        "metric_id": "metric_id_415",
                        "metric_type": "",
                        "metric_sub_type": "",
                        "metric_layout": "horizontal",
                        "category_key": "table",
                        "keys": CUSTOMER_LIST_KEYS,                         
                        "metric_data": CUSTOMER_LIST
                }
            }
        elif metric_id == "metric_id_416":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_416",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "",
                            "value": "500230"
                        }
                        
                    ]
                }
            }

        elif metric_id == "metric_id_417":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_417",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "",
                            "value": "34"
                        }
                    ]
                }
            }
        elif metric_id == "metric_id_418":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_418",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "",
                            "value": "83110"
                        }
                    ]
                }
            }
        elif metric_id == "metric_id_419":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_419",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "",
                            "value": "20100"
                        }
                    ]
                }
            }
        elif metric_id == "metric_id_420":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_420",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "",
                            "value": "High"
                        }
                    ]
                }
            }
        elif metric_id == "metric_id_421":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_421",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "",
                            "value": "App Push Notification"
                        }
                    ]
                }
            }
        elif metric_id == "metric_id_422":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_422",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "",
                            "value": "500230"
                        }
                        
                    ]
                }
            }

        elif metric_id == "metric_id_423":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_423",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "",
                            "value": "34"
                        }
                    ]
                }
            }
        elif metric_id == "metric_id_424":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_424",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "",
                            "value": "83110"
                        }
                    ]
                }
            }
        elif metric_id == "metric_id_425":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_425",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "",
                            "value": "20100"
                        }
                    ]
                }
            }
        elif metric_id == "metric_id_426":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_426",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "",
                            "value": "Books"
                        }
                    ]
                }
            }
        elif metric_id == "metric_id_427":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_427",
                    "metric_type": "card",
                    "keys": [
                        "key",
                        "value"
                    ],
                    "metric_data": [
                        {
                            "key": "",
                            "value": "Fiction"
                        }
                    ]
                }
            }
        elif metric_id == "metric_id_428":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_428",
                    "metric_type": "bar",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "Total Revenue",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_529",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        
                    ],
                    "metric_data": [
                        {
                            "color": "blue",
                            "name": "In Record",
                            "data": [
                                110,
                                175,
                                151,
                                129,
                                190,
                                60,
                                52,
                                129,
                                241,
                                203,
                                120,
                                180,
                                183,
                                84,
                                194,
                                39
                            ]
                        },
                        {
                            "color": "green",
                            "name": "Out Record",
                            "data": [
                                93,
                                164,
                                145,
                                129,
                                186,
                                51,
                                50,
                                112,
                                229,
                                184,
                                116,
                                173,
                                182,
                                81,
                                182,
                                25
                            ]
                        }
                    ],
                    "axis_data": [
                        "2010",
                        "2011",
                        "2012",
                        "2013",
                        "2014",
                        "2015",
                        "2016",
                        "2017",
                        "2018",
                        "2019",
                        "2020",
                        "2021"
                    ]
                }
            }
        elif metric_id == "metric_id_429":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_429",
                    "metric_type": "bar",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "Total Revenue",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_530",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        
                    ],
                    "metric_data": [
                        {
                            "color": "blue",
                            "name": "In Record",
                            "data": [
                                110,
                                175,
                                151,
                                129,
                                190,
                                60,
                                52,
                                129,
                                241,
                                203,
                                120,
                                180,
                                183,
                                84,
                                194,
                                39
                            ]
                        },
                        {
                            "color": "green",
                            "name": "Out Record",
                            "data": [
                                93,
                                164,
                                145,
                                129,
                                186,
                                51,
                                50,
                                112,
                                229,
                                184,
                                116,
                                173,
                                182,
                                81,
                                182,
                                25
                            ]
                        }
                    ],
                    "axis_data": [
                        "2010",
                        "2011",
                        "2012",
                        "2013",
                        "2014",
                        "2015",
                        "2016",
                        "2017",
                        "2018",
                        "2019",
                        "2020",
                        "2021"
                    ]
                }
            }
        elif metric_id == "metric_id_430":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_430",
                    "metric_type": "bar",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "Total Revenue",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_531",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        
                    ],
                    "metric_data": [
                        {
                            "color": "blue",
                            "name": "In Record",
                            "data": [
                                110,
                                175,
                                151,
                                129,
                                190,
                                60,
                                52,
                                129,
                                241,
                                203,
                                120,
                                180,
                                183,
                                84,
                                194,
                                39
                            ]
                        },
                        {
                            "color": "green",
                            "name": "Out Record",
                            "data": [
                                93,
                                164,
                                145,
                                129,
                                186,
                                51,
                                50,
                                112,
                                229,
                                184,
                                116,
                                173,
                                182,
                                81,
                                182,
                                25
                            ]
                        }
                    ],
                    "axis_data": [
                        "2010",
                        "2011",
                        "2012",
                        "2013",
                        "2014",
                        "2015",
                        "2016",
                        "2017",
                        "2018",
                        "2019",
                        "2020",
                        "2021"
                    ]
                }
            }
        elif metric_id == "metric_id_431":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_431",
                    "metric_type": "bar",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "Total Revenue",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_532",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        
                    ],
                    "metric_data": [
                        {
                            "color": "blue",
                            "name": "In Record",
                            "data": [
                                110,
                                175,
                                151,
                                129,
                                190,
                                60,
                                52,
                                129,
                                241,
                                203,
                                120,
                                180,
                                183,
                                84,
                                194,
                                39
                            ]
                        },
                        {
                            "color": "green",
                            "name": "Out Record",
                            "data": [
                                93,
                                164,
                                145,
                                129,
                                186,
                                51,
                                50,
                                112,
                                229,
                                184,
                                116,
                                173,
                                182,
                                81,
                                182,
                                25
                            ]
                        }
                    ],
                    "axis_data": [
                        "2010",
                        "2011",
                        "2012",
                        "2013",
                        "2014",
                        "2015",
                        "2016",
                        "2017",
                        "2018",
                        "2019",
                        "2020",
                        "2021"
                    ]
                }
            }
        elif metric_id == "metric_id_432":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_432",
                    "metric_type": "bar",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "Total Revenue",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_533",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        
                    ],
                    "metric_data": [
                        {
                            "color": "blue",
                            "name": "In Record",
                            "data": [
                                110,
                                175,
                                151,
                                129,
                                190,
                                60,
                                52,
                                129,
                                241,
                                203,
                                120,
                                180,
                                183,
                                84,
                                194,
                                39
                            ]
                        },
                        {
                            "color": "green",
                            "name": "Out Record",
                            "data": [
                                93,
                                164,
                                145,
                                129,
                                186,
                                51,
                                50,
                                112,
                                229,
                                184,
                                116,
                                173,
                                182,
                                81,
                                182,
                                25
                            ]
                        }
                    ],
                    "axis_data": [
                        "2010",
                        "2011",
                        "2012",
                        "2013",
                        "2014",
                        "2015",
                        "2016",
                        "2017",
                        "2018",
                        "2019",
                        "2020",
                        "2021"
                    ]
                }
            }
        elif metric_id == "metric_id_433":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_433",
                    "metric_type": "pie",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_534",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        
                    ],
                    "metric_data": [
                        {
                            "color": "blue",
                            "name": "In Record",
                            "data": [
                                110,
                                175,
                                151,
                                129,
                                190,
                                60,
                                52,
                                129,
                                241,
                                203,
                                120,
                                180,
                                183,
                                84,
                                194,
                                39
                            ]
                        },
                        {
                            "color": "green",
                            "name": "Out Record",
                            "data": [
                                93,
                                164,
                                145,
                                129,
                                186,
                                51,
                                50,
                                112,
                                229,
                                184,
                                116,
                                173,
                                182,
                                81,
                                182,
                                25
                            ]
                        }
                    ],
                    "axis_data": [
                        "2010",
                        "2011",
                        "2012",
                        "2013",
                        "2014",
                        "2015",
                        "2016",
                        "2017",
                        "2018",
                        "2019",
                        "2020",
                        "2021"
                    ]
                }
            }
        elif metric_id == "metric_id_434":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "metric_id_434",
                    "metric_type": "pie",
                    "metric_sub_type": "",
                    "metric_layout": "horizontal",
                    "y_axis_text": "",
                    "metric_pivot_key": "event_name",
                    "metric_axis_key": "time_period",
                    "colors": [
                        "#030bfc",
                        "#e303fc",
                        "#fc032d",
                        "#52fc03",
                        "#fca103"
                    ],
                    "keys": [
                    ],
                    "metric_filter": [
                        {
                            "filter_id": "filter_id_535",
                            "values": "Hourly, Monthly, Quaterly, Yearly",
                            "filter_values": [
                                {"id": "Hourly", "name": "Hourly"},
                                {"id": "Monthly", "name": "Monthly"},
                                {"id": "Quaterly", "name": "Quaterly"},
                                {"id": "Yearly", "name": "Yearly"}
                            ],
                            "filter_label": "Time Period",
                            "filter_type": "dropdown_timeperiod",
                            "selected_values": [
                                {"id": "Quaterly", "name": "Quaterly"}
                            ]
                        },
                        
                    ],
                    "metric_data": [
                        {
                            "color": "blue",
                            "name": "In Record",
                            "data": [
                                110,
                                175,
                                151,
                                129,
                                190,
                                60,
                                52,
                                129,
                                241,
                                203,
                                120,
                                180,
                                183,
                                84,
                                194,
                                39
                            ]
                        },
                        {
                            "color": "green",
                            "name": "Out Record",
                            "data": [
                                93,
                                164,
                                145,
                                129,
                                186,
                                51,
                                50,
                                112,
                                229,
                                184,
                                116,
                                173,
                                182,
                                81,
                                182,
                                25
                            ]
                        }
                    ],
                    "axis_data": [
                        "2010",
                        "2011",
                        "2012",
                        "2013",
                        "2014",
                        "2015",
                        "2016",
                        "2017",
                        "2018",
                        "2019",
                        "2020",
                        "2021"
                    ]
                }
            }
        elif metric_id == "null":
            apiData = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "metric_id": "",
                    "metric_type": "",
                    "keys": None
                }
            }
            
        else:
            apiData = {
                "status": "Error",
                "message": "Something Went Wrong",
                "code": 500
            }

        print('metric_data response', apiData)
        return jsonify(apiData)
    except Exception as e:
        print(e)
        return jsonify({
            "status": "Error",
            "message": "Something Went Wrong",
            "code": 500
        })


@app.route("/connector_data", methods=['POST'])
def connector_data():
    try:
        apiData = {
            "status": "success",
            "code": 200,
            "message": None,
            "data": {
                "component_type": "connector",
                "source": {
                    "title": "Sources",
                    "data": [
                        {
                            "name": "Appsflyer",
                            "icon_url": "https://dummyimage.com/40x40/000/fff",
                            "description": "Appsflyer",
                            "count": "7200",
                        },
                        {
                            "name": "Shopify",
                            "icon_url": "https://dummyimage.com/40x40/000/fff",
                            "description": "Shopify",
                            "count": "8200",
                        },
                        {
                            "name": "AWS S3",
                            "icon_url": "https://dummyimage.com/40x40/000/fff",
                            "description": "User info",
                            "count": "1796",
                        },
                        {
                            "name": "AWS S3",
                            "icon_url": "https://dummyimage.com/40x40/000/fff",
                            "description": "data info",
                            "count": "1183",
                        },
                        {
                            "name": "Branch",
                            "icon_url": "https://dummyimage.com/40x40/000/fff",
                            "description": "User info or data info",
                            "count": "4100",
                        },
                        {
                            "name": "Custom",
                            "icon_url": "https://dummyimage.com/40x40/000/fff",
                            "description": "User info or data info",
                            "count": "2200",
                        },
                        {
                            "name": "Branch",
                            "icon_url": "https://dummyimage.com/40x40/000/fff",
                            "description": "User info or data info",
                            "count": "4100",
                        },
                        {
                            "name": "Custom",
                            "icon_url": "https://dummyimage.com/40x40/000/fff",
                            "description": "User info or data info",
                            "count": "2200",
                        }
                    ]
                },
                "destination": {
                    "title": "Destinations",
                    "data": [
                        {
                            "name": "Appsflyer",
                            "icon_url": "https://dummyimage.com/40x40/000/fff",
                            "description": "Appsflyer",
                            "count": "4100",
                        },
                        {
                            "name": "Branch",
                            "icon_url": "https://dummyimage.com/40x40/000/fff",
                            "description": "User info",
                            "count": "8300",
                        },
                        {
                            "name": "Shopify",
                            "icon_url": "https://dummyimage.com/40x40/000/fff",
                            "description": "data info",
                            "count": "5436",
                        },
                        {
                            "name": "Appsflyer",
                            "icon_url": "https://dummyimage.com/40x40/000/fff",
                            "description": "User info or data info",
                            "count": "4141",
                        }
                    ]
                }
            }
        }

        return jsonify(apiData)

    except Exception as e:
        print(e)
        return jsonify({
            "status": "Error",
            "message": "Something Went Wrong",
            "code": 500
        })


@app.route("/filter_data", methods=["POST"])
def filter_data():
    try:
        req_obj = request.get_json()
        filter_ids = req_obj.get('filter_ids')
        data = []

        if filter_ids:
            for filter_id in filter_ids:
                if filter_id == "filter_id_501":
                    data.append({
                        "filter_type": "date_range",
                        "filter_id": "filter_id_501",
                        "filter_label": "Date Range",
                        "filter_values": [
                            "2016-01-01",
                            "2022-01-01"
                        ],
                        "selected_values": [
                            "2017-01-01",
                            "2019-01-01"
                        ]
                    })
                if filter_id == "filter_id_508":
                    data.append({
                        "filter_type": "single_dropdown",
                        "filter_id": "filter_id_508",
                        "filter_label": "Connection Type",
                        "filter_values": [
                            {"id": "All", "name": "All"},
                            {"id": "ingress", "name": "ingress"},
                            {"id": "egress", "name": "egress"}
                        ],
                        "selected_values": [
                            {"id": "All", "name": "All"}
                        ]
                    })
                if filter_id == "filter_id_509":
                    data.append({
                        "filter_type": "single_dropdown",
                        "filter_id": "filter_id_509",
                        "filter_label": "Connection Status",
                        "filter_values": [
                            {"id": "All", "name": "All"},
                            {"id": "operational", "name": "operational"},
                            {"id": "blocked", "name": "blocked"}
                        ],
                        "selected_values": [
                            {"id": "All", "name": "All"}
                        ]
                    })
        if data:
            apiData = {
                "status": "success",
                "code": 200,
                "message": None,
                "data": data
            }
        else:
            apiData = {
                "status": "Error",
                "message": "Something Went Wrong",
                "code": 500
            }

        pp(apiData)
        return apiData

    except Exception as e:
        print(e)
        return jsonify({
            "status": "Error",
            "message": "Something Went Wrong",
            "code": 500
        })


@app.route("/filtered_layout_data", methods=["POST"])
def filtered_layout_data():
    try:
        req_obj = request.get_json()
        layout_tab_id = req_obj.get('layout_tab_id')
        selected_filters = req_obj.get(
            'selected_filters')

        selected_filters.pop(0)

        pp(selected_filters)

        if layout_tab_id == "layout_tab_id_202":

            if selected_filters[0]["selected_values"][0]["name"] == "ingress" and selected_filters[1]["selected_values"][0]["name"] == "operational":
                apiData = {
                    "status": "success",
                    "code": 200,
                    "message": None,
                    "data": {
                        "graph_metric_ids": [
                            "metric_layout_304",
                            "metric_layout_304"
                        ],
                        "metadata": [
                            {
                                "connection_status": "operational",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "101",
                                "type": "connector"
                            },
                            {
                                "connection_status": "operational",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Mobile App",
                                "custom_connection_name": "Android SDK",
                                "description": "Integrate SDK with your android app",
                                "display_image_url": "android.svg",
                                "id": "103",
                                "type": "connector"
                            }
                        ]
                    }
                }

            elif selected_filters[0]["selected_values"][0]["name"] == "ingress" and selected_filters[1]["selected_values"][0]["name"] == "blocked":
                apiData = {
                    "status": "success",
                    "code": 200,
                    "message": None,
                    "data": {
                        "graph_metric_ids": [
                            "metric_layout_304",
                            "metric_layout_304"
                        ],
                        "metadata": [
                            {
                                "connection_status": "blocked",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "104",
                                "type": "connector"
                            },
                            {
                                "connection_status": "blocked",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Mobile App",
                                "custom_connection_name": "Android SDK",
                                "description": "Integrate SDK with your android app",
                                "display_image_url": "android.svg",
                                "id": "106",
                                "type": "connector"
                            }
                        ]
                    }
                }

            elif selected_filters[0]["selected_values"][0]["name"] == "egress" and selected_filters[1]["selected_values"][0]["name"] == "operational":
                apiData = {
                    "status": "success",
                    "code": 200,
                    "message": None,
                    "data": {
                        "graph_metric_ids": [
                            "metric_layout_304",
                            "metric_layout_304"
                        ],
                        "metadata": [
                            {
                                "connection_status": "operational",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "102",
                                "type": "connector"
                            },
                            {
                                "connection_status": "operational",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "105",
                                "type": "connector"
                            }
                        ]
                    }
                }

            elif selected_filters[0]["selected_values"][0]["name"] == "egress" and selected_filters[1]["selected_values"][0]["name"] == "blocked":
                apiData = {
                    "status": "success",
                    "code": 200,
                    "message": None,
                    "data": {
                        "graph_metric_ids": [
                            "metric_layout_304",
                            "metric_layout_304"
                        ],
                        "metadata": [
                            {
                                "connection_status": "blocked",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "107",
                                "type": "connector"
                            },
                            {
                                "connection_status": "blocked",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "108",
                                "type": "connector"
                            }
                        ]
                    }
                }

            elif selected_filters[0]["selected_values"][0]["name"] == "ingress" and selected_filters[1]["selected_values"][0]["name"] == "All":
                apiData = {
                    "status": "success",
                    "code": 200,
                    "message": None,
                    "data": {
                        "graph_metric_ids": [
                            "metric_layout_304",
                            "metric_layout_304",
                            "metric_layout_304",
                            "metric_layout_304"
                        ],
                        "metadata": [
                            {
                                "connection_status": "operational",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "101",
                                "type": "connector"
                            },
                            {
                                "connection_status": "operational",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Mobile App",
                                "custom_connection_name": "Android SDK",
                                "description": "Integrate SDK with your android app",
                                "display_image_url": "android.svg",
                                "id": "103",
                                "type": "connector"
                            },
                            {
                                "connection_status": "blocked",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "104",
                                "type": "connector"
                            },
                            {
                                "connection_status": "blocked",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Mobile App",
                                "custom_connection_name": "Android SDK",
                                "description": "Integrate SDK with your android app",
                                "display_image_url": "android.svg",
                                "id": "106",
                                "type": "connector"
                            }
                        ]
                    }
                }

            elif selected_filters[0]["selected_values"][0]["name"] == "egress" and selected_filters[1]["selected_values"][0]["name"] == "All":
                print("reached ahrer")
                apiData = {
                    "status": "success",
                    "code": 200,
                    "message": None,
                    "data": {
                        "graph_metric_ids": [
                            "metric_layout_304",
                            "metric_layout_304",
                            "metric_layout_304",
                            "metric_layout_304"
                        ],
                        "metadata": [
                            {
                                "connection_status": "operational",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "102",
                                "type": "connector"
                            },
                            {
                                "connection_status": "operational",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "105",
                                "type": "connector"
                            },
                            {
                                "connection_status": "blocked",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "107",
                                "type": "connector"
                            },
                            {
                                "connection_status": "blocked",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "108",
                                "type": "connector"
                            }

                        ]
                    }
                }

            elif selected_filters[0]["selected_values"][0]["name"] == "All" and selected_filters[1]["selected_values"][0]["name"] == "blocked":
                apiData = {
                    "status": "success",
                    "code": 200,
                    "message": None,
                    "data": {
                        "graph_metric_ids": [
                            "metric_layout_304",
                            "metric_layout_304",
                            "metric_layout_304",
                            "metric_layout_304"
                        ],
                        "metadata": [
                            {
                                "connection_status": "blocked",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "104",
                                "type": "connector"
                            },
                            {
                                "connection_status": "blocked",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Mobile App",
                                "custom_connection_name": "Android SDK",
                                "description": "Integrate SDK with your android app",
                                "display_image_url": "android.svg",
                                "id": "106",
                                "type": "connector"
                            },
                            {
                                "connection_status": "blocked",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "107",
                                "type": "connector"
                            },
                            {
                                "connection_status": "blocked",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "108",
                                "type": "connector"
                            }
                        ]
                    }
                }

            elif selected_filters[0]["selected_values"][0]["name"] == "All" and selected_filters[1]["selected_values"][0]["name"] == "operational":
                apiData = {
                    "status": "success",
                    "code": 200,
                    "message": None,
                    "data": {
                        "graph_metric_ids": [
                            "metric_layout_304",
                            "metric_layout_304",
                            "metric_layout_304",
                            "metric_layout_304"
                        ],
                        "metadata": [
                            {
                                "connection_status": "operational",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "101",
                                "type": "connector"
                            },
                            {
                                "connection_status": "operational",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Mobile App",
                                "custom_connection_name": "Android SDK",
                                "description": "Integrate SDK with your android app",
                                "display_image_url": "android.svg",
                                "id": "103",
                                "type": "connector"
                            },
                            {
                                "connection_status": "operational",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "102",
                                "type": "connector"
                            },
                            {
                                "connection_status": "operational",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "105",
                                "type": "connector"
                            }
                        ]
                    }
                }

            elif selected_filters[0]["selected_values"][0]["name"] == "All" and selected_filters[1]["selected_values"][0]["name"] == "All":
                apiData = {
                    "status": "success",
                    "code": 200,
                    "message": None,
                    "data": {
                        "graph_metric_ids": [
                            "metric_layout_304",
                            "metric_layout_304",
                            "metric_layout_304",
                            "metric_layout_304",
                            "metric_layout_304",
                            "metric_layout_304",
                            "metric_layout_304",
                            "metric_layout_304"
                        ],
                        "metadata": [
                            {
                                "connection_status": "operational",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "101",
                                "type": "connector"
                            },
                            {
                                "connection_status": "operational",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "102",
                                "type": "connector"
                            },
                            {
                                "connection_status": "operational",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Mobile App",
                                "custom_connection_name": "Android SDK",
                                "description": "Integrate SDK with your android app",
                                "display_image_url": "android.svg",
                                "id": "103",
                                "type": "connector"
                            },
                            {
                                "connection_status": "blocked",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "104",
                                "type": "connector"
                            },
                            {
                                "connection_status": "operational",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "105",
                                "type": "connector"
                            },
                            {
                                "connection_status": "blocked",
                                "connection_type": "ingress",
                                "connector_repository_group_name": "Mobile App",
                                "custom_connection_name": "Android SDK",
                                "description": "Integrate SDK with your android app",
                                "display_image_url": "android.svg",
                                "id": "106",
                                "type": "connector"
                            },
                            {
                                "connection_status": "blocked",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Servers",
                                "custom_connection_name": "Shopify",
                                "description": "Copy and paste the JS tags on your website",
                                "display_image_url": "shopify.svg",
                                "id": "107",
                                "type": "connector"
                            },
                            {
                                "connection_status": "blocked",
                                "connection_type": "egress",
                                "connector_repository_group_name": "Storage",
                                "custom_connection_name": "Amazon S3",
                                "description": "Feed data to your custom server",
                                "display_image_url": "aws_s3.svg",
                                "id": "108",
                                "type": "connector"
                            }
                        ]      
                    }
                }

            else:
                apiData = {
                    "status": "Error",
                    "message": "Something Went Wrong",
                    "code": 500
                }

        pp(apiData)
        return apiData
    except Exception as e:
        print(e)
        return jsonify({
            "status": "Error",
            "message": "Something Went Wrong",
            "code": 500
        })

@app.route("/search", methods=["POST"])
def search():
    try:
        apiData = {
                    "code": 200,
                    "msg": "Success",
                    "status": "success",
                    "data": {
                        "keys": CUSTOMER_LIST_KEYS,
                        "data": CUSTOMER_LIST
                }
            }
        return apiData
    except Exception as e:
        print(e)
        return jsonify({
            "status": "Error",
            "message": "Something Went Wrong",
            "code": 500
        })
@app.route("/get_events_by_user", methods=["POST"])
def get_events_by_user():
    try:
        apiData = {
                    "code": 200,
                    "msg": "Success",
                    "status": "success",
                    
                    "data": {
                        "today": [
                            {
                                "title": "Subscription Payment-Flipcart",
                                "description": "Bought Sparx Navy Blue SM-2322 Shoes Bought Sparx Navy Blue Sm-2322  Bought Sparx Navy Blue Sm-2322 ",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Grammerly",
                                "description": "Upgraded subscription from monthly to annual upgradedsubscription from monthly, ID,  Registration updated to premium which is annually charged. Registeration updated to Premium which is annually charged",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Flipcart",
                                "description": "Bought Sparx Navy Blue SM-2322 Shoes Bought Sparx Navy Blue Sm-2322  Bought Sparx Navy Blue Sm-2322 ",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Grammerly",
                                "description": "Upgraded subscription from monthly to annual upgradedsubscription from monthly, ID,  Registration updated to premium which is annually charged. Registeration updated to Premium which is annually charged",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            }
                            
                                 ],
                        "yesterday": [
                           {
                                "title": "Subscription Payment-Flipcart",
                                "description": "Bought Sparx Navy Blue SM-2322 Shoes Bought Sparx Navy Blue Sm-2322  Bought Sparx Navy Blue Sm-2322 ",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Grammerly",
                                "description": "Upgraded subscription from monthly to annual upgradedsubscription from monthly, ID,  Registration updated to premium which is annually charged. Registeration updated to Premium which is annually charged",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Flipcart",
                                "description": "Bought Sparx Navy Blue SM-2322 Shoes Bought Sparx Navy Blue Sm-2322  Bought Sparx Navy Blue Sm-2322 ",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Grammerly",
                                "description": "Upgraded subscription from monthly to annual upgradedsubscription from monthly, ID,  Registration updated to premium which is annually charged. Registeration updated to Premium which is annually charged",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            }
                                    ],
                        "17/11/2021": [
                            {
                                "title": "Subscription Payment-Flipcart",
                                "description": "Bought Sparx Navy Blue SM-2322 Shoes Bought Sparx Navy Blue Sm-2322  Bought Sparx Navy Blue Sm-2322 ",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Grammerly",
                                "description": "Upgraded subscription from monthly to annual upgradedsubscription from monthly, ID,  Registration updated to premium which is annually charged. Registeration updated to Premium which is annually charged",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Flipcart",
                                "description": "Bought Sparx Navy Blue SM-2322 Shoes Bought Sparx Navy Blue Sm-2322  Bought Sparx Navy Blue Sm-2322 ",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Grammerly",
                                "description": "Upgraded subscription from monthly to annual upgradedsubscription from monthly, ID,  Registration updated to premium which is annually charged. Registeration updated to Premium which is annually charged",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            }
                                    ],
                        "16/11/2021": [
                            {
                                "title": "Subscription Payment-Flipcart",
                                "description": "Bought Sparx Navy Blue SM-2322 Shoes Bought Sparx Navy Blue Sm-2322  Bought Sparx Navy Blue Sm-2322 ",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Grammerly",
                                "description": "Upgraded subscription from monthly to annual upgradedsubscription from monthly, ID,  Registration updated to premium which is annually charged. Registeration updated to Premium which is annually charged",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Flipcart",
                                "description": "Bought Sparx Navy Blue SM-2322 Shoes Bought Sparx Navy Blue Sm-2322  Bought Sparx Navy Blue Sm-2322 ",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Grammerly",
                                "description": "Upgraded subscription from monthly to annual upgradedsubscription from monthly, ID,  Registration updated to premium which is annually charged. Registeration updated to Premium which is annually charged",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            }
                                    ],
                        "15/11/2021": [
                            {
                                "title": "Subscription Payment-Flipcart",
                                "description": "Bought Sparx Navy Blue SM-2322 Shoes Bought Sparx Navy Blue Sm-2322  Bought Sparx Navy Blue Sm-2322 ",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Grammerly",
                                "description": "Upgraded subscription from monthly to annual upgradedsubscription from monthly, ID,  Registration updated to premium which is annually charged. Registeration updated to Premium which is annually charged",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Flipcart",
                                "description": "Bought Sparx Navy Blue SM-2322 Shoes Bought Sparx Navy Blue Sm-2322  Bought Sparx Navy Blue Sm-2322 ",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Grammerly",
                                "description": "Upgraded subscription from monthly to annual upgradedsubscription from monthly, ID,  Registration updated to premium which is annually charged. Registeration updated to Premium which is annually charged",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            }
                                    ],
                        "14/11/2021": [
                            {
                                "title": "Subscription Payment-Flipcart",
                                "description": "Bought Sparx Navy Blue SM-2322 Shoes Bought Sparx Navy Blue Sm-2322  Bought Sparx Navy Blue Sm-2322 ",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Grammerly",
                                "description": "Upgraded subscription from monthly to annual upgradedsubscription from monthly, ID,  Registration updated to premium which is annually charged. Registeration updated to Premium which is annually charged",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Flipcart",
                                "description": "Bought Sparx Navy Blue SM-2322 Shoes Bought Sparx Navy Blue Sm-2322  Bought Sparx Navy Blue Sm-2322 ",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            },
                            {
                                "title": "Subscription Payment-Grammerly",
                                "description": "Upgraded subscription from monthly to annual upgradedsubscription from monthly, ID,  Registration updated to premium which is annually charged. Registeration updated to Premium which is annually charged",
                                "image_url": "image_url",
                                "time": "04:21:33"
                            }
                                    ]
                            
                            }
                        }

     
            
        return apiData
    except Exception as e:
        print(e)
        return jsonify({
            "status": "Error",
            "message": "Something Went Wrong",
            "code": 500
        })
@app.route("/get_user_details", methods=["POST"])
def get_user_details():
    try:
        apiData = {
                    "code": 200,
                    "msg": "Success",
                    "status": "success",
                    "data": {
                        "keys": [
                            "contact_info",
                            "personal_info"
                                ],
                        "information": {
                            "contact_info": {
                                "email": "johnwick1@gmail.com",
                                "phone": "9898989898",
                                "address": "221b, Baker Street",
                                "city": "London"
                                            },
                            "personal_info": {
                                "work": "Software engineer",
                                "birthday": "22nd August 1980",
                                "age": "23",
                                "gender": "male"
                                        }
                                    }
                                }
                            }           
            
     
            
        return apiData
    except Exception as e:
        print(e)
        return jsonify({
            "status": "Error",
            "message": "Something Went Wrong",
            "code": 500
        })


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5002)
    app.run(debug=True, port=5002)
