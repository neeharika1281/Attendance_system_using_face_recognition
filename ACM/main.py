from flask import Flask,flash, redirect, url_for, request,render_template
from flask import session
# import MySQLdb
app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def success():
   return render_template('upload.html',msg='')

@app.route('/upload',methods = ['POST', 'GET'])
def upload():
   msg = []
   if request.method == 'POST':
        user_img_name = request.form['fileUpload']
        if(user_img_name==''):
            return render_template('upload.html',msg='Please select an image')
        msg.append(user_img_name)
        img_src = request.form['src']
        msg.append(img_src)
        print(user_img_name)
    #   conn = MySQLdb.connect( host="localhost",
    #                         user="root",
    #                         passwd="Neeha@123",
    #                         db="vignite",
    #                         port=3306)
    #   curs = conn.cursor()
    #   nrows=curs.execute("select * from users where username = %s and password = %s" ,(user,password,))
      
    #   if nrows == 1:
    #      msg = 'You have logged in successfully !'
    #      return render_template('chooseui.html', msg = msg) 
    #   else: 
    #      msg = 'Incorrect username / password !'
    #      return render_template('index.html',msg =  msg)    
        return render_template('completed.html',msg=msg)
if __name__ == '__main__':
   app.run(debug = True)   