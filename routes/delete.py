# 削除機能
from flask import Blueprint, redirect, url_for
from db import get_db_connection

bp = Blueprint('delete', __name__, url_prefix='/delete')

@bp.route('/<int:task_id>')
def delete(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('main.index'))
