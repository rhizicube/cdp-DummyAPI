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

@app.route("/get_users_by_segment", methods=["POST"])
def get_users_by_segment():
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('cid')
        block_relation = req_obj.get('block_relation')
        condition_relation = req_obj.get('condition_relation')
        condition = req_obj.get('condition')
        data_type = req_obj.get('data_type')
        name = req_obj.get('name')
        value = req_obj.get('value')

        response = {
                        "code": 700,
                        "msg" : "Success" ,
                        "status" : "success" ,
                        "cid" : 100001,
                        "uid" : 559,
                        "data":[ 
                            {
                                "Uid": 15255, 
                                "CDP ID" : "cdp-1234321",
                                "SFSC ID" : "2873ghr87938rh",
                                "Name": "Abel aaberg",
                                "Email ID": "abelaaberg@gmail.com",
                                "Mobile No." : 8888812344,
                                "COuntry" : "United Arab Emirates"
                            },
                            {
                                "Uid": 15255, 
                                "CDP ID" : "cdp-1234322",
                                "SFSC ID" : "ewyd837648r3h",
                                "Name": "Abel aaberg",
                                "Email ID": "abelaaberg@gmail.com",
                                "Mobile No." : 8888812344,
                                "COuntry" : "United Arab Emirates"
                            }
                        ]
                    }
    except Exception as err:
        response = {
            "status" : "Error",
            "code" : 500,
            "status" : "Something Went Wrong"
                }

    print('get_users_by_segment response', response)
    return response


@app.route("/get_user_attributes", methods=["POST"])
def get_user_attributes():
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('cid')
        user_id = req_obj.get('uid')
    
        response = {
                "code": 700,
                "msg" : "Success" ,
                "status" : "success" ,
                "cid": 100001, 
                "uid": 5432, 
                "data" : { 
                    "direct_attrs": {
                    "name": "krishan", 
                    "age": "20"
                    },
                    "derived_attrs": {
                        "deterministic":{
                            "total_order_count": 100,
                            "total_order_value": 15780,
                            "average_order_value": 157.80,
                            "category_preference":"Books",
                            "product_preference":"Fiction"
                        },
                        "conflicting":{
                            "total_order_count": 150,
                            "total_order_value": 17780,
                            "average_order_value": 197.80
                        },
                       
                    }
                }
            }
    except Exception as err:
        print(err)
        response = {"status" : "Error",
                    "code" : 500,
                    "status" : "Something Went Wrong"
                }
            # response["status"] = "Error"
            # response["status"] = 500
            # response["message"] = "Wrong Client Id or User ID"
    #except Exception as err:
        #response  = {}
        # response["status"] = "Error"
        # response["status"] = 500
        # response["status"] = "Something Went Wrong"

    print('get_ids_count_by_client response', response)
    return response


@app.route("/get_products_by_event", methods=["POST"])
def get_products_by_event():
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('cid')
        user_id = req_obj.get('uid')
        #event_name = req.obj('event_name')
        #order_by_date = req.obj('order_by_date')
        #nrecs = req.obj('nrecs')
    
        response= {
                  "code": 200,
                  "msg" : "Success" ,
                  "status" : "success" ,
		          "client_id" : 100001,
		          "uid": 5432,
                  "data":{
                    "deterministic": [
                        { 
                            "pid":56544, 
                            "pname":"Veg-Pizza", 
                            "description":"This is a veg pizza", 
                            "purchase_date":"2021-11-21 13:34", 
                            "price": 100,
                            "image_url":"https://www.dominos.co.in/files/items/Farmhouse.jpg" 
                        }, 
                        { 
                           "pid":56545, 
                           "pname":"NVeg-Pizza", 
                           "description":"This is a non veg pizza", 
                           "purchase_date":"2021-11-11 13:34", 
                           "price":150,
                           "image_url":"https://www.dominos.co.in/files/items/Dominator.jpg" 
                        },
                        { 
                            "pid":56546, 
                            "pname":"Veg-Pizza", 
                            "description":"", 
                            "purchase_date":"2021-11-21 13:34", 
                            "price": 100,
                            "image_url":"https://www.dominos.co.in/files/items/Farmhouse.jpg" 
                        }, 
                        { 
                           "pid":56547, 
                           "pname":"NVeg-Pizza", 
                           "description":"", 
                           "purchase_date":"2021-11-11 13:34", 
                           "price":150,
                           "image_url":"https://www.dominos.co.in/files/items/Dominator.jpg" 
                        },
                        { 
                            "pid":56548, 
                            "pname":"Veg-Pizza", 
                            "description":"This is a veg pizza", 
                            "purchase_date":"2021-11-21 13:34", 
                            "price": 100,
                            "image_url":"https://www.dominos.co.in/files/items/Farmhouse.jpg" 
                        }, 
                        { 
                           "pid":56549, 
                           "pname":"NVeg-Pizza", 
                           "description":"This is a non veg pizza", 
                           "purchase_date":"2021-11-11 13:34", 
                           "price":150,
                           "image_url":"https://www.dominos.co.in/files/items/Dominator.jpg" 
                        },
                        { 
                            "pid":56550, 
                            "pname":"Veg-Pizza", 
                            "description":"This is a veg pizza", 
                            "purchase_date":"2021-11-21 13:34", 
                            "price": 100,
                            "image_url":"https://www.dominos.co.in/files/items/Farmhouse.jpg" 
                        }, 
                        { 
                           "pid":56551, 
                           "pname":"NVeg-Pizza", 
                           "description":"This is a non veg pizza", 
                           "purchase_date":"2021-11-11 13:34", 
                           "price":150,
                           "image_url":"https://www.dominos.co.in/files/items/Dominator.jpg" 
                        }
                        ], 
                    "conflicting": [
                        { 
                            "pid":56544, 
                            "pname":"Veg-Pizza", 
                            "description":"This is a veg pizza", 
                            "purchase_date":"2021-11-21 13:34", 
                            "image_url":"http://pizzahut-xyz.com/images/img1.png" 
                        }, 
                        { 
                           "pid":56545, 
                           "pname":"NVeg-Pizza", 
                           "description":"This is a non veg pizza", 
                           "purchase_date":"2021-11-11 13:34", 
                           "image_url":"http://pizzahut-xyz.com/images/img2.png" 
                        }
                    ]
                }
            }
    except Exception as err:
        print(err)
        response = {
            "status" : "Error",
            "code" : 500,
            "status" : "Something Went Wrong"
                }

    print('get_products_by_event response', response)
    return response

