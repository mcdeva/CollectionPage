function filterCards() {
    // Get the search box input value
    var input = document.getElementById("search-box");
    var filter = input.value.toUpperCase();

    // Get the selected category radio button value
    var categoryRadios = document.getElementsByName("category");
    var category;
    for (var i = 0; i < categoryRadios.length; i++) {
        if (categoryRadios[i].checked) {
            category = categoryRadios[i].value;
            break;
        }
    }

    // Get the table rows
    var rows = document.getElementsByTagName("tr");
    // Loop through the rows and hide those that don't match the search query or category
    for (var i = 1; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName("td");
        var match = false;
        for (var j = 0; j < cells.length; j++) {
            var cell = cells[j];
            if (cell) {
                var text = cell.textContent || cell.innerText;
                if (text.toUpperCase().indexOf(filter) > -1) {
                    match = true;
                }
            }
        }
        var categoryCell = cells[3];
        if (category === "all" || categoryCell.textContent === category) {
            if (match) {
                rows[i].style.display = "";
            } else {
                rows[i].style.display = "none";
            }
        } else {
            rows[i].style.display = "none";
        }
    }
}

fetch('static/cards.json')
    .then(response => response.json())
    .then(cards => {
    const cardList = document.getElementById('card-list');
        cards.forEach(card => {
            const row = document.createElement('tr');
            row.innerHTML = `
            <td id="id" class="category-${card.category}">${card.id}</td>
            <td id="name" class="category-${card.category}">${card.name}</td>
            <td id="energy" class="category-${card.category}">${card.energy}</td>
            <td id="category" class="category-${card.category}">${card.category}</td>
            <td id="box" class="category-${card.category}">${card.box}</td>
            <td id="order" class="category-${card.category}">${card.order}</td>
            <td id="type" class="category-${card.category}">${card.type}</td>
            <td id="quantity" class="category-${card.category}">${card.quantity}</td>
            `;
            cardList.appendChild(row);
        });
    })
    .catch(error => console.error('Error loading card data:', error));


window.addEventListener("load", function() {
    // Listen for changes to the search box and category radio buttons
    document.getElementById("search-box").addEventListener("keyup", filterCards);
    var categoryRadios = document.getElementsByName("category");
    for (var i = 0; i < categoryRadios.length; i++) {
        categoryRadios[i].addEventListener("change", filterCards);
    }
});
