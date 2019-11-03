let all_correct_buttons = document.querySelectorAll('.correct-answer')
for (let correct_button of all_correct_buttons) {
    correct_button.addEventListener('click', event => {
        event.preventDefault()
        const el = event.target

        fetch(`/question_box/${correct_button.dataset.answerid}/mark_correct/`, {
            method: 'POST'
        })
        correct_button.parentElement.querySelector(".correct-answer").style.display = 'none'
        correct_button.parentElement.querySelector(".check-mark").style.display = 'inline-block'
    })
}
