document.addEventListener('DOMContentLoaded', () => {
  const addBtn = document.getElementById('addBtn');
  const todoInput = document.getElementById('todo');
  const prioritySelect = document.getElementById('priority');
  const deadlineInput = document.getElementById('deadline');
  const taskList = document.getElementById('taskList');

  // ✅ 新規：完了タスク表示ボタン
  const showAllBtn = document.getElementById('showAll');
  const showCompletedBtn = document.getElementById('showCompleted');

  addBtn.addEventListener('click', () => {
    const todo = todoInput.value.trim();
    const priority = prioritySelect.value;
    const deadline = deadlineInput.value;

    if (todo === '') {
      alert('タスクを入力してください。');
      return;
    }

    const li = document.createElement('li');

    // ✅ チェックボックス追加
    li.innerHTML = `
      <input type="checkbox" class="completeCheckbox">
      <span><strong>${todo}</strong> （優先度: ${priority}、期日: ${deadline || '未設定'}）</span>
      <button class="editBtn">編集</button>
      <button class="deleteBtn">削除</button>
    `;

    const checkbox = li.querySelector('.completeCheckbox');
    checkbox.addEventListener('change', () => {
      if (checkbox.checked) {
        li.classList.add('completed');
        li.style.display = 'none'; // 完了時は非表示
      } else {
        li.classList.remove('completed');
        li.style.display = '';     // 未完了時は表示
      }
    });

    // 削除機能
    li.querySelector('.deleteBtn').addEventListener('click', () => {
      taskList.removeChild(li);
    });

    // 編集機能
    li.querySelector('.editBtn').addEventListener('click', () => {
      const span = li.querySelector('span');
      const oldText = span.innerText;
      const [oldTodo, rest] = oldText.split(' （優先度: ');
      const [oldPriority, oldDeadlinePart] = rest.split('、期日: ');
      const oldDeadline = oldDeadlinePart.replace('）', '');

      span.innerHTML = `
        <input type="text" class="edit-todo" value="${oldTodo.trim()}">
        <select class="edit-priority">
          <option value="低" ${oldPriority === '低' ? 'selected' : ''}>低</option>
          <option value="普" ${oldPriority === '普' ? 'selected' : ''}>普</option>
          <option value="高" ${oldPriority === '高' ? 'selected' : ''}>高</option>
        </select>
        <input type="date" class="edit-deadline" value="${oldDeadline}">
        <button class="saveBtn">保存</button>
        <button class="cancelBtn">キャンセル</button>
      `;

      li.querySelector('.saveBtn').addEventListener('click', () => {
        const newTodo = li.querySelector('.edit-todo').value.trim();
        const newPriority = li.querySelector('.edit-priority').value;
        const newDeadline = li.querySelector('.edit-deadline').value;

        if (newTodo === '') {
          alert('タスク内容を入力してください。');
          return;
        }

        span.innerHTML = `<strong>${newTodo}</strong> （優先度: ${newPriority}、期日: ${newDeadline || '未設定'}）`;
      });

      li.querySelector('.cancelBtn').addEventListener('click', () => {
        span.innerHTML = oldText;
      });
    });

    taskList.appendChild(li);
    todoInput.value = '';
    prioritySelect.value = '普';
    deadlineInput.value = '';
  });

  // ✅ 表示切り替え機能
  if (showAllBtn && showCompletedBtn) {
    // 「現在のタスク」ボタン：未完了のタスクだけ表示
    showAllBtn.addEventListener('click', () => {
      Array.from(taskList.children).forEach(li => {
        li.style.display = li.classList.contains('completed') ? 'none' : '';
      });
    });

    // 「完了タスクのみ表示」ボタン：完了タスクだけ表示
    showCompletedBtn.addEventListener('click', () => {
      Array.from(taskList.children).forEach(li => {
        li.style.display = li.classList.contains('completed') ? '' : 'none';
      });
    });
  }
});
