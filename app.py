from flask import Flask, render_template, request, url_for, redirect, session
import db
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert_form')
def insert_form():
    return render_template('insert_form.html')

@app.route('/insert_exe', methods=['POST'])
def insert_exe():
    todo = request.form.get('todo')
    deadline = request.form.get('deadline')
    priority = int(request.form.get('priority'))
    
    count =  db.insert_todo(todo, deadline, priority)
    
    if count == 1:
        msg = '登録成功'
        return render_template('insert_form.html', msg=msg)
    else :
        error = '登録失敗'
        return render_template('insert_form.html', error=error)
    
@app.route('/select_todo')
def select_todo():
    rows = db.select_todo()
    
    return render_template('todo_list.html',rows=rows)
    
if __name__ == '__main__':
 app.run(debug=True)

 