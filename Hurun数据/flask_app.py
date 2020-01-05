# -*- coding:utf-8 -*-
from flask import Flask,request,redirect,jsonify,render_template,Response,make_response
import json
import os
from shutil import copytree,rmtree
import pandas as pd

app = Flask(__name__)



list = ['电视出口总额','二零一八年分省传输网络总量地理图','欧洲与美洲出口总额']

@app.route('/',methods=['GET'])
def index():
    return redirect('/TV-export')

@app.route('/TV-export',methods=['GET'])
def export():
    path = (os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), 'csv/TV-export.csv' ))
    result = pd.read_csv( path, encoding='utf-8', delimiter="," )
    data = result.to_html( )
    return render_template( 'TV-export.html', the_res=data, list=list )


@app.route('/total-transmission',methods=['GET'])
def total_transmission():
    path = (os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), 'csv/transmisson.csv' ))
    result = pd.read_csv( path, encoding='utf-8', delimiter="," )
    data = result.to_html( )
    return render_template( 'transmisson.html', the_res=data, list=list )

@app.route('/total',methods=['GET'])
def total():
    path = (os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), 'csv/transmisson.csv' ))
    result = pd.read_csv( path, encoding='utf-8', delimiter="," )
    data = result.to_html( )
    return render_template( 'total.html', the_res=data, list=list )

@app.route('/skip',methods=['POST'])
def skip():
    option = request.form['option']
    if option == "电视出口总额":
        return redirect('/TV-export')
    elif option == "二零一八年分省传输网络总量地理图":
        return redirect('/total-transmission')
    elif option == "欧洲与美洲出口总额":
        return redirect('/total')
    else:
        return "异常"

if __name__ == '__main__':
    app.run(debug=True,port=8080)