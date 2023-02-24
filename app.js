fetch('data.json')
  .then(response => response.json())
  .then(data => {
    const employeeList = document.getElementById('employee-list');
    data.employees.forEach(employee => {
      const div = document.createElement('div');
      div.classList.add('employee');
      div.innerHTML = `
        <img src="${employee.image}" alt="${employee.name}">
        <h3>${employee.name} (${employee.age})</h3>
        <p>${employee.position}</p>
      `;
      employeeList.appendChild(div);
    });
  })
  .catch(error => console.error(error));
