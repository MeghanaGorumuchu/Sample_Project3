from datetime import datetime, timedelta
import re
import MySQLdb
from flask import Flask, request, jsonify, session
import logging
import socket
from flask_mysqldb import MySQL
from werkzeug.routing import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from faker import Faker

app = Flask(__name__)

app.config['MYSQL_HOST'] = '35.213.140.165'
app.config['MYSQL_USER'] = 'uwgwdvoi7jwmp'
app.config['MYSQL_PASSWORD'] = 'Clinicalfirst@123'
app.config['MYSQL_DB'] = 'dbim4u0mfuramq'
app.config['SECRET_KEY'] = 'secret_key'


mysql = MySQL(app)


@app.route('/patient_signup', methods=['POST'])
def register():
    if 'patient_name' in request.json and 'password' in request.json \
            and 'email' in request.json and 'phone' in request.json:

        cursor = mysql.connection.cursor()
        patient_id = max_id_value(cursor)
        patient_name = request.json['patient_name']
        email = request.json['email']
        phone = request.json['phone']
        password = request.json['password']
        hashed_password = generate_password_hash(password)
        ex = Faker()
        ip = ex.ipv4()
        print(ip)
        date = datetime.today()
        device = socket.gethostname()
        print(device)

        # Cursor:-

        cursor.execute('SELECT * FROM PATIENT_SIGNUP WHERE PATIENT_MAIL_ID = %s OR PATIENT_PHONE_NUMBER = %s',
                       (email, phone))
        account = cursor.fetchone()

        if account and account['PATIENT_MAIL_ID'] == email:
            msg = 'Your mail_id already exist please enter new mail_id  !!!!'

        elif account and account["PATIENT_PHONE_NUMBER"] == phone:
            msg = "Your phone number is duplicate please enter new number!!!"

        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = ' mail id must contain @ domain name !'

        elif not re.match(r'[A-Za-z]+', patient_name):
            msg = 'Username must contain only characters !'

        elif not re.match(r'^[A-Za-z0-9@#$%^&+=]{8,32}', password):
            msg = 'Password must contain alpha_number with special_characters !'

        elif not re.match(r'^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$', phone):
            msg = ' phone number must contain ten digits, must starts with 9 or 8 or 7 and starts with +91 !'

        elif not re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                          ip):
            msg = 'Invalid ip address format !'

        # elif not re.match(r'^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$', date):
        #     msg = ' date format start with year, month and date !'

        elif not patient_name or not password or not email or not phone or not ip or not date:
            msg = 'Please fill out the form !'

        else:
            cur = mysql.connection.cursor()
            cur.execute(
                "insert into PATIENT_SIGNUP (PATIENT_ID, PATIENT_NAME, PATIENT_MAIL_ID, PATIENT_PHONE_NUMBER, "
                "PATIENT_PASSWORD, PATIENT_IP, "
                "PATIENT_DATE_CREATED, PATIENT_DEVICE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                (patient_id, patient_name, email, phone, hashed_password, ip, date, device))
            mysql.connection.commit()
            # details = cur.fetchall()
            logging.info("successfully registered")
            return "successfully inserted", 200
        return msg
    return "invalid parameters"


@app.route('/patient_login', methods=["POST"])
def login():
    if 'email' in request.json and 'password' in request.json:
        email = request.json["email"]
        logging.info('Admin logged in')
        pw = request.json["password"]
        logging.warning('Watch out!')
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("select * from PATIENT_SIGNUP WHERE (PATIENT_MAIL_ID = %s )", (email,))
        details = cur.fetchone()
        if details is None:
            return ({"message": "No details"}), 401
        # if details and details["PATIENT_MAIL_ID"]!= email:
        #     return "invalid mailid"
        hashed_password = details["PATIENT_PASSWORD"]
        password_match = check_password_hash(hashed_password, pw)
        if password_match:
            session['PATIENT_ID'] = details['PATIENT_ID']
            return "successfully login"
        else:
            logging.error("Invalid credentials")

        return ({"Error": "invalid credentials"}), 401

    return "Insufficient parameters", 400


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


@app.route('/mab_b_booking', methods=['POST'])
def mab_b_booking():
    if "location" in request.json and "price" in request.json and "MAB_B_SERVICE_TYPE" in request.json:
        date = datetime.today()
        location = request.json['location']
        price = request.json['price']
        mab_service = request.json['MAB_B_SERVICE_TYPE']
        id = session['PATIENT_ID']
        try:
            cur = mysql.connection.cursor()
            cur.execute("select MAB_B_ID from MAB_BABY_SERVICES where MAB_B_SERVICE_TYPE= %s", (mab_service,))
            details = cur.fetchone()
            if details is None:
                return "no details"
            cur = mysql.connection.cursor()
            cur.execute("insert into MAB_BOOKING(PATIENT_ID,MAB_SERVICE_ID, DATE, LOCATION,PRICE)"
                        "values(%s,%s,%s,%s,%s)", (id,details,  date, location, price))
            mysql.connection.commit()
            return "success"
        except ValidationError as e:
            print(e)
            return jsonify(e.messages)
    return "invalid parameters"


@app.route('/booking', methods=['POST','GET'])
def mab_booking():
    if 'MAB_SERVICE_TYPE' in request.json and 'location' in request.json and 'price' in request.json:
        date = datetime.today()
        location = request.json['location']
        price = request.json['price']
        mab_service = request.json['MAB_SERVICE_TYPE']
        id = session['PATIENT_ID']
        try:
            cur = mysql.connection.cursor()
            cur.execute("select MAB_M_ID from MAB_MOTHER_SERVICES where MAB_M_SERVICE_TYPE=%s", (mab_service,))
            details = cur.fetchone()
            if details is None:
                cur = mysql.connection.cursor()
                cur.execute("select MAB_B_ID from MAB_BABY_SERVICES where MAB_B_SERVICE_TYPE= %s", (mab_service,))
                details = cur.fetchone()
            cur = mysql.connection.cursor()
            cur.execute("insert into MAB_BOOKING(PATIENT_ID,MAB_SERVICE_ID, DATE, LOCATION,PRICE)"
                        "values(%s,%s,%s,%s,%s)", (id, details, date, location, price))
            mysql.connection.commit()
            return "success"
        except ValidationError as e:
            print(e)
            return jsonify(e.messages)
        return "invalid parameters"


@app.route('/mab_m_booking', methods=['POST'])
def mab_m_booking():
    if 'MAB_M_SERVICE_TYPE' in request.json and 'location' in request.json and 'price' in request.json:
        date = datetime.today()
        location = request.json['location']
        price = request.json['price']
        mab_service = request.json['MAB_M_SERVICE_TYPE']
        id = session['PATIENT_ID']
        try:
            cur = mysql.connection.cursor()
            cur.execute("select MAB_M_ID from MAB_MOTHER_SERVICES where MAB_M_SERVICE_TYPE=%s", (mab_service,))
            details = cur.fetchone()
            if details is None:
                return "no details"
            cur = mysql.connection.cursor()
            cur.execute("insert into MAB_BOOKING(PATIENT_ID,MAB_SERVICE_ID, DATE, LOCATION,PRICE)"
                        "values(%s,%s,%s,%s,%s)", (id, details,  date, location, price))
            mysql.connection.commit()
            return "success"
        except ValidationError as e:
            print(e)
            return jsonify(e.messages)
    return "invalid parameters"


@app.route('/pwc_booking', methods=['POST'])
def pwc_booking():
    if 'PWC_SERVICE_TYPE' in request.json and 'location' in request.json and 'price' in request.json:

        date = datetime.today()
        location = request.json['location']
        price = request.json['price']
        pwc_service = request.json['PWC_SERVICE_TYPE']
        id = session['PATIENT_ID']
        try:
            cur = mysql.connection.cursor()
            cur.execute("select PWC_SERVICE_ID from PWC_SERVICES where PWC_SERVICE_TYPE=%s", (pwc_service,))
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


if __name__ == '__main__':
    app.run(debug=True)
