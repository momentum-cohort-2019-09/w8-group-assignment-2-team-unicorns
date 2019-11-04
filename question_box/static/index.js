
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