#changes in here
@app.route("/get_user_count_by_client", methods=["POST"])
def get_user_count_by_client ():
    try:
        print(request.headers)
        req_obj = request.get_json()
        print(req_obj)
        client_id = req_obj.get('cid')
        group_by= req_obj.get('group_by')
        nrecs = req_obj.get('nrecs')
    
        response = {
                    "code": 200,
                    "msg" : "Success" ,
                    "status" : "success" ,
                    "data":{ 
                        "value": 1100000, 
                        "group_values": { 
                            "12-2021": 100000, 
                            "11-2021": 280000, 
                            "10-2021": 160000, 
                        } 
                    }
                }
    except Exception as err:
        print(err)
        response = {"status" : "Error",
                    "code" : 500,
                    "status" : "Something Went Wrong"
                }
    print('get_user_count_by_client response', response)
    return response
#ends here


@app.route("/get_identifier_count_by_client",methods=["POST"])
def get_identifier_count_by_client():
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('cid')
        response = {
                    "code": 700,
                    "msg" : "Success" ,
                    "status" : "success" ,
                    "data":{ 
                        "deterministic":{
                            "value": 1100000, 
                            "group_values": { 
                                "12-2021": 100000, 
                                "11-2021": 280000, 
                                "10-2021": 160000, 
                                    } 
                                }, 
                                "conflicting":{ 
                                    "value": 1200000, 
                                    "group_values": { 
                                        "12-2021": 120000, 
                                        "11-2021": 290000, 
                                        "10-2021": 190000,
                                        } 
                                    } 
                            }
                        }
    except Exception as err:
        response = {"status" : "Error",
                    "code" : 500,
                    "status" : "Something Went Wrong"
                }

    print('get_identifier_count_by_client response', response)
    return response


