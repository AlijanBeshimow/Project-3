let HOST = "http://127.0.0.1:5000/api/tasks";

function showTasks() {
  axios.get(HOST)
    .then(response => {
      let data = response.data;
      let tasks = data.tasks;
      let length = tasks.length;

      let taskList = document.getElementById('taskList');
      taskList.innerHTML = '';
      
      tasks.forEach(task => {
        let taskDiv = document.createElement('div');
        taskDiv.classList.add('task');
        taskDiv.innerHTML = `
          <p class="title">${task.title}</p>
          <p class="description">${task.description}</p>
          <p class="category">${task.category}</p>
        `;
        taskList.appendChild(taskDiv);
      });

      let lengthElement = document.getElementById('length');
      lengthElement.textContent = length;
    })
    .catch(error => {
      console.error('Error fetching tasks:', error);
    });
}

showTasks();
