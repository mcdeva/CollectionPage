document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('filter-form');
  const nameInput = document.getElementById('name-input');
  const categoryRadios = document.querySelectorAll('input[name="category"]');
  const cards = document.querySelectorAll('.card');

  function filterCards() {
    const nameFilter = nameInput.value.toLowerCase();
    let categoryFilter = '';
    categoryRadios.forEach(radio => {
      if (radio.checked) {
        categoryFilter = radio.value.toLowerCase();
      }
    });
    cards.forEach(card => {
      const name = card.querySelector('.card-name').textContent.toLowerCase();
      const category = card.querySelector('.card-category').textContent.toLowerCase();
      if (name.includes(nameFilter) && (categoryFilter === '' || category === categoryFilter)) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  nameInput.addEventListener('input', filterCards);
  categoryRadios.forEach(radio => {
    radio.addEventListener('change', filterCards);
  });
});
