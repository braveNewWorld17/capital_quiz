import pymysql
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

"""
Run this from your shell
and then visit http://localhost:4000/ from your browser
"""

home_html = """
<html>
<body background='http://flightattendanttraininghq.com/wp-content/uploads/2017/09/Quiz-Time.png'>
<center>
<h1>Welcome to Quiz World</h1>
<hr>
<li><a href='/state_capital'>State Capital</li>
<li><a href='/nation_capital'>Nation Capital</li>
</center>
</html>
"""

question_answer_html_header_state = """
<html>
<body>
    <center>
    <h1>State Capital Questions</h1>
"""
question_answer_html_header_nation = """
<html>
<body>
    <center>
    <h1>Nation Capital Questions</h1>
"""
question_answer_html_footer = """    
    </center>
</body>
</html>
"""

def get_state_capital():
    sc = []
    conn = pymysql.connect(host='localhost',
                       user='root', password='as920558',
                       db='test', charset='utf8')
    curs = conn.cursor()
    sql = "select state, capital from state_capital"
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        sc.append({ 'state':row[0], 'capital':row[1] })
    conn.close()
    return sc

def get_nation_capital():
    nc = []
    conn = pymysql.connect(host='localhost',
                       user='root', password='as920558',
                       db='test', charset='utf8')
    curs = conn.cursor()
    sql = "select nation, capital from nation_capital"
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        nc.append({ 'nation':row[0], 'capital':row[1] })
    conn.close()
    print(nc)
    return nc

def table_state_capital(sc_list):
    html = "<table border = '1'>"
    for sc in sc_list:
        qa_pair = "<tr align = 'center' valign = 'middle'>"
        qa_pair += "<td><h3>Capital of <b>" + sc['state'] + "</b></td>"
        qa_pair += "<td><h3><font color='red'><i>" + sc['capital'] + "</font></i></h3><p></td>"
        qa_pair += "</tr>"
        html += qa_pair
    html += "</tr>"
    html += "</table>"
    return html
   
def table_nation_capital(nc_list):
    html = "<table border = '1'>"
    html += "<tr ><th align = 'cneter' valign = 'middle'> Nation </th>"
    html += "<th align = 'cneter' valign = 'middle'> Capital </th></tr>"
    for nc in nc_list:
        qa_pair = "<tr align = 'center' valign = 'middle'>"
        qa_pair += "<td><h3><b>" + nc['nation'] + "</b></td>"
        qa_pair += "<td><h3><font color='red'><i>" + nc['capital'] + "</font></i></h3><p></td>"
        qa_pair += "</tr>"
        html += qa_pair
    html += "</tr>"
    html += "</table>"
    return html
   
@app.route("/")
def index():
    return home_html

@app.route("/state_capital", methods=['GET'])
def state_capital():
    sc_list = get_state_capital()
    html = question_answer_html_header_state
    qa_pair = table_state_capital(sc_list)
    html += qa_pair
    html += question_answer_html_footer
    return html
 
@app.route("/nation_capital", methods=['GET'])
def nation_capital():
    nc_list = get_nation_capital()
    html = question_answer_html_header_nation
    qa_pair = table_nation_capital(nc_list)
    html += qa_pair
    html += question_answer_html_footer
    return html
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
