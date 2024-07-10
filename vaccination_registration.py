from flask import Flask, request
from flask_mysqldb import MySQL
from werkzeug.routing import ValidationError


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'soft'
app.config['SECRET_KEY'] = 'omkar'
mysql = MySQL(app)


@app.route('/vac_reg', methods=['POST'])
def vac_reg():
    if request.method == 'POST':
        user = request.json
        YEARS = user['YEARS']
        VACCINE_NAME = user['VAC_NAME']
        try:
            cur = mysql.connection.cursor()
            cur.execute("select YEARS from VACCINATIONS where YEARS=%s", (YEARS,))
            data = cur.fetchone()

            cur.execute("select VACCINE_ID from VACCINATIONS  WHERE (YEARS=%s AND "
                        "VACCINE_NAME=%s)", (YEARS, VACCINE_NAME))
            data1 = cur.fetchone()

            Vaccinated = user['Vaccinated']
            cur.execute("select ID from covid19_vaccine  WHERE (Vaccinated=%s)", (Vaccinated,))
            data2 = cur.fetchone()

            x = "VC001"
            if x in data2:
                Dose = user['Dose']
                covid_vaccine_name = user['covid_vaccine_name']
                cur.execute("select ID from covid19_dose  WHERE (Dose=%s)", (Dose,))
                data3 = cur.fetchone()

                other_vaccine_name = user['other_vaccine_name']
                cur.execute("insert into VAC_BOOKING(ID,YEARS,VAC_NAME,VACCINATED,COVID_VAC_NAME,DOSE,OTHER_VAC_NAME)"
                            "values(null,%s,%s,%s,%s,%s,%s)", (data, data1, data2, covid_vaccine_name, data3, other_vaccine_name))
                mysql.connection.commit()
            else:
                cur.execute("insert into VAC_BOOKING(ID,YEARS,VAC_NAME,VACCINATED)"
                            "values(null,%s,%s,%s)", (data, data1, data2))
                mysql.connection.commit()
        except ValidationError as e:
            print(e)
        return 'Successfully inserted Records'
    return'invalid Parameters'
	
if __name__ == '__main__':
    app.run(debug=True)
