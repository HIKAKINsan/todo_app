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

@app.route('/coplate_todo', methods=['POST', 'GET'])
def complate_todo():
    todo_id = int(request.args.get('id'))
    complate = request.form.get('complate')
    
    if complate == 'on':
        complate = True
    else:
        return redirect(url_for('select_todo'))
            
    count = db.complate_todo(todo_id, complate)
    
    if count == 1:
        msg = '完了しました'
        return render_template('todo_finish.html', msg=msg)
    else:
        error = '完了できない'
        return render_template('todo_list.html', error=error)
    

@app.route('/select_complate_todo')
def select_complate_todo():
    rows = db.select_complate_todo()
    
    return render_template('complate_todo_list.html',rows=rows)

@app.route('/edit_form')
def edit_form():
    todo_id = int(request.args.get('id'))
    
    row = db.id_select_todo(todo_id)
    
    return render_template('edit_form.html', row=row)


@app.route('/edit_exe', methods=['POST', 'GET'])
def edit_exe():
    todo_id = request.args.get('id')
    todo = request.form.get('todo')
    deadline = request.form.get('deadline')
    priority = request.form.get('priority')
    
    count = db.edit_todo(todo_id, todo, deadline, priority)
    
    if count == 1:
        msg = '編集しました'
        return render_template('edit_finish.html',msg=msg)
    
@app.route('/delete_form')
def delete_form():
    rows = db.select_todo()
    
    return render_template('delete_form.html',rows=rows)

@app.route('/delete_exe')
def delete_exe():
    todo_id = request.args.get('id')
    count = db.delete_todo(todo_id)
    
    if count == 1:
        msg = '削除成功'
        return  render_template('delete_finish.html',msg=msg)

if __name__ == '__main__':
 app.run(debug=True)

 