@app.route('/REG_Disability', methods=['POST'])
def REG_Disability():
    DISABLED_STATUS = request.json['DISABLED_STATUS']
    AVAILABILITY = request.json['AVAILABILITY']
    cur = mysql.connection.cursor()
    cur.execute("select DISABLED_ID from DISABLED_PATIENT where DISABLED_STATUS=%s", (DISABLED_STATUS,))
    dataa = cur.fetchone()
    cur.execute("select CERTIFICATE_ID from DISABILITY_CERTIFICATE where AVAILABILITY=%s", (AVAILABILITY,))
    data = cur.fetchone()
    if "CER001" in data:
        CERTIFICATE_NUMBER = request.json['CERTIFICATE_NUMBER']
        ISSUE_DATE = request.json['ISSUE_DATE']
        DISABILITY_PERCENTAGE = request.json['DISABILITY_PERCENTAGE']
        AUTHORITY_NAME = request.json['AUTHORITY_NAME']
        cur.execute("select AUTHORITY_ID from DISABILITY_ISSUING_AUTHORITY where AUTHORITY_NAME=%s",
                    (AUTHORITY_NAME,))
        data1 = cur.fetchone()
        DISABILITY_TYPE_NAME = request.json['DISABILITY_TYPE_NAME']
        cur.execute("select DISABILITY_TYPE_ID from DISABILITY_TYPE where DISABILITY_TYPE_NAME=%s",
                    (DISABILITY_TYPE_NAME,))
        data2 = cur.fetchone()

        STATUS = request.json['STATUS']
        cur.execute("select DISABILITY_BY_BIRTH_ID from DISABILITY_BY_BIRTH where STATUS=%s", (STATUS,))
        data3 = cur.fetchone()

        if 'DBID001' in data3:
            PENSIONCARD_NUMBER = request.json['PENSIONCARD_NUMBER']
            DISABILITY_AREA_NAME = request.json['DISABILITY_AREA_NAME']
            cur.execute("select DISABILITY_AREA_ID from DISABILITY_AREA where DISABILITY_AREA_NAME=%s",
                        (DISABILITY_AREA_NAME,))
            data4 = cur.fetchone()
            DISABILITY_DUE_NAME = request.json['DISABILITY_DUE_NAME']
            cur.execute("select DISABILITY_DUE_ID from DISABILITY_DUE_TO where DISABILITY_DUE_NAME=%s",
                        (DISABILITY_DUE_NAME,))
            data5 = cur.fetchone()
            DISABILITY_SCHEME = request.json['DISABILITY_SCHEME']
            cur.execute(
                "insert into REG_DISABILITY_DETAILS(DISABLED_ID,CERTIFICATE_ID,CERTIFICATE_NUMBER,ISSUE_DATE,"
                "DISABILITY_PERCENTAGE,DETAILS_OF_ISSUING_AUTHORITY,DISABILITY_TYPE_ID,DISABILITY_BY_BIRTH_ID,"
                "PENSIONCARD_NUMBER,DISABILITY_AREA_ID,DISABILITY_DUE_TO,DISABILITY_SCHEME)"
                " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (dataa, data, CERTIFICATE_NUMBER, ISSUE_DATE,
                                                                 DISABILITY_PERCENTAGE, data1, data2, data3,
                                                                 PENSIONCARD_NUMBER, data4, data5,
                                                                 DISABILITY_SCHEME))
            mysql.connection.commit()
            return "SUCCESS"
        else:
            cur.execute(
                "insert into REG_DISABILITY_DETAILS(DISABLED_ID,CERTIFICATE_ID,CERTIFICATE_NUMBER,ISSUE_DATE,"
                "DISABILITY_PERCENTAGE,DETAILS_OF_ISSUING_AUTHORITY,DISABILITY_TYPE_ID,DISABILITY_BY_BIRTH_ID)"
                " values(%s,%s,%s,%s,%s,%s,%s,%s)", (dataa, data, CERTIFICATE_NUMBER, ISSUE_DATE,
                                                     DISABILITY_PERCENTAGE, data1, data2, data3))
            mysql.connection.commit()
            return 'successfully inserted values'
    else:
        STATUS = request.json['STATUS']
        cur.execute("select DISABILITY_BY_BIRTH_ID from DISABILITY_BY_BIRTH where STATUS=%s", (STATUS,))
        data3 = cur.fetchone()
        if 'DBID001' in data3:
            PENSIONCARD_NUMBER = request.json['PENSIONCARD_NUMBER']
            DISABILITY_AREA_NAME = request.json['DISABILITY_AREA_NAME']
            cur.execute("select DISABILITY_AREA_ID from DISABILITY_AREA where DISABILITY_AREA_NAME=%s",
                        (DISABILITY_AREA_NAME,))
            data4 = cur.fetchone()
            DISABILITY_DUE_NAME = request.json['DISABILITY_DUE_NAME']
            cur.execute("select DISABILITY_DUE_ID from DISABILITY_DUE_TO where DISABILITY_DUE_NAME=%s",
                        (DISABILITY_DUE_NAME,))
            data5 = cur.fetchone()
            DISABILITY_SCHEME = request.json['DISABILITY_SCHEME']
            cur.execute(
                "insert into REG_DISABILITY_DETAILS(DISABLED_ID,CERTIFICATE_ID,CERTIFICATE_NUMBER,PENSIONCARD_NUMBER,DISABILITY_AREA_ID,"
                "DISABILITY_DUE_TO,DISABILITY_SCHEME) values(%s,%s,%s,%s,%s,%s,%s)",
                (dataa, data, data3, PENSIONCARD_NUMBER, data4, data5, DISABILITY_SCHEME))
            mysql.connection.commit()
            return "SUCCESS"

    cur.execute("insert into REG_DISABILITY_DETAILS(DISABLED_ID,CERTIFICATE_ID)"
                " values(%s,%s)", (dataa, data,))
    mysql.connection.commit()
    return 'successfully inserted values without disability'