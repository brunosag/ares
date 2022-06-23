var select_workout = document.getElementById("select_workout")

/* Show selected workout on page load */
var selected_workout = document.getElementsByClassName(`workout ${select_workout.value}`)[0]
selected_workout.hidden = false

/* Listen for change in select menu */
select_workout.addEventListener("change", function() {

    /* Hide current shown workout */
    var workouts = document.getElementsByClassName("workout")
    for (let i = 0; i < workouts.length; i++) {
        workouts[i].hidden = true
    }

    /* Show selected workout */
    var selected_workout = document.getElementsByClassName(`workout ${select_workout.value}`)[0]
    selected_workout.hidden = false
})

/* Listen for delete exercise buttons */
var delete_buttons = document.querySelectorAll(".delete")
delete_buttons.forEach(element => {
    element.addEventListener("click", () => {
        element.parentElement.parentElement.remove()
    })
});