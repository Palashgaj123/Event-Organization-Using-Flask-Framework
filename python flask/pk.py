from flask import *
import pymysql

db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "palashg",
    
   ) 
    
cursor = db.cursor()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/order")
def order():
    cursor.execute("SELECT * FROM pg")
    data = cursor.fetchall()
    return render_template("order.html",pg=data)
                           
@app.route("/edit",methods =["POST"])                           
def edit():
    uname = request.form.get('name')
    contact = request.form.get('contact')
    emailid = request.form.get('emailid')
    schedule = request.form.get('schedule')
    price = request.form.get('price')
   
    insq = "insert into pg(Name,Contact,emailid,Schedule,price) values ('{}','{}','{}','{}','{}')".format(uname,contact,emailid,schedule,price)
 
       
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for('order'))
            
    except:
         db.rollback()
         return "error in query"
     


if __name__=="__main__":
    app.run(debug=True)
    
    