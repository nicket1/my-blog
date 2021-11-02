from flask import Flask,render_template
from flask import Markup
import markdown
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
    content = md2html('static/markdown/index.md')
    return render_template('index.html',todo=todo,content=content)
def md2html(filename):
		
		exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
		mdcontent = ""
		with open(filename,'r',encoding='utf-8') as f:
			mdcontent = f.read()
			pass	
		html = markdown.markdown(mdcontent,extensions=exts)
		content = Markup(html)
		#Markup就是把内容转换成字符串，str不可以
		#也可以不用这个，但是前端的内容要加safe，像这样 {{ content | safe}}
		return content
def move_forward():
    #Moving forward code
    print("Moving Forward...")

   