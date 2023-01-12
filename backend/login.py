import pymysql
import json
from config import mydb
from flask import jsonify
from flask import flash, request
from app import app
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask import render_template

app.route('/get', methods=['GET'])
def Get():
    return 'haii'

@app.route('/register', methods=['POST'])
def register():
    try:
        json = request.json
        print(json)
        fullname =json['fullname']
        username = json['username']
        email= json['email']
        password = json['password']
      
        if fullname and username and email and password and request.method == 'POST':
            conn = mydb.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO user(fullname,username,email,password) VALUES(%s, %s, %s,%s)"
            bindData = (fullname,username,email,password)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('User added successfully!')
            respone.status_code = 200
            return respone
          
        else:
            return showMessage()
    except Exception as e:
        print(e)
        return 'Exception'
    # finally:
    #     cursor.close()
    #     conn.close()


@app.route('/login', methods=['POST'])
def login():
    try:
        json = request.json
        username = json['username']

        password = json['password']

        print(username)

        if username and password and request.method == 'POST':

            conn = mydb.connect()

            cursor = conn.cursor(pymysql.cursors.DictCursor)

            sqlQuery="SELECT fullname FROM user WHERE username= '%s'  and password='%s'" % (username, password)

            data=cursor.execute(sqlQuery)

            print(data)

            if data==1:

                access_token = create_access_token(identity=username)

                conn.commit()

                return jsonify(message='Login Successful', access_token=access_token),200

            else:

                conn.commit()

                return jsonify('Bad email or Password... Access Denied!'), 401

        else:

            return showMessage()

    except Exception as e:

        print(e)

        return 'Exception'

    finally:

        cursor.close()

        conn.close()

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

if __name__ == "__main__":
    app.run()

