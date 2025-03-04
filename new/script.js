document.addEventListener("DOMContentLoaded", function () {
    // Search functionality
    const searchInput = document.querySelector("input[type='text']");
    searchInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            alert("Search functionality is not yet implemented.");
        }
    });

    // Book Now button functionality
    const bookButtons = document.querySelectorAll(".book-btn");
    bookButtons.forEach(button => {
        button.addEventListener("click", function () {
            alert("Booking functionality is not yet implemented.");
        });
    });
});
