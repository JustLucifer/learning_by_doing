const answers = [
  'You can invite up to 2 additional users on the Free<span>plan.\
  There is no limit on team members for the</span> Premium plan.',
  'No more than 2GB. All files in your account must fit<span>your\
   allotted storage space.</span>',
  'Click “Forgot password” from the login page or<span>“Change password”\
  from your profile page. A reset</span> link will be emailed to you.',
  'Yes! Send us a message and we\'ll process your request<span>no questions asked.</span>',
  'Chat and email support is available 24/7. Phone lines<span>are open\
   during normal business hours.</span>'
]

let tmpId;
let flag = false;
let buttonImg;

function showAnswer(questionId) {
  if (flag) {
    deleteAnswer();
    flipButtonImgBack();
    flag = false;
  }

  if (questionId !== tmpId) {
    const answer = createAnswer(questionId);
    const faqContainer = document.getElementById(`faq-container${questionId}`);
    faqContainer.appendChild(answer);
    flipButtonImg(questionId);
  } else {
    createAnswer();
  }
}

function deleteAnswer() {
  if (document.getElementById(`answer-container${tmpId}`)) {
    document.getElementById(`answer-container${tmpId}`).remove();
  }
}

function createAnswer(id) {
  const div = document.createElement('div');
  div.setAttribute('id', `answer-container${id}`);
  div.setAttribute('class', 'answer-container');

  const p = document.createElement('p');
  p.innerHTML = answers[id];

  div.appendChild(p);
  tmpId = id;
  flag = true;
  return div;
}

function flipButtonImg(id) {
  buttonImg = document.getElementById(`button-img${id}`);
  buttonImg.style.transform = 'scaleY(-1)';
}

function flipButtonImgBack() {
  buttonImg.removeAttribute('style');
}