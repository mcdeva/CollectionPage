fetch('data.json')
  .then(response => response.json())
  .then(data => {
    const employeeList = document.getElementById('employee-list');
    data.employees.forEach(employee => {
      const li = document.createElement('li');
      li.textContent = `${employee.name} (${employee.age}) - ${employee.position}`;
      employeeList.appendChild(li);
    });
  })
  .catch(error => console.error(error));
