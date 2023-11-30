from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def parent():
    return "<p><h1>WELCOME!</h1></p>"

data = {
    'details': [
        {'student_id': 100, 'f_name': "ram", 'gmail': "100.ram@gamil.com"},
        {'student_id': 101, 'f_name': "sam", 'gmail': "100.sam@gamil.com"},
        {'student_id': 102, 'f_name': "john", 'gmail': "john@gmail.com"}
    ]
}

@app.route("/get/<int:student_id>")
def get(student_id):
    for student in data['details']:
        if student['student_id'] == student_id:
            student_data = [student['f_name'], student['gmail']]
            return str(student_data)
    return 'Student not found'

if __name__ == '__main__':
    app.run()
