
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import mysql.connector
import jwt


app = Flask(__name__)

mydb = mysql.connector.connect(host='127.0.0.1',user='root', password = "p@ssword")
mycursor = mydb.cursor()

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/GetUserInfo',methods = ['GET'])
def GetUser():
    
    user = request.args.get('uid')
    mycursor.execute("SELECT * FROM user WHERE uid="+user)
    myresult =  mycursor.fetchall()
    print()
    if(len(myresult)==0):
        return "User doesn't exit"
    else:
        data={'uid':myresult[0][0],'name':myresult[0][1],'age':myresult[0][3],'city':myresult[0][2]}
        return data

@app.route('/CreateUser',methods = ['POST'])
def CreateUser():
    content = request.json
    content = decode_jwt(content['token'])
    sql = "INSERT INTO user (name,city,age) VALUES(%s,%s,%s);"
    val = (content['name'],str(content['city']),str(content['age']))
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.execute("SELECT * FROM user WHERE name='{}'".format(content['name']))
    myresult =  mycursor.fetchall()
    data={'uid':myresult[0][0],'name':myresult[0][1],'age':myresult[0][3],'city':myresult[0][2]}
    return data

@app.route('/EditUser/<uid>',methods = ['PUT']) 
def EditUSer(uid):
    content = request.json
    content = decode_jwt(content['token'])
    print(content)
    mycursor.execute("SELECT * FROM user WHERE uid="+uid)
    myresult =  mycursor.fetchall()
    old_data ={'uid':myresult[0][0],'name':myresult[0][1],'age':myresult[0][3],'city':myresult[0][2]}
    new_data_keys = list(content.keys())
    new_data_value= list(content.values())
    j=0
    for i in new_data_keys:
        sql = "UPDATE user SET {} = \'{}\' WHERE {} = \'{}\'".format(i,new_data_value[j],i,old_data[i])
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        j= j+1
    mycursor.execute("SELECT * FROM user WHERE uid="+uid)
    myresult =  mycursor.fetchall()
    data ={'uid':myresult[0][0],'name':myresult[0][1],'age':myresult[0][3],'city':myresult[0][2]}
    return data

@app.route('/DeleteUser/<uid>',methods = ['DELETE'])
def DeleteUser(uid):
    content = decode_jwt(request.json['token'])
    if(content['action'] != 'delete'):
        return "You don't have permission to this operation"
    sql = "DELETE FROM user WHERE uid='{}'".format(uid)
    mycursor.execute(sql)
    mydb.commit()
    return uid+" Deleted"

@app.route('/upload')
def upload():
   return render_template('upload.html')

@app.route('/uploader', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

def decode_jwt(encrypted):
    return jwt.decode(encrypted,key='JWT_p@ssword',algorithms=["HS256"])

def Run_flask():
    mycursor.execute("use Python;")
    app.run()

