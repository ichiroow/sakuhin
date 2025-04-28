# 完了切り替え
from flask import Blueprint, redirect, url_for
from db import get_db_connection

bp = Blueprint('complete', __name__, url_prefix='/complete')

@bp.route('/<int:task_id>')
def complete(task_id):
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET completed = CASE completed WHEN 0 THEN 1 ELSE 0 END WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('main.index'))
