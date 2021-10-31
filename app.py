from flask import Flask,render_template
import datetime
app = Flask(__name__)

todo=[
    {'date':'10.31','busness':'划水'},
    {'date':'11.01','busness':'白嫖'},
    {'date':'11.02','busness':'划水'},
    {'date':'11.03','busness':'划水'},
    {'date':'11.04','busness':'划水'}
]
year=datetime.datetime.now().year
mouth=datetime.datetime.now().month
day=datetime.datetime.now().day

@app.route('/')
def hello():
    return render_template('index.html',todo=todo,year=year,mouth=mouth,day=day);