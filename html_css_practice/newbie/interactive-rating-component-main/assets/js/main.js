const listElements = [];

function chooseRating(rating) {
  let buttonId = rating.innerText;
  const listRateButtons = document.querySelectorAll('.rate-button');
  
  for (i = 0; i < listRateButtons.length; i++) {
    let rateButton = listRateButtons[i];

    if (listRateButtons[i].innerText === buttonId) {
      rateButton.style.background = 'hsl(217, 12%, 63%)';
      rateButton.style.color= 'white';
      rateButton.setAttribute('id', 'choosed-rating');
    } else {
      rateButton.style.background = 'hsl(216, 12%, 22%)';
      rateButton.style.color= 'hsl(216, 12%, 54%)';
      rateButton.removeAttribute('id');
    }
  }
}

function createImage() {
  const img = document.createElement('img');
  img.src = './assets/images/illustration-thank-you.svg'
  listElements.push(img);
}

function createRatingResponse(rating) {
  const ratingResponse = document.createElement('p');
  ratingResponse.innerText = `You selected ${rating} out of 5`;
  ratingResponse.setAttribute('class', 'rating-response');

  listElements.push(ratingResponse);
}

function createThankYouH1() {
  const h1 = document.createElement('h1');
  h1.style.color = 'white';
  h1.innerText = 'Thank You!'
  listElements.push(h1);
}

function createDescription() {
  const description = document.createElement('p');
  description.innerHTML = 'We appreciate you taking the time to give a rating. <span>If you ever need more support, don\'t hesitate to</span> get in touch!';

  listElements.push(description);
}

function createThankYouPage(rating) {
  const thankYouContainer = document.createElement('div');
  createImage();
  createRatingResponse(rating);
  createThankYouH1();
  createDescription();

  thankYouContainer.setAttribute('class', 'thank-you-container');

  for (let i = 0; i < listElements.length; i++) {
    thankYouContainer.appendChild(listElements[i]);
  }

  return thankYouContainer;
}

function sendRating() {
  const rating = document.getElementById('choosed-rating').innerText;

  const thankYouPage = createThankYouPage(rating);
  const mainElement = document.querySelector('main');
  const oldDiv = document.getElementById('rating-component');
  mainElement.removeChild(oldDiv);
  mainElement.appendChild(thankYouPage);
}
