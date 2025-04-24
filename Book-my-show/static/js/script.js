document.addEventListener("DOMContentLoaded", function () {
    // 🔍 Search functionality
    function handleSearch(event) {
        if (event.key === "Enter") {
            const searchQuery = event.target.value.trim();

            if (searchQuery === "") {
                alert("Please enter a movie or event to search.");
                return;
            }

            // Call an API to search for movies or filter through a list
            fetch(`/api/search_movies?query=${searchQuery}`)
                .then(response => response.json())
                .then(movies => {
                    const movieListContainer = document.getElementById("movie-list");
                    movieListContainer.innerHTML = "";  // Clear current list
                    if (movies.length === 0) {
                        movieListContainer.innerHTML = "<p>No movies found.</p>";
                    } else {
                        movies.forEach(movie => {
                            const movieItem = document.createElement("div");
                            movieItem.classList.add("movie");
                            movieItem.innerHTML = `
                                <h3 class="movie-title">${movie.title}</h3>
                                <img src="${movie.image_url}" alt="${movie.title}">
                                <button class="book-btn" data-movie-id="${movie.id}">Book Now</button>
                            `;
                            movieListContainer.appendChild(movieItem);
                        });

                        // Re-add event listeners for "Book Now" buttons
                        const bookButtons = document.querySelectorAll(".book-btn");
                        bookButtons.forEach(button => {
                            button.addEventListener("click", handleBookNowClick);
                        });
                    }
                })
                .catch(error => {
                    console.error("Error fetching movies:", error);
                    alert("Failed to fetch movies.");
                });
        }
    }

    const searchInput = document.querySelector("input[type='text']");
    searchInput.addEventListener("keypress", handleSearch);

    // 📘 Book Now button functionality
    function handleBookNowClick(event) {
        const movieId = event.target.getAttribute("data-movie-id");

        // Redirect to the book page with the selected movie's ID
        window.location.href = `/book?movie_id=${movieId}`;
    }

    // Initializing the "Book Now" functionality for all buttons on page load
    const bookButtons = document.querySelectorAll(".book-btn");
    bookButtons.forEach(button => {
        button.addEventListener("click", handleBookNowClick);
    });
});
