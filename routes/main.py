# タスクの一覧・追加
from flask import Blueprint, render_template, request, redirect, url_for
from db import init_db, get_db_connection

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    init_db()
    if request.method == 'POST':
        content = request.form['content']
        priority = request.form['priority']
        deadline = request.form['deadline']
        if content:
            conn = get_db_connection()
            conn.execute('INSERT INTO tasks (content, priority, deadline) VALUES (?, ?, ?)',
                         (content, priority, deadline))
            conn.commit()
            conn.close()
        return redirect(url_for('main.index'))

    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)
