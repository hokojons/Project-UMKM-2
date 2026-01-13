const todoInput = document.getElementById('todo-input');
const addBtn = document.getElementById('add-btn');
const todoList = document.getElementById('todo-list');

let todos = [];

function addTodo() {
    const todoText = todoInput.value.trim();
    
    if (todoText !== '') {
        const newTodo = {
            id: Date.now(),
            text: todoText,
            completed: false
        };
        
        todos.push(newTodo);
        
        renderTodos();
        
        todoInput.value = '';
    }
}

function renderTodos() {
    todoList.innerHTML = '';
    
    todos.forEach(todo => {
        const li = document.createElement('li');
        li.className = 'todo-item';
        li.dataset.id = todo.id;
        
        const span = document.createElement('span');
        span.textContent = todo.text;
        if (todo.completed) {
            span.style.textDecoration = 'line-through';
            span.style.color = '#888';
        }
        
        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'delete-btn';
        deleteBtn.textContent = 'Hapus';
        deleteBtn.addEventListener('click', () => deleteTodo(todo.id));
        
        span.addEventListener('click', () => toggleComplete(todo.id));
        
        li.appendChild(span);
        li.appendChild(deleteBtn);
        todoList.appendChild(li);
    });
}

function deleteTodo(id) {
    todos = todos.filter(todo => todo.id !== id);
    renderTodos();
}

function toggleComplete(id) {
    todos = todos.map(todo => {
        if (todo.id === id) {
            return {...todo, completed: !todo.completed};
        }
        return todo;
    });
    renderTodos();
}

addBtn.addEventListener('click', addTodo);

todoInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        addTodo();
    }
});

if (localStorage.getItem('todos')) {
    todos = JSON.parse(localStorage.getItem('todos'));
    renderTodos();
}

window.addEventListener('beforeunload', () => {
    localStorage.setItem('todos', JSON.stringify(todos));
});