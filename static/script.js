document.addEventListener("DOMContentLoaded", function () {
    // Confirmation before deleting a task
    let deleteButtons = document.querySelectorAll(".delete-btn");
    deleteButtons.forEach(function (btn) {
        btn.addEventListener("click", function (event) {
            let confirmDelete = confirm("Are you sure you want to delete this task?");
            if (!confirmDelete) {
                event.preventDefault(); // Stop the deletion
            }
        });
    });

    // Form validation before submitting
    let taskForm = document.querySelector("#taskForm");
    if (taskForm) {
        taskForm.addEventListener("submit", function (event) {
            let title = document.querySelector("#title").value.trim();
            let description = document.querySelector("#description").value.trim();

            if (title === "" || description === "") {
                alert("Please fill out all fields before submitting!");
                event.preventDefault(); // Stop form submission
            }
        });
    }
});
