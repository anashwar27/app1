from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from sqlalchemy.exc import IntegrityError

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
# todo-jha data store hoga
db=SQLAlchemy(app)
app.app_context().push()

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    data_created=db.Column(db.DateTime,default=datetime.utcnow)


    def __repr__(self):
        return f"{self.sno}-{self.title}-{self.desc}"
    
@app.route('/',methods=["GET","POST"])
def hello_world():
     if request.method=="POST": 
         title=request.form['title']
         desc=request.form['desc']
         todo=Todo(title=title,desc=desc)
         db.session.add(todo)
         db.session.commit()
     alltodo=Todo.query.all()
     return render_template('index.html',alltodo=alltodo)

@app.route('/show')
def show():
    alltodo=Todo.query.all()
    print(alltodo)
    return "hello user"
@app.route('/delete/<int:sno>')
def delete(sno):
    alltodo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(alltodo)
    db.session.commit()
    return redirect('/')
@app.route('/update/<int:sno>',methods=["GET","POST"])

def update(sno):
    if request.method=='POST':
         title=request.form['title']
         desc=request.form['desc']
         alltodo=Todo.query.filter_by(sno=sno).first()
         alltodo.title=title
         alltodo.desc=desc
         db.session.add(alltodo)
         db.session.commit()
         return redirect('/')

    alltodo=Todo.query.filter_by(sno=sno).first()
    return render_template('update.html',alltodo=alltodo)
    

if __name__=="__main__":
    app.run(debug=True)














































































# class Posts(db.Model):
#     # s.no,first,last,email
#     sno = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(80), unique=False, nullable=False)
#     last_name= db.Column(db.String(80), unique=False, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

# @app.route('/',methods = ['GET','POST'])
# def hello_world():
#     return render_template('index.html')
# @app.route('/product')
# def product():
#     return "this is product page"
# @app.route('/')
# def todo():
#     if request.method=="POST":
#         first_na=request.form.get('first_name')
#         last_na=request.form.get('last_name')
#         email=request.form.get('email')
#         entry=Posts(first_name=first_na,last_name=last_na,email=email)
#         db.session(entry)
#         db.session.commit()


#     return "not"