@app.route("/get_identifiers_by_user", methods=["POST"])
def get_identifiers_by_user():
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('cid')
        user_id = req_obj.get('uid')
        response= {
                "code": 700,
                "msg" : "Success" ,
                "status" : "success" ,
                "data":{
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
            }
    except Exception as err:
        print(err)
        response = {"status" : "Error",
                    "code" : 500,
                    "status" : "Something Went Wrong"
                }

    print('get_identifiers_by_user response', response)
    return response


@app.route("/get_events_by_user", methods=["POST"])
def get_events_by_user():
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('cid')
        user_id = req_obj.get('uid')
        response = {
            "code": 700,
            "msg" : "Success" ,
            "status" : "success" ,
            "client_id" : 100001,
            "data" : {                    
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
    except Exception as err:
        print(err)
        response = {"status" : "Error",
                    "code" : 500,
                    "status" : "Something Went Wrong"
                }

    print('get_events_by_user response', response)
    return response


@app.route("/get_group_counts_by_user", methods=["POST"])
def get_group_counts_by_user():
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('cid')
        user_id = req_obj.get('uid')
        da_name = req_obj.get('da_name')
        group_by = req_obj.get('group_by')
        if da_name == "revenue" and group_by.lower() in ["year","day","quarter","month"]:
            response = {                    
                    "code": 700,
                    "msg" : "Success" ,
                    "status" : "success" ,
                    "client_id" : 100001,
                    "User ID" : 5432,
                    "data" : {
                        "values" : 370000,
                        "group_values" : {
                            "2010" : 40000,
                            "2011" : 40000,
                            "2012" : 22000,
                            "2013" : 31000,
                            "2014" : 25000,
                            "2015" : 25000,
                            "2016" : 30000,
                            "2017" : 38000,
                            "2018" : 40000,
                            "2019" : 22000,
                            "2020" : 32000,
                            "2021" : 25000
                        }
                    }
                    
                    
                }
        elif da_name == "revenue" and group_by.lower() == "category":
            response= {
                    "code": 700,
                    "msg" : "Success" ,
                    "status" : "success" ,
                    "client_id" : 100001,
                    "data" : {                   
                        "values" : 582,
                        "group_values" : {
                            "1st Jan 2013 12AM" : 130,
                            "1st Jan 2016 12AM" : 53,
                            "1st Jan 2019 12AM" : 184,
                            "1st Jan 2070 12AM" : 180,
                            "1st Jan 2070 12AM" : 35
                        }
                    }
                }
        elif da_name == "revenue" and group_by.lower() == "product":
            response = {
                "code": 700,
                "msg" : "Success" ,
                "status" : "success" ,
                "client_id" : 100001,
                "data" : {                     
                    "values" : 370000,
                    "group_values" : {
                        "key1" : 646,
                        "key2" : 983,
                        "key3" : 132
                    }
                }
            }
        elif da_name == "revenue" and group_by.lower() == "channel":
            response = {
                "code": 700,
                "msg" : "Success" ,
                "status" : "success" ,
                "client_id" : 100001,
                "data" : {                     
                    "values" : 370000,
                    "group_values" : {
                        "key1" : 446,
                        "key2" : 133,
                        "key3" : 464
                    }
                }
            }
        elif da_name == "revenue" and group_by.lower() == "order":
            response = {
                "code": 700,
                "msg" : "Success" ,
                "status" : "success" ,
                "client_id" : 100001,
                "data" : {                     
                    "values" : 370000,
                    "group_values" : {
                        "key1" : 446,
                        "key2" : 133,
                        "key3" : 464
                    }
                }
            }
        elif da_name == "product" and group_by.lower() == "category":
            response = {
                "code": 700,
                "msg" : "Success" ,
                "status" : "success" ,
                "client_id" : 100001,
                "data" : {                    
                    "values" : 75000,
                    "group_values" : {
                        "Mobile and Computers" : 7.5,
                        "Tv, Appliances, Electronics" : 7.5,
                        "Fashion" : 7.5,
                        "2013" : 7.5,
                        "Home,Kitchen,Pets" : 7.5,
                        "Beauty Health Grocery" : 7.5,
                        "Sports Fitness Bags Luggages" : 7.5,
                        "Toy's Baby Products Kid's Fashion" : 7.5,
                        "Cars Motorbike Industrial" : 7.5,
                        "Books" : 7.5,
                        "Others" : 7.5,
                        "2021" : 7.5
                    }
                }
            }
        elif da_name == "product" and group_by.lower() == "product":
            response = {
                "code": 700,
                "msg" : "Success" ,
                "status" : "success" ,
                "client_id" : 100001,
                "data" : {                    
                    "values" : 7500,
                    "group_values" : {
                        "Mobile and Computers" : 7.5
                    }
                }
            }
    except Exception as err:
        print(err)
        response = {"status" : "Error",
                    "code" : 500,
                    "status" : "Something Went Wrong"
                }

    print('get_group_counts_by_user response', response)
    return response


@app.route("/get_best_day_time", methods=["POST"])
def get_best_day_time():
    try:
        req_obj = request.get_json()
        client_id = req_obj.get('cid')
        user_id = req_obj.get('uid')
        
        response = {
                "code": 700,
                "msg" : "Success" ,
                "status" : "success" ,
                "client_id" : 100001,
                "data" : {
                    "users_id" : 5432,
                    "day" : "Friday",
                    "time_Window" : "15:24:10 PM - 15:34:52 PM"
                }
        }
    except Exception as err:
        print(err)
        response = {
            "status" : "Error",
            "code" : 500,
            "status" : "Something Went Wrong"
                }

    print('get_best_day_time response', response)
    return response


#My code Ends here


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5002)
    app.run(debug=True,host="0.0.0.0", port=1234)
