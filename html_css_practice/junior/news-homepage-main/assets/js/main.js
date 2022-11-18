document.getElementById('hamburger-menu').addEventListener('click', function () {
  showMenu();
})

function showMenu() {
  const menu = createMenu();

  const nav = document.getElementById('nav-panel');
  nav.appendChild(menu);
}

function createMenu() {
  const menu = document.createElement('div');
  menu.setAttribute('id', 'mb-side-menu');

  const closeButton = document.createElement('button');
  const crossImage = document.createElement('img');
  crossImage.src = './assets/images/icon-menu-close.svg'
  closeButton.appendChild(crossImage);
  closeButton.setAttribute('id', 'cross-button');

  closeButton.addEventListener('click', function() {
    menu.remove();
  })
  
  const links = createLinks();
  
  menu.appendChild(closeButton);
  menu.appendChild(links);

  return menu;
}

function createLinks() {
  const linksNames = ['Home', 'New', 'Popular', 'Trending', 'Categories'];

  const linksContainer = document.createElement('div');
  linksContainer.setAttribute('id', 'links');

  for (let i = 0; i < 5; i++) {
    const link = document.createElement('a');
    link.href = '';
    link.innerText = linksNames[i];
    linksContainer.appendChild(link);
  }

  return linksContainer;
}