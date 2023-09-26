    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('search');
    const filterSelect = document.getElementById('filterSelect');
    const displayList = document.getElementById('displayList');
    const listItems = displayList.getElementsByClassName('row-list');

searchForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const searchText = searchInput.value.toLowerCase();


        for (let i = 0; i < listItems.length; i++) {
          const listItem = listItems[i];
          const displayText = listItem.dataset.user.toLowerCase();
            console.log(displayText)
          if (displayText.includes(searchText)) {
            listItem.style.display = 'block';
          } else {
            listItem.style.display = 'none';
          }
        }
      });