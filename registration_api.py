@app.route('/EYE', methods=['POST'])
def EYE_D():
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
            cursor.execute("select PFED_TYPE_ID from PAT_FAMILY_HAS_EYE_DISEASE where PFED_TYPE_NAME=%s", (Patient_Family,))
            account2 = cursor.fetchone()
            if "PFED001" in account2:
                medication = request.json['MEDICATIONS']
                medication1 = request.json['MEDICATIONS1']
                cursor.execute(
                    "insert into REG_EYE_DISEASE (PAT_HAS_ED,SYMPTOMS,PFM_HAS_ED,MEDICATIONS,MEDICATIONS1) VALUES(%s,%s,%s,%s,%s)",
                    (account, account1, account2, medication,medication1))
                mysql.connection.commit()
                return "SUCCESS WITH YES CONDITIONS"
            else:
                medication2 = request.json['MEDICATIONS']
                cursor.execute("insert into REG_EYE_DISEASE (PAT_HAS_ED,SYMPTOMS,PFM_HAS_ED,MEDICATIONS) VALUES(%s,%s,%s,%s)",
                               (account, account1, account2,medication2))
                mysql.connection.commit()
                return "success with family no condition"

        else:
            Patient_Family = request.json['PFED_TYPE_NAME']
            cursor.execute("select PFED_TYPE_ID from PAT_FAMILY_HAS_EYE_DISEASE where PFED_TYPE_NAME=%s",
                           (Patient_Family,))
            account3 = cursor.fetchone()
            if 'PFED001' in account3:
                medication3 = request.json['MEDICATIONS1']
                cursor.execute("insert into REG_EYE_DISEASE (PAT_HAS_ED,PFM_HAS_ED,MEDICATIONS1) VALUES(%s,%s,%s)",
                               (account, account3, medication3))
                mysql.connection.commit()
                return "no and yes condition"
            else:
                cursor.execute("insert into REG_EYE_DISEASE (PAT_HAS_ED,PFM_HAS_ED) VALUES(%s,%s)",
                               (account, account3))
                mysql.connection.commit()
                return 'no and no condition'

    return 'invalid Parameters'
\