let errorAlreadyShowed = false;

const emailInput = document.getElementById('email');
emailInput.addEventListener('keypress', function() {
  deleteError();
  errorAlreadyShowed = false;
})

function deleteError() {
  const errorMessage =  document.getElementById('error-message');
  if (errorMessage) {
    errorMessage.remove();
  }
}

function appendErrorToDiv(error) {
  const emailContainer = document.getElementById('email-container');
  emailContainer.appendChild(error);
}

function createErrorMessage() {
  const errorMessage = document.createElement('p');
  errorMessage.innerText = 'Please provide a valid email address';
  errorMessage.setAttribute('id', 'error-message');
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
    console.log('i worked');
    if (!errorAlreadyShowed) {
      showErrorMessage();
      errorAlreadyShowed = true;
    }
  } else {
    email.value = '';
    errorAlreadyShowed = false;
  }
}