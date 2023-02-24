function loadDataCard() {
    fetch('data.json')
        .then(response => response.json())
        .then(data => {
            const employeeList = document.getElementById('collection-card-list');
            data.employees.forEach(employee => {
            const div = document.createElement('div');
            div.classList.add('employee');
            div.innerHTML = `
                <img src='${employee.image}' alt='${employee.name}'>
                <h3>${employee.name} (${employee.age})</h3>
                <p>${employee.position}</p>
            `;
            employeeList.appendChild(div);
            });
        })
        .catch(error => {
            console.error('Error loading card data:', error);
        });
}

// For Test
// loadDataCard();
function showPrompt() {
    // Define the expected password
    const expectedPassword = '9048f53c1c342ae6640cf14e86cd7be223cf8e0cf0dfcb024d1e3b5b9ea88023';

    // Prompt the user for their password
    const userInput = prompt('Enter your password:');

    // Encrypt the user input using a secure hashing algorithm
    sha256(userInput).then(hashedInput => {
    // Compare the hashed input to the expected password
        if (hashedInput === expectedPassword) {
            loadDataCard();
            loadCardList();
        } else {
            alert('Access denied.');
        }
    });
}

// Define a secure hashing algorithm (such as SHA-256)
async function sha256(input) {
    const hashBuffer = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(input));
    return hex(hashBuffer);
}

// Convert a byte array to a hex string
function hex(buffer) {
return Array.from(new Uint8Array(buffer))
    .map(b => b.toString(16).padStart(2, '0'))
    .join('');
}

// Card List
// const cardList = document.getElementById('cardList');

// let isDown = false;
// let startX;
// let scrollLeft;

// cardList.addEventListener('mousedown', (e) => {
//     isDown = true;
//     startX = e.pageX - cardList.offsetLeft;
//     scrollLeft = cardList.scrollLeft;
//     cancelAnimationFrame(animate);
// });

// cardList.addEventListener('mouseleave', () => {
//     isDown = false;
//     cancelAnimationFrame(animate);
// });

// cardList.addEventListener('mouseup', () => {
//     isDown = false;
//     cancelAnimationFrame(animate);
// });

// cardList.addEventListener('mousemove', (e) => {
//     if (!isDown) return;
//     e.preventDefault();
//     const x = e.pageX - cardList.offsetLeft;
//     const walk = x - startX;
//     cardList.scrollLeft = scrollLeft - walk;
// });

// function animate() {
//     requestAnimationFrame(animate);
//     cardList.scrollLeft += 1;
// }

// animate();

function loadCardList() {
    fetch('cards.json')
        .then(response => response.json())
        .then(data => {
            const cardList = document.getElementById('cardList');
            data.forEach(cardData => {
                const card = document.createElement('div');
                card.classList.add('card');

                const image = document.createElement('img');
                image.src = cardData.image;
                image.alt = 'Card Image';
                card.appendChild(image);

                const content = document.createElement('div');
                content.classList.add('card-content');

                const title = document.createElement('h2');
                title.textContent = cardData.title;
                content.appendChild(title);

                const description = document.createElement('p');
                description.textContent = cardData.content;
                content.appendChild(description);

                card.appendChild(content);

                cardList.appendChild(card);
            });
        })
        .catch(error => {
            console.error('Error loading card data:', error);
        });
}
