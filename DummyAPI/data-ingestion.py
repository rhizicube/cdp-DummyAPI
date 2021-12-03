import datetime
from random import randrange, randint

import mysql.connector

start_date = datetime.date(2008, 1, 1)
end_date = datetime.date(2020, 1, 1)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YasMys@1",
    database="nc_cdp"
)

mycursor = db.cursor()

sql = """INSERT INTO `nc_cdp`.`customer_insights` (`date`, `customers`, `id_stitched_deterministic`,
        `id_Stitched_shared`, `data_points_ingested`, `data_points_exported`, `reachable_customers_email`, 
        `reachable_customers_sms`, `reachable_customers_apn`, `reachable_customers_wpn`) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

for i in range(1, 500):
    val = (start_date + datetime.timedelta(days=randrange(days_between_dates)), randint(0, 500), randint(0, 500),
           randint(0, 500), randint(0, 500),
           randint(0, 500), randint(0, 500), randint(0, 500), randint(0, 500), randint(0, 500))

    mycursor.execute(sql, val)

    db.commit()

print(mycursor.rowcount, "record inserted.")
