let showed = false;

const menuButton = document.getElementById('menu-button');
menuButton.addEventListener('click', function() {
  if (showed) {
    closeMenu();
  } else {
    showMenu();
  }
})

function showMenu() {
  dimButton();
  const menu = createMenu();

  const menuContainer = document.getElementById('menu-container');
  menuContainer.appendChild(menu);

  showed = true;
}

function createMenu() {
  const listItems = ['About', 'Services', 'Projects', 'CONTACT'];
  
  const div = document.createElement('div');
  div.id = 'mb-menu';

  const ul = document.createElement('ul');
  ul.className = 'navbar__list navbar__list--mb';

  for (let i = 0; i < listItems.length; i++) {
    const li = document.createElement('li');
    li.innerText = listItems[i];

    if (i === 3) {
      li.className = 'li-contact';
    }

    ul.appendChild(li);
  }

  div.appendChild(ul);
  return div;
}

function closeMenu() {
  document.getElementById('mb-menu').remove();
  LightButton();
  showed = false;
}

function dimButton() {
  menuButton.style.opacity = '.7';
}

function LightButton() {
  menuButton.style.opacity = '1';
}