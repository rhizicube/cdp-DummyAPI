from pprint import pprint as pp

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YasMys@1",
    database="nc_cdp"
)

from_date = '2008-05-25'
to_date = '2019-02-03'

query = f"""SELECT WEEK(date) AS temp_week, YEAR(date) AS temp_year, SUM(reachable_customers_email) as email_customers, SUM(reachable_customers_sms) AS sms_customers,
            SUM(reachable_customers_apn) AS apn_customers, SUM(reachable_customers_wpn) AS wpn_customers FROM customer_insights WHERE date
            BETWEEN '{from_date}' AND '{to_date}' GROUP BY temp_year, temp_week"""

mycursor = db.cursor(dictionary=True)

mycursor.execute(query)

myresult = mycursor.fetchall()

print(myresult)

data = []

for object in myresult:
    object['email_customers'] = int(object['email_customers'])
    object['sms_customers'] = int(object['sms_customers'])
    object['apn_customers'] = int(object['apn_customers'])
    object['wpn_customers'] = int(object['wpn_customers'])
    object['Week'] = f"Week {object['temp_week']}, {object['temp_year']}"
    data.append(object)

apiData = {
    "graph_type": "bar",
    "graph_layout": "vertical",
    "keys": ["email_customers", "sms_customers", "apn_customers", "wpn_customers"],
    "pivot": "month",
    "colors": ['#FBB65B', '#513551', '#de3163', 'grey'],
    "data": data
}

pp(apiData)
pp(len(apiData['data']))
