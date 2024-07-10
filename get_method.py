@app.route("/USER_SIGNUP",methods = ['GET','POST'])
def user_signup():
     if request.method=='POST':
        d=request.json
        USER_SIGNUP_ID=d['USER_SIGNUP_ID']
        USER_ID = d['USER_ID']
        USER_NAME = d['USER_NAME']
        USER_MAIL_ID=d['USER_MAIL_ID']
        USER_PHONE_NUMBER=d['USER_PHONE_NUMBER']
        USER_PASSWORD=d['USER_PASSWORD']
        USER_IP=d['USER_IP']
        USER_DATE_CREATED=d['USER_DATE_CREATED']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO USER_SIGNUP(USER_SIGNUP_ID,USER_ID,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,USER_PASSWORD,USER_IP,USER_DATE_CREATED) VALUES( %s,%s,%s,%s,%s,%s,%s,%s)",(USER_SIGNUP_ID,USER_ID,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,USER_PASSWORD,USER_IP,USER_DATE_CREATED))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM USER_SIGNUP")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'