import MySQLdb
from flask import Flask, request, jsonify, session
from flask_mysqldb import MySQL
from werkzeug.routing import ValidationError

app = Flask(__name__)
app.config['MYSQL_HOST'] = '35.213.140.165'
app.config['MYSQL_USER'] = 'uwgwdvoi7jwmp'
app.config['MYSQL_PASSWORD'] = 'Clinicalfirst@123'
app.config['MYSQL_DB'] = 'dbim4u0mfuramq'
mysql = MySQL(app)


            ################################## PATIENT_PERSONAL_DETAILS ######################################

@app.route('/REG_Patient_Personal', methods=['POST'])
def personal():
    if request.method == 'POST':
        user = request.json
        pat_name = user['PATIENT_NAME']
        pat_phone = user['PATIENT_PHONE_NUMBER']
        alt_phn_number = user['ALTERNATIVE_PHONE_NUMBER']
        email = user['EMAIL_ADDRESS']
        password = user['PASSWORD']
        address = user['ADDRESS']
        dob = user['DOB']
        age = user['AGE']
        gender = user['GENDER']
        marital_status = user['MARITAL_STATUS']
        spouse_name = user['SPOUSE_NAME_IF_MARRIED']
        spouse_phone = user['SPOUSE_PHONE_NUMBER']
        patient_employer = user['PATIENTS_EMPLOYER']
        employ_status = user['EMPLOYMENT_STATUS']
        emp_id = user['EMPLOY_ID']
        body_temp = user['BODY_TEMPERATURE']
        blood_pressure = user['BLOOD_PRESSURE']
        ht = user['HEIGHT']
        wt = user['WEIGHT']
        diabetes = user['DIABETES']
        blood_group = user['BLOOD_GROUP']
        transfused = user['TRANSFUSED_IN_LAST_3MONTHS']
        emer_cont_name = user['EMERGENCY_CONTACT_NAME']
        relation_to_patient = user['RELATION_TO_PATIENT']
        emer_cont_address = user['EMERGENCY_CONT_ADDRESS']
        emer_cont_phone = user['EMERGENCY_PHONE_NUMBER']
        cur = mysql.connection.cursor()
        cur.execute('insert into REG_PATIENT_PERSONAL_DETAILS(PATIENT_NAME,PATIENT_PHONE_NUMBER,'
                    'ALTERNATIVE_PHONE_NUMBER,EMAIL_ADDRESS,PASSWORD,ADDRESS,DOB,AGE,GENDER,MARITAL_STATUS,'
                    'SPOUSE_NAME_IF_MARRIED,SPOUSE_PHONE_NUMBER,PATIENTS_EMPLOYER,EMPLOYMENT_STATUS,EMPLOY_ID,'
                    'BODY_TEMPERATURE,BLOOD_PRESSURE,HEIGHT,WEIGHT,DIABETES,BLOOD_GROUP,TRANSFUSED_IN_LAST_3MONTHS,'
                    'EMERGENCY_CONTACT_NAME,RELATION_TO_PATIENT,EMERGENCY_CONT_ADDRESS,EMERGENCY_PHONE_NUMBER) '
                    'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (pat_name, pat_phone, alt_phn_number, email, password, address, dob, age, gender,
                     marital_status, spouse_name, spouse_phone, patient_employer,
                     employ_status, emp_id, body_temp, blood_pressure, ht, wt, diabetes,
                     blood_group, transfused, emer_cont_name, relation_to_patient,
                     emer_cont_address, emer_cont_phone))
        mysql.connection.commit()

        return 'data inserted successfully'

                       ####################### PATIENT_FAMILY_DETAILS ##########################


