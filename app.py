from load import *
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from plot import *
import sys
import os

#import the dataset from load.py
Graph1=cyclicgraph()
#Graph1.printGraph()
Graph1.isCyclic()
print ("Number of cycles are:",Graph1.ctr)
print ("Removing the cycles")
data=Graph1.removecycles()
#print (data)
savedata("dataset/data2.txt",data)
Graph2=nonecyclicgraph()
#Graph2.printGraph()
Graph2.isCyclic()
print ("Number of cycles are:",Graph2.ctr)

#Flask work
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redirect',methods=["GET","POST"])
def redirect():
    if request.method=="POST":
        x=int(request.form['x'])
        y=int(request.form['y'])
    print(x,y)
    visualise('dataset/data.txt',x,y,'static/cycle.png')
    visualise('dataset/data2.txt',x,y,'static/nocycle.png')
    return render_template('redirect.html')

@app.route('/cycle',methods=["GET","POST"])
def cycle():
    return render_template('cycle.html')

@app.route('/nocycle',methods=["GET","POST"])
def nocycle():
    return render_template('nocycle.html')

if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
