var add_exercise = document.getElementById("add_exercise")
var exercises = document.getElementById("exercises")
var checkboxes = document.getElementsByClassName("include_details")
var hidden_inputs = document.getElementsByClassName("include_details_hidden")

/* Handle first hidden input for include_details */
checkboxes[1].addEventListener("change", function() {
    if (checkboxes[1].checked) {
        hidden_inputs[1].disabled = true
    }
    else {
        hidden_inputs[1].disabled = false
    }
})

/* Add listeners for delete exercise buttons */
var delete_buttons = document.getElementsByClassName("delete")
for (let i = 0; i < delete_buttons.length; i++) {
    delete_buttons[i].addEventListener("click", function() {
        delete_buttons[i].parentElement.parentElement.remove()
    })
}

/* Add exercise function */
add_exercise.addEventListener("click", function() {

    /* Clone template */
    var template = document.getElementById("template").querySelector(".exercise")
    var clone = template.cloneNode(true)

    /* Show and enable inputs */
    clone.hidden = false
    var clone_inputs = clone.getElementsByTagName("input")
    for (let i = 0; i < clone_inputs.length; i++) {
        clone_inputs[i].disabled = false
    }

    /* Add listener for delete exercise button */
    var delete_button = clone.getElementsByClassName("delete")[0]
    delete_button.addEventListener("click", function() {
        delete_button.parentElement.parentElement.remove()
    })

    /* Add to workout form */
    exercises.appendChild(clone)

    /* Handle hidden inputs for include_details */
    for (let i = 1; i < checkboxes.length; i++) {
        checkboxes[i].addEventListener("change", function() {
            if (checkboxes[i].checked) {
                hidden_inputs[i].disabled = true
            }
            else {
                hidden_inputs[i].disabled = false
            }
        })
    }

})

/* Create sortable list */
new Sortable(exercises, {
    animation: 250,
    handle: ".handle"
})