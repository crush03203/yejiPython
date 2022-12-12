from flask import Flask
from flask import request
import psycopg2
from flask import Flask,render_template
from flask.json import jsonify




app = Flask(__name__)



@app.route('/')
@app.route('/three')
def teacher():
    return render_template('three.html')



if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    