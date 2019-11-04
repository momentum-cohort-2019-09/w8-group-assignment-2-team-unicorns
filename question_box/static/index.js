
document.querySelector('.questions').addEventListener('click', function(event) {
  let element = event.target
  if (element.matches('.favorite-star')) {
    const questionPk = element.dataset.questionPk
    fetch(`/question_box/${questionPk}/favorite`, {
      method: 'POST'
    }).then(resp => resp.json()
    )
    .then(resp => {
      if (resp.is_favorite) {
        element.innerText = "Remove from Favorites"
      }
      else {
        element.innerText = "Add to Favorites"
      }
    })
  }
})


let all_correct_buttons = document.querySelectorAll('.correct-answer')
for (let correct_button of all_correct_buttons) {
    correct_button.addEventListener('click', event => {
        event.preventDefault()
        const el = event.target

        fetch(`/question_box/${correct_button.dataset.answerid}/mark_correct`, {
            method: 'POST'
        })
        correct_button.parentElement.querySelector(".correct-answer").style.display = 'none'
        correct_button.parentElement.querySelector(".check-mark").style.display = 'inline-block'
    })
}

