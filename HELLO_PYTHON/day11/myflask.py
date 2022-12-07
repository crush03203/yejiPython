from day11.dao_mem import DaoMem
from flask import Flask
from flask import request
import psycopg2
from flask import Flask,render_template

app = Flask(__name__)
#list화면 출력

@app.route('/')
@app.route('/mem_list')
def mem_list():
    ds = DaoMem()
    list = ds.selects()
    return render_template('mem_list.html', list=list)


if __name__ == '__main__':
    app.run(debug=True)