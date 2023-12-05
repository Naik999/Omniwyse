from flask import Flask ,render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:R%40vindra@localhost/data'

db = SQLAlchemy(app)

class User (db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(30))
    mail = db.Column(db.String(80), unique = True)
    age = db.Column(db.Integer)

@app.route('/')
def students():
    return render_template("new_path.html" )

@app.route('/submit', methods=["GET", "POST"])
def submit():
        user_id = request.form.get('id')
        if user_id:
            user = User.query.get(user_id)
            if user:
                out = f" {user.name} , {user.mail} , {user.age}"
                return jsonify(out)
        return "ID not provided"
    

if __name__ == '__main__':
    app.run()




