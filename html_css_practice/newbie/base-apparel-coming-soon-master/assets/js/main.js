const emailInput = document.getElementById('email');
emailInput.addEventListener('keypress', function() {
  deleteError();
})

function deleteError() {
  document.getElementById('error-container').remove();
  document.getElementById('invalid-email-message').remove();
}

function appendErrorToDiv(error) {
  const emailContainer = document.getElementById('submit-email');
  emailContainer.appendChild(error);
}

function createErrorIcon() {
  const errorContainer = document.createElement('div');
  errorContainer.setAttribute('id', 'error-container');

  const errorImage = document.createElement('img');
  errorImage.src = './assets/images/icon-error.svg';

  errorContainer.appendChild(errorImage);
  return errorContainer;
}

function showErrorIcon() {
  const errorIcon = createErrorIcon();
  console.log(errorIcon);
  appendErrorToDiv(errorIcon);
}

function createErrorMessage() {
  const errorMessage = document.createElement('p');
  errorMessage.innerText = 'Please provide a valid email';
  errorMessage.setAttribute('id', 'invalid-email-message');
  return errorMessage;
}


function showErrorMessage() {
  const errorMessage = createErrorMessage();

  appendErrorToDiv(errorMessage);
}

function checkEmail() {
  let email = document.getElementById('email');
  stripedEmail = email.value.replace(/\s/g, '');

  if (stripedEmail === '' || !stripedEmail.includes('@')) {
    console.log('Put valid email');
    showErrorIcon();
    showErrorMessage();
  } else {
    email.value = '';
  }
}