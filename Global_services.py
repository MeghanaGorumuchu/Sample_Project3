from datetime import datetime
import logging
import re
import socket
from faker import Faker
import MySQLdb
from flask import Flask, request, jsonify, session
from flask_mysqldb import MySQL
from werkzeug.routing import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['MYSQL_HOST'] = '35.213.140.165'
app.config['MYSQL_USER'] = 'uwgwdvoi7jwmp'
app.config['MYSQL_PASSWORD'] = 'Clinicalfirst@123'
app.config['MYSQL_0DB'] = 'dbim4u0mfuramq'
app.config['SECRET_KEY'] = 'secret_key'

mysql = MySQL(app)


# @app.route('/PWC_SERVICES', methods=['POST'])
# def pwc_service():
#     if 'PWC_SERVICE_TYPE' in request.json:
#         pwc_service_name = request.json["PWC_SERVICE_TYPE"]
#
#         cursor = mysql.connection.cursor()
#         PWC_SERVICE_ID = max_value(cursor)
#         try:
#             cur = mysql.connection.cursor()
#             cur.execute("insert into PWC_SERVICES(PWC_SERVICE_ID,PWC_SERVICE_TYPE) VALUES(%s, %s)",
#                         (PWC_SERVICE_ID, pwc_service_name))
#             mysql.connection.commit()
#             return "successfully inserted", 200
#         except ValidationError as e:
#             print(e)
#         return jsonify(e.messages)
#     return "invalid parameters",


# def max_value(c):
#     max_value_query = "SELECT substring(MAB_ID,6) as id FROM MAB_SERVICES WHERE substring(MAB_ID," \
#                       "6)=(SELECT MAX(CAST(SUBSTRING(MAB_ID,6) AS SIGNED)) FROM MAB_SERVICES)"
#     c.execute(max_value_query)
#     result_value = c.fetchone()
#     if result_value == 0 or result_value == 'None' or result_value == '' or result_value is None:
#         result_value = 1;
#         MAB_ID = 'MAB000' + str(result_value)
#         return MAB_ID
#     else:
#         result_value = int(result_value[0]) + 1
#         MAB_ID = 'MAB000' + str(result_value)
#         return MAB_ID

# @app.route('/MAB_SERVICES', methods=['POST'])
# def mab_service():
#     if 'MAB_SERVICE_TYPE' in request.json:
#         mab_service_name = request.json["MAB_SERVICE_TYPE"]
#
#         cursor = mysql.connection.cursor()
#         MAB_ID = max_value(cursor)
#         try:
#             cur = mysql.connection.cursor()
#             cur.execute("insert into MAB_SERVICES(MAB_ID,MAB_SERVICE_TYPE) VALUES(%s, %s)",
#                         (MAB_ID, mab_service_name))
#             mysql.connection.commit()
#             return "successfully inserted", 200
#         except ValidationError as e:
#             print(e)
#         return jsonify(e.messages)
#     return "invalid parameters",

def max_id_value(c):
    max_value_query = "SELECT substring(patient_id,6) as id FROM PATIENT_SIGNUP WHERE substring(patient_id," \
                      "6)=(SELECT MAX(CAST(SUBSTRING(patient_id,6) AS SIGNED)) FROM PATIENT_SIGNUP) "
    c.execute(max_value_query)
    result_value = c.fetchone()
    if result_value == 0 or result_value == 'None' or result_value == '' or result_value is None:
        result_value = 1
        patient_id = 'PA000' + str(result_value)
        return patient_id
    else:
        result_value = int(result_value[0]) + 1
        patient_id = 'PA000' + str(result_value)
        return patient_id

@app.route('/patient_signup', methods=['POST','GET'])
def signup():
    if 'patient_name' in request.json and 'email' in request.json and 'phn_number' in request.json\
       and 'password' in request.json :
        cursor = mysql.connection.cursor()
        patient_id = max_id_value(cursor)
        post_man = request.json
        name = post_man['patient_name']
        mail = post_man['email']
        phone_number = post_man['phn_number']
        patient_password = post_man['password']
        hashed_password = generate_password_hash(patient_password)
        ex = Faker()
        ip = ex.ipv4()
        device = socket.gethostname()
        date=datetime.today()

        #cursor:
        cursor.execute('SELECT * FROM PATIENT_SIGNUP WHERE (PATIENT_MAIL_ID =%s OR PATIENT_PHONE_NUMBER = %s)',\
             (mail,phone_number))
        account = cursor.fetchone()

        if account and account['PATIENT_MAIL_ID'] == mail:
            msg = 'your mail_id already exit please enter new mail_id'
        elif account and account['PATIENT_PHONE_NUMBER'] == phone_number:
            msg = 'phn number alredy exit please enter new phone number'

        elif not re.match(r'[^@]+@[^@]+\.[^@]+', mail):
            msg = ' mail id must contain @ domain name !'

        elif not re.match(r'[A-Za-z]+', name):
            msg = 'Username must contain only characters !'

        elif not re.match(r'^[A-Za-z0-9@#$%^&+=]{8,32}', patient_password):
            msg = 'Password must contain alpha_number with special_characters !'

        elif not re.match(r'^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$', phone_number):
            msg = ' phone number must contain ten digits, must starts with 9 or 8 or 7 and starts with +91 !'

        elif not re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                          ip):
            msg = 'Invalid ip address format !'

            # elif not re.match(r'^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$', date):
            #     msg = ' date format start with year, month and date !'

        elif not name or not patient_password or not mail or not phone_number or not ip or not date:
            msg = 'Please fill out the form !'
        else:
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute(
                "insert into PATIENT_SIGNUP (PATIENT_ID,PATIENT_NAME,PATIENT_MAIL_ID,PATIENT_PHONE_NUMBER,"
                "PATIENT_PASSWORD,PATIENT_IP,"
                "PATIENT_DEVICE, PATIENT_DATE_CREATED) values (%s,%s,%s,%s,%s,%s,%s,%s)",
                (patient_id,name, mail, phone_number, hashed_password, ip, device, date))
            mysql.connection.commit()

            # details = cur.fetchall()
            logging.info("successfully registered")
            return" successfully inserted",200
        return msg
    return "invalid parameters"

@app.route('/patient_login', methods=['POST'])
def login():
    if 'email' in request.json and 'password' in request.json:
        mail = request.json['email']
        pw = request.json['password']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("select * from PATIENT_SIGNUP where (PATIENT_MAIL_ID =%s)",(mail,))
        details = cur.fetchone()
        if details is None:
            return({"message":"No Details"}), 401
        # if details and details["PATIENT_MAIL_ID"]! = email:
        #      return "invalid email"
        hashed_password = details["PATIENT_PASSWORD"]
        password_match = check_password_hash(hashed_password, pw)
        if password_match:
            session['PATIENT_ID'] = details['PATIENT_ID']
            return "successfully login"
        else:
            return "invalid credentials"
    return "insufficient parameters", 400


@app.route('/get_method', methods=['GET'])
def get_method():
    try:
        cur = mysql.connection.cursor()
        cur.execute('select * from PATIENT_SIGNUP')
        data = cur.fetchall()
        if data is None:
            return "no details in your data"
        return jsonify(data)
    except:
        return jsonify({"message":"No data"})




@app.route('/mab_booking', methods=['POST'])
def mab_booking():
    if "location" in request.json and "price" in request.json and "MAB_SERVICE_TYPE" in request.json:
        date = datetime.today()
        location = request.json['location']
        price = request.json['price']
        mab_service= request.json['MAB_SERVICE_TYPE']
        id = session['PATIENT_ID']
        try:
            cur = mysql.connection.cursor()
            cur.execute("select MAB_ID from mab_services where MAB_SERVICE_TYPE=%s",(mab_service,))
            details = cur.fetchone()
            if details is None:
                return "no details"
            cur = mysql.connection.cursor()
            cur.execute("insert into mab_baby_booking(MAB_B_ID,PATIENT_ID, DATE, LOCATION,PRICE)"
                        "values(%s,%s,%s,%s,%s)",(details, id, date, location, price))
            mysql.connection.commit()
            return "success"
        except ValidationError as e:
            print(e)
            return jsonify(e.messages)
    return "invalid parameters"


@app.route('/pwc_booking', methods=['POST'])
def pwc_booking():
    if 'PWC_SERVICE_TYPE' in request.json and 'location' in request.json  and 'price' in request.json:

        date = datetime.today()
        location = request.json['location']
        price = request.json['price']
        pwc_service = request.json['PWC_SERVICE_TYPE']
        id = session['PATIENT_ID']
        try:
            cur = mysql.connection.cursor()
            cur.execute("select PWC_SERVICE_ID from PWC_SERVICES where PWC_SERVICE_TYPE=%s",(pwc_service,))
            details = cur.fetchone()
            if details is None:
                return "no details"
            cur = mysql.connection.cursor()
            cur.execute("insert into PWC_BOOKING(PATIENT_ID,PWC_ID,LOCATION,PRICE,DATE)"
                        "values(%s,%s,%s,%s,%s)", (details, id, location, price, date))
            mysql.connection.commit()
            return 'success'
        except ValidationError as e:
            print(e)
            return jsonify(e.messages)
    return "invalid parameters"


if __name__ == "__main__":
    app.run(debug=True)
