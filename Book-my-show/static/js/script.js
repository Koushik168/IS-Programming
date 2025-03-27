// Wait until the DOM is fully loaded before running the code
document.addEventListener("DOMContentLoaded", function () {

    // 🔍 Search functionality
    function handleSearch(event) {
        if (event.key === "Enter") {
            alert("Search functionality is not yet implemented.");
        }
    }

    const searchInput = document.querySelector("input[type='text']");
    searchInput.addEventListener("keypress", handleSearch);

    // 📘 Book Now button functionality
    function handleBookNowClick() {
        alert("Booking functionality is not yet implemented.");
    }

    const bookButtons = document.querySelectorAll(".book-btn");
    bookButtons.forEach(button => {
        button.addEventListener("click", handleBookNowClick);
    });

});
