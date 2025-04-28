# 編集処理
from flask import Blueprint, render_template, request, redirect, url_for
from db import get_db_connection

bp = Blueprint('edit', __name__, url_prefix='/edit')

@bp.route('/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    conn = get_db_connection()
    if request.method == 'POST':
        content = request.form['content']
        priority = request.form['priority']
        deadline = request.form['deadline']
        conn.execute('UPDATE tasks SET content = ?, priority = ?, deadline = ? WHERE id = ?',
                     (content, priority, deadline, task_id))
        conn.commit()
        conn.close()
        return redirect(url_for('main.index'))
    
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    conn.close()
    return render_template('edit.html', task=task)
