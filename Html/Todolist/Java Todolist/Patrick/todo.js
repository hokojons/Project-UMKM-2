// Function to add a new task
function addTask() {
    const taskInput = document.getElementById('taskInput');
    const taskText = taskInput.value.trim();
    
    if (taskText === '') {
        alert('Please enter a task!');
        return;
    }
    
    const taskList = document.getElementById('taskList');
    
    // Create new list item
    const li = document.createElement('li');
    
    // Create task text span
    const taskSpan = document.createElement('span');
    taskSpan.textContent = taskText;
    
    // Create delete button
    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';
    deleteBtn.className = 'delete-btn';
    deleteBtn.onclick = function() {
        taskList.removeChild(li);
        updateSummary();
    };
    
    // Toggle completed status when clicked
    taskSpan.onclick = function() {
        taskSpan.classList.toggle('completed');
        updateSummary();
    };
    
    // Append elements to list item
    li.appendChild(taskSpan);
    li.appendChild(deleteBtn);
    
    // Add list item to the list
    taskList.appendChild(li);
    
    // Clear input field
    taskInput.value = '';
    
    // Update task summary
    updateSummary();
}

// Function to update the task summary
function updateSummary() {
    const taskList = document.getElementById('taskList');
    const totalTasks = taskList.children.length;
    const completedTasks = document.querySelectorAll('.completed').length;
    
    document.getElementById('totalTasks').textContent = totalTasks;
    document.getElementById('completedTasks').textContent = completedTasks;
}

// Allow adding task with Enter key
document.getElementById('taskInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        addTask();
    }
});