@app.route('/patient/details', methods=["POST"])
def patient_details():
    if 'logged' in session:
        data = request.json
        if 'PATIENTS_FAMILY_MEMBERS' in data and \
            'FAMILY_MEMBER_1' in data and \
            'DATE_OF_BIRTH_1' in data and \
            "RELATION_TO_THE_PATIENT_1" in data and \
            'FAMILY_MEMBER_2' in data and \
            'DATE_OF_BIRTH_2' in data and \
            "RELATION_TO_THE_PATIENT_2" in data and \
            'FAMILY_MEMBER_3' in data and \
            'DATE_OF_BIRTH_3' in data and \
            "RELATION_TO_THE_PATIENT_3" in data and \
            'FAMILY_MEMBER_4' in data and \
            'DATE_OF_BIRTH_4' in data and \
            "RELATION_TO_THE_PATIENT_4" in data and \
            "BODY_TEMPERATURE" in data and \
            "BLOOD_PRESSURE" in data and \
            "HEIGHT" in data and \
            "WEIGHT" in data and \
            "DIABETES" in data and \
            "BLOOD_GROUP" in data and \
            "TRANSFUSED" in data and \
            "NAME" in data and \
            "RELATION_TO_THE_PATIENT_5" in data and \
            "ADDRESS" in data and \
            "PHONE_NUMBER" in data:
            # Variables
            PATIENT_ID = session['PATIENT_ID']
            #PATIENTS_FAMILY_MEMBERS = data['PATIENTS_FAMILY_MEMBERS']
            FAMILY_MEMBER_1 = data['FAMILY_MEMBER_1']
            DATE_OF_BIRTH_1 = data['DATE_OF_BIRTH_1']
            RELATION_TO_THE_PATIENT_1 = data['RELATION_TO_THE_PATIENT_1']
            FAMILY_MEMBER_2 = data['FAMILY_MEMBER_2']
            DATE_OF_BIRTH_2 = data['DATE_OF_BIRTH_2']
            RELATION_TO_THE_PATIENT_2 = data['RELATION_TO_THE_PATIENT_2']
            FAMILY_MEMBER_3 = data['FAMILY_MEMBER_3']
            DATE_OF_BIRTH_3 = data['DATE_OF_BIRTH_3']
            RELATION_TO_THE_PATIENT_3 = data['RELATION_TO_THE_PATIENT_3']
            FAMILY_MEMBER_4 = data['FAMILY_MEMBER_4']
            DATE_OF_BIRTH_4 = data['DATE_OF_BIRTH_4']
            RELATION_TO_THE_PATIENT_4 = data['RELATION_TO_THE_PATIENT_4']
            BODY_TEMPERATURE = data['BODY_TEMPERATURE']
            BLOOD_PRESSURE = data['BLOOD_PRESSURE']
            HEIGHT = data['HEIGHT']
            WEIGHT = data['WEIGHT']
            DIABETES = data['DIABETES']
            BLOOD_GROUP = data['BLOOD_GROUP']

            TRANSFUSED = data['TRANSFUSED']

            NAME = data['NAME']
            RELATION_TO_THE_PATIENT_5 = data['RELATION_TO_THE_PATIENT_5']
            ADDRESS = data['ADDRESS']
            PHONE_NUMBER = data['PHONE_NUMBER']

            try:
                cur = mysql.connection.cursor()
                cur.execute(
                    "insert into PATIENT_FAMILY_DETAILS(PATIENT_ID, FAMILY_MEMBER_1, DATE_OF_BIRTH_1,"
                    "RELATION_TO_THE_PATIENT_1, FAMILY_MEMBER_2, DATE_OF_BIRTH_2, RELATION_TO_THE_PATIENT_2,"
                    " FAMILY_MEMBER_3, DATE_OF_BIRTH_3, RELATION_TO_THE_PATIENT_3,"
                    " FAMILY_MEMBER_4, DATE_OF_BIRTH_4, RELATION_TO_THE_PATIENT_4)"
                    "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (PATIENT_ID, FAMILY_MEMBER_1, DATE_OF_BIRTH_1, RELATION_TO_THE_PATIENT_1,
                     FAMILY_MEMBER_2, DATE_OF_BIRTH_2, RELATION_TO_THE_PATIENT_2,
                     FAMILY_MEMBER_3, DATE_OF_BIRTH_3, RELATION_TO_THE_PATIENT_3,
                     FAMILY_MEMBER_4, DATE_OF_BIRTH_4, RELATION_TO_THE_PATIENT_4))
                cur.execute(
                    "insert into GENERAL_HEALTH_CHECKUP(BODY_TEMPERATURE, BLOOD_PRESSURE, HEIGHT, WEIGHT, "
                    "DIABETES, BLOOD_GROUP, PATIENT_ID)"
                    "values(%s, %s, %s, %s, %s, %s, %s)",
                    (BODY_TEMPERATURE, BLOOD_PRESSURE, HEIGHT, WEIGHT, DIABETES, BLOOD_GROUP, PATIENT_ID))
                cur.execute("insert into TRANSFUSED(TRANS_LAST_3_MONTHS, PATIENT_ID)"
                            "values(%s, %s)", (TRANSFUSED, PATIENT_ID))
                cur.execute(
                    "insert into EMERGENCY_CONTACT(NAME, RELATION_TO_THE_PATIENT, ADDRESS, PHONE__NUMBER, PATIENT_ID)"
                    "values(%s, %s, %s, %s, %s)",
                    (NAME, RELATION_TO_THE_PATIENT_5, ADDRESS, PHONE_NUMBER, PATIENT_ID))
                mysql.connection.commit()
                return "Successfully Inserted All Details", 200
            except ValidationError as e:
                print(e)
            return jsonify(e.messages)
        return "invalid parameters"
    return "User not logged in, please login first"

              ######################################## DISABILITY #############################################


