from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import date

app = Flask(__name__)

# DB初期化
def init_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            priority TEXT NOT NULL,
            deadline TEXT,
            completed INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    init_db()
    if request.method == 'POST':
        content = request.form['content']
        priority = request.form['priority']
        deadline = request.form['deadline']
        if content:
            conn = sqlite3.connect('todo.db')
            c = conn.cursor()
            c.execute('INSERT INTO tasks (content, priority, deadline) VALUES (?, ?, ?)',
                      (content, priority, deadline))
            conn.commit()
            conn.close()
        return redirect(url_for('index'))
    
    # タスク一覧取得
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks ORDER BY id DESC')
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
