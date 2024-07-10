
##################### GET VALUES #######################################

@app.route('/doc_booking_get_data', methods=['POST'])
def getting_doctor_data():
    specialization = request.json['doc_special']
    cur = mysql.connection.cursor()
    cur.execute("select Doctor_Name from Doctor_Specialization where Doctor_Specialization=%s", (specialization,))
    data = cur.fetchall()
    return jsonify(data)


################## GET VALUES WHEN WE PASS SINGLE VALUE #######################

@app.route("/get_booking_data", methods=["POST"])
def getting():

    PATIENT_ID = request.json["PATIENT_ID"]
    cur = mysql.connection.cursor()
    cur.execute("select * from MAB_BOOKING where PATIENT_ID = %s", (PATIENT_ID,))
    data = cur.fetchall()
    cur.execute("select * from  where PATIENT_ID = %s", (PATIENT_ID,))
    data = cur.fetchall()
    return jsonify(data)

