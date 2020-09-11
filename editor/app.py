from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
#import bleach # to clean unnesseray data form editor data like script etc.
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///editor_base.db'
db = SQLAlchemy(app)

class editor_base(db.Model):
   id = db.Column('content_id', db.Integer, primary_key = True)
   content = db.Column(db.Text)
   
db.create_all()


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        #cleaned_data = bleach.clean(request.form.get('editordata')) # this thing to remove destuctive java script
        new_data= editor_base(content=request.form.get('editordata'))
        db.session.add(new_data)
        db.session.commit()
        return 'Poster Data'
    return render_template('index.html')

@app.route("/display/<int:id>")
def display(id):
    data=editor_base.query.get(id)
    return render_template('display.html',data=data.content)



if __name__ == '__main__':
    app.run(debug=True)