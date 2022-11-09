function changeColorOnFocus(element) {
  element.style.borderColor = 'hsl(248, 32%, 49%)';
}

function changeColorOnBlur(element) {
  element.style.borderColor = 'rgb(199, 199, 199)';
}

function checkForm() {
  const idsList = ['first-name', 'last-name', 'email', 'password'];
  let formInputs = [];

  for (let i = 0; i < 4; i++) {
    formInputs.push(document.getElementById(idsList[i]));
  }

  for (let i = 0; i < 4; i++) {
    checkInputElement(formInputs[i]);
  }

}

function checkInputElement(element) {
  const stripedElement = element.value.replace(/\s/g, '');

  if (element.id === 'email') {
    // simple check
    if (stripedElement === '' || !stripedElement.includes('@') || !stripedElement.includes('.')) {
      showErrorMessage(element);
    }
  } else {
    if (stripedElement === '') {
      showErrorMessage(element);
    }
  }
}

function showErrorMessage(element) {
  const errorImg = document.createElement('img');
  errorImg.src = './assets/images/icon-error.svg';
  errorImg.setAttribute('id', `${element.id}-error-message`);
  let errorMessage = document.createElement('p');
  errorMessage.setAttribute('id', `${element.id}-error-message`);
  let errorContainer = document.getElementById(`${element.id}-container`);

  if (element.id === 'first-name') {
    errorMessage.innerText = 'First Name cannot be empty';
  } else if (element.id === 'last-name') {
    errorMessage.innerText = 'Last Name cannot be empty';
  } else if (element.id === 'email') {
    errorMessage.innerText = 'Looks like this is not an email';
  } else if (element.id === 'password') {
    errorMessage.innerText = 'Password cannot be empty';
  }

  element.style.boxShadow = '0 0 2px 1px hsl(0, 100%, 50%)';
  errorContainer.appendChild(errorMessage);
  errorContainer.appendChild(errorImg);
}