@app.route('/REG_Disability', methods=['POST'])
def REG_Disability():
    DISABLED_STATUS = request.json['DISABLED_STATUS']
    AVIALABILITY = request.json['AVIALABILITY']

    cur = mysql.connection.cursor()
    cur.execute("select DISABLED_ID from DISABLED_PATIENT where DISABLED_STATUS=%s", (DISABLED_STATUS,))
    dataa = cur.fetchone()

    cur.execute("select CERTIFICATE_ID from DISABILITY_CERTIFICATE where AVIALABILITY=%s", (AVIALABILITY,))
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

    cur.execute("insert into REG_DISABILITY_DETAILS(DISABLED_ID,CERTIFICATE_ID)"
                " values(%s,%s)", (dataa, data,))
    mysql.connection.commit()
    return 'successfully inserted values without disability'

                         ####################################### ORGAN #################################


@app.route('/REG_Organ', methods=["POST", "GET"])
def Organ_Transplant():
    if request.method == 'POST':
        Procedure_Name = request.json['Procedure_type_name']
        ORGAN = request.json['ORGAN_NAME']
        Complication = request.json['Complication_type_name']
        Med = request.json['Medication']
        Des = request.json['Description']
        cur = mysql.connection.cursor()
        cur.execute("select Procedure_type_ID from REMOVAL_OR_TRANSPLANTATION_OF_ANY_ORGAN "
                    "where Procedure_type_name=%s", (Procedure_Name,))
        abc = cur.fetchone()
        if abc is None:
            return "Please enter correct speciality"
        cur.execute("select ORGAN_ID from ORGANS where ORGAN_NAME=%s", (ORGAN,))
        pqr = cur.fetchone()
        if pqr is None:
            return "please enter correct speciality"
        cur.execute(
            "select Complication_type_ID from ORGAN_COMPLICATIONS_TABLE where Complication_type_name=%s",
            (Complication,))
        xyz = cur.fetchone()
        x = "CRTO001"
        y = "CRTO002"
        if x in xyz:
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute(
                "insert into REG_REMOVAL_OR_TRANSPLANTATION_DETAILS "
                "(Procedure_,ORGAN,Complication,Medication,Description)VALUES(%s,%s,%s,%s,%s)",
                (abc, pqr, xyz, Med, Des))
            mysql.connection.commit()
            cur.close()
        elif y in xyz:
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute(
                "insert into REG_REMOVAL_OR_TRANSPLANTATION_DETAILS (Procedure_,ORGAN,Complication) "
                "VALUES(%s,%s,%s)", (abc, pqr, xyz))
            mysql.connection.commit()
            cur.close()
        mysql.connection.commit()
        cur.close()
        return 'Successfully Inserted'
    else:
        return "Unsuccessful"

                    ####################################### INSURANCE ############################################


@app.route('/REG_INSURANCE', methods=['POST'])
def REG_INSURANCE():
    if request.method == 'POST':
        # PATIENT_ID = session['PATIENT_ID']
        Primary_Insurance = request.json['Primary_Insurance']
        Primary_Insured_Name = request.json['Primary_Insured_Name']
        Primary_Policy_ID = request.json['Primary_Policy_ID']
        Secondary_Insurance = request.json['Secondary_Insurance']
        Secondary_Insured_Name = request.json['Secondary_Insured_Name']
        Secondary_Policy_ID = request.json['Secondary_Policy_ID']

        cur = mysql.connection.cursor()
        cur.execute('insert into REG_INSURANCE_DETAILS values(%s,%s,%s,%s,%s,%s)',
                    (Primary_Insurance, Primary_Insured_Name, Primary_Policy_ID, Secondary_Insurance,
                     Secondary_Insured_Name, Secondary_Policy_ID))
        mysql.connection.commit()
        return 'Insurance Details Inserted successful'
    else:
        return " Insurance Details Not Inserted"

                        ############################ PREGNANCY DETAILS ###############################


@app.route('/REG_Pregnancy_Details', methods=['POST'])
def Pregnancy_Details():
    if request.method == 'POST':
        u = request.json
        pregnant = u['pregnant']
        expected_date = u['expected_date']
        previous_live_births = u["previous_live_births"]
        date_of_delivery = u['date_of_delivery']
        type_of_delivery = u['type_of_delivery']
        lactation_status = u['lactation_status']
        feeding = u['breast_feeding_status']
        COMPLICATION_STATUS = u['COMPLICATION_STATUS']
        complication_name = u['complication_name']
        vaccination_name = u['vaccination_name']
        try:
            cur = mysql.connection.cursor()
            cur.execute("select PREVIOUS_PREGNANCY_COMPLICATION_ID from PREVIOUS_PREGNANCY_COMPLICATIONS where "
                        "COMPLICATION_STATUS = %s",
                        (COMPLICATION_STATUS,))
            data = cur.fetchone()

            if data is None:
                return "No Details"
            cur.execute("select COMPLICATION_ID from PREGNANCY_COMPLICATIONS where COMPLICATION_NAME =%s",
                        (complication_name,))
            data1 = cur.fetchone()

            cur.execute("select VACCINATION_ID from PREGNANCY_VACCINATIONS where VACCINATION_NAME= %s",
                        (vaccination_name,))
            data2 = cur.fetchone()
            cur.execute("select PATIENT_LACTATING_ID from PREGNANCY_PATIENT_LACTATING_WOMEN "
                        "where LACTATING_STATUS=%s",
                        (lactation_status,))
            data3 = cur.fetchone()
            cur.execute("select PATIENT_BREAST_FEEDING_ID from PREGNANCY_BREAST_FEEDING "
                        "where BREAST_FEEDING_STATUS=%s",
                        (feeding,))
            data4 = cur.fetchone()

            if "PPC001" in data:
                cur = mysql.connection.cursor()
                cur.execute("insert into REG_PREGNANCY_DETAILS "
                            "(PREGNANT,EXPECTED_DELIVERY_DATE,PREVIOUS_LIVE_BIRTHS,"
                            "PREVIOUS_PREGNANCY_COMPLICATION_ID,VACCINATION_ID,COMPLICATION_ID,"
                            "PATIENT_LACTATING_ID,DATE_OF_DELIVERY,TYPE_OF_DELIVERY,PATIENT_BREAST_FEEDING_ID)"
                            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (pregnant, expected_date, previous_live_births, data,
                             data2, data1, data3, date_of_delivery, type_of_delivery,
                             data4))
                mysql.connection.commit()
                return "Successful"
            else:
                cur = mysql.connection.cursor()
                cur.execute("insert into REG_PREGNANCY_DETAILS "
                            "(PREGNANT,EXPECTED_DELIVERY_DATE,PREVIOUS_LIVE_BIRTHS,"
                            "PREVIOUS_PREGNANCY_COMPLICATION_ID,VACCINATION_ID,"
                            "PATIENT_LACTATING_ID,DATE_OF_DELIVERY,TYPE_OF_DELIVERY,PATIENT_BREAST_FEEDING_ID)"
                            "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (pregnant, expected_date, previous_live_births, data,
                             data2, data3, date_of_delivery, type_of_delivery,
                             data4))
                mysql.connection.commit()
                return "Without Complication ID success"
        except ValidationError as e:
            print(e)
    return "invalid method"

                ##################################### VACCINATION ##########################################


@app.route('/VAC_Reg', methods=['POST'])
def VAC_Reg():
    if request.method == 'POST':
        YEARS = request.json['YEARS']
        VACCINE_NAME = request.json['VAC_NAME']
        try:
            cur = mysql.connection.cursor()
            cur.execute("select YEARS from VACCINATIONS where YEARS=%s", (YEARS,))
            data = cur.fetchone()

            cur.execute("select VACCINE_ID from VACCINATIONS  WHERE (YEARS=%s AND "
                        "VACCINE_NAME=%s)", (YEARS, VACCINE_NAME))
            data1 = cur.fetchone()

            Vaccinated = request.json['Vaccinated']
            cur.execute("select ID from COVID_VACCINE  WHERE (Vaccinated=%s)", (Vaccinated,))
            data2 = cur.fetchone()

            if "VC001" in data2:
                Dose = request.json['Dose']
                covid_vaccine_name = request.json['covid_vaccine_name']
                cur.execute("select ID from covid19_dose  WHERE (Dose=%s)", (Dose,))
                data3 = cur.fetchone()

                other_vaccine_name = request.json['other_vaccine_name']
                cur.execute("insert into REG_VAC_BOOKING"
                            "(ID,YEARS,VAC_NAME,VACCINATED,COVID_VAC_NAME,DOSE,OTHER_VAC_NAME)"
                            "values(null,%s,%s,%s,%s,%s,%s)",
                            (data, data1, data2, covid_vaccine_name, data3, other_vaccine_name))
                mysql.connection.commit()
            else:
                cur.execute("insert into REG_VAC_BOOKING(ID,YEARS,VAC_NAME,VACCINATED)"
                            "values(null,%s,%s,%s)", (data, data1, data2))
                mysql.connection.commit()
        except ValidationError as e:
            print(e)
            return 'Successfully inserted Records'
    return 'invalid Parameters'

                ################################### Previous_health_issues ########################


@app.route("/HEALTH_ISSUES", methods=["POST"])
def health_issues():
    if "logged" in session:
        if request.method == 'POST':
            data = request.json

            if "issue_name" in data and "TREATMENT_TAKEN_AT" in data and "SURGERIES" in data and \
                "COMPLICATIONS_DURING_TREATMENT" in data and "MEDICATIONS" in data and \
                "LIST_ANY_ALLERGIES_TO_MEDICATIONS" in data:

                PATIENT_ID = session['PATIENT_ID']

                issue_name = request.json["issue_name"]
                TREATMENT_TAKEN_AT = request.json["TREATMENT_TAKEN_AT"]
                SURGERIES = request.json['SURGERIES']
                COMPLICATIONS_DURING_TREATMENT = request.json['COMPLICATIONS_DURING_TREATMENT']
                MEDICATIONS = request.json['MEDICATIONS']
                LIST_ANY_ALLERGIES_TO_MEDICATIONS = request.json['LIST_ANY_ALLERGIES_TO_MEDICATIONS']

                try:
                    cur = mysql.connection.cursor()
                    HIS_NAME = request.json['HIS_NAME']
                    cur.execute("select HIS_ID from HEALTH_ISSUE  WHERE (HIS_NAME=%s)", (HIS_NAME,))
                    HIS_ID = cur.fetchone()
                    if "HIS001" in HIS_ID:
                        Yes = HIS_ID
                        cur.execute("select ISSUE_ID from HEALTH_ISSUES where (ISSUE_NAME = %s)",
                                    (issue_name,))
                        IssueName = cur.fetchone()
                        if IssueName is None:
                            return "No details in account"
                        # Txn Table
                        cur = mysql.connection.cursor()
                        cur.execute(
                            "insert into PREVIOUS_HEALTH_ISSUES(USER_ID, ISSUE_ID, TREATMENT_TAKEN_AT, SURGERIES, "
                            "COMPLICATIONS_DURING_TREATMENT, MEDICATIONS, LIST_ANY_ALLERGIES_TO_MEDICATIONS, "
                            "HEALTH_ISSUE) values(%s, %s, %s, %s, %s, %s, %s, %s)",
                            (PATIENT_ID, IssueName, TREATMENT_TAKEN_AT, SURGERIES, COMPLICATIONS_DURING_TREATMENT,
                             MEDICATIONS, LIST_ANY_ALLERGIES_TO_MEDICATIONS, Yes))
                        mysql.connection.commit()
                        return "Successfully Inserted with All Values", 200
                    else:
                        NO = 'HIS002'
                        cur.execute(
                            "insert into PREVIOUS_HEALTH_ISSUES(USER_ID, HEALTH_ISSUE) values(%s, %s)",
                            (PATIENT_ID, NO))
                        mysql.connection.commit()
                        return "successfully inserted with no condition"
                except ValidationError as e:
                    print(e)
                return jsonify(e.messages)
            return "invalid parameters"
        return "Method Not Found"
    return "User not logged in, please login first"

                            ##################################### EYE ######################################


@app.route('/REG_EYE', methods=['POST'])
def EYE_DISEASE():
    if request.method == 'POST':
        Disease = request.json['ED_TYPE_NAME']
        Symptom = request.json['SYMPTOM_NAME']
        cursor = mysql.connection.cursor()
        cursor.execute("select ED_TYPE_ID from PAT_HAS_EYE_DISEASE where ED_TYPE_NAME=%s", (Disease,))
        account = cursor.fetchone()
        h = "ED001"
        if h in account:
            cursor = mysql.connection.cursor()
            cursor.execute("select SYMPTOM_ID from EYE_DISEASE_SYMPTOMS where SYMPTOM_NAME=%s", (Symptom,))
            account1 = cursor.fetchone()

            Patient_Family = request.json['PFED_TYPE_NAME']
            cursor.execute("select PFED_TYPE_ID from PAT_FAMILY_HAS_EYE_DISEASE where PFED_TYPE_NAME=%s",
                           (Patient_Family,))
            account2 = cursor.fetchone()
            if "PFED001" in account2:
                medication = request.json['MEDICATIONS']
                medication1 = request.json['MEDICATIONS1']
                cursor.execute(
                    "insert into REG_EYE_DISEASE (PAT_HAS_ED,SYMPTOMS,PFM_HAS_ED,MEDICATIONS,MEDICATIONS1) "
                    "VALUES(%s,%s,%s,%s,%s)",
                    (account, account1, account2, medication, medication1))
                mysql.connection.commit()
                return "SUCCESS WITH YES CONDITIONS"
            else:
                medication2 = request.json['MEDICATIONS']
                cursor.execute(
                    "insert into REG_EYE_DISEASE (PAT_HAS_ED,SYMPTOMS,PFM_HAS_ED,MEDICATIONS) VALUES(%s,%s,%s,%s)",
                    (account, account1, account2, medication2))
                mysql.connection.commit()
                return "success with family no condition"

        else:
            Patient_Family = request.json['PFED_TYPE_NAME']
            cursor.execute("select PFED_TYPE_ID from PAT_FAMILY_HAS_EYE_DISEASE wh