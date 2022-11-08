let divIsActive = false;
const iconsPath = ['icon-facebook.svg', 'icon-twitter.svg', 'icon-pinterest.svg']

function createShareDiv() {
  const div = document.createElement('div');
  const h4 = document.createElement('h4');

  h4.innerText = 'SHARE';
  div.setAttribute('id', 'talkbubble');
  div.appendChild(h4)

  for (let i = 0; i < 3; i++) {
    let img = document.createElement('img');
    img.src = './assets/images/' + iconsPath[i];
    img.setAttribute('class', 'share-app-icon');
    div.appendChild(img);
  }
  
  const shareDiv = document.createElement('div');
  shareDiv.appendChild(div);
  shareDiv.setAttribute('id', 'share-div');

  return shareDiv;
}

function showShareDiv() {
  const shareDiv = createShareDiv();

  if (divIsActive === false) {
    document.getElementById('share-container').appendChild(shareDiv);
    divIsActive = true;
  } else {
    document.getElementById('share-div').remove();
    divIsActive = false;
  }
}