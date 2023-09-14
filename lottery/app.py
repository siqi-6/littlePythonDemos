from flask import Flask,render_template
from random import randint

app = Flask(__name__)

heros = ['张三', '李四', '王麻子']

@app.route('/index')
def index():
    return render_template('index.html',hero=heros)

@app.route('/lottery')
def lottery():
   num= randint(0,len(heros)-1)
   return render_template('index.html',hero=heros,h=heros[num])


app.run(debug=True)
