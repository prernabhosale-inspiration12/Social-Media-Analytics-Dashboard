console.log("Dashboard Loaded");

// ==========================
// Sidebar
// ==========================
function toggleSidebar() {
    document.querySelector(".sidebar").classList.toggle("active");
}

// ==========================
// Dark Mode
// ==========================
function toggleTheme() {

    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("theme", "dark");
    } else {
        localStorage.setItem("theme", "light");
    }
}

// Load Saved Theme
window.onload = function () {

    let theme = localStorage.getItem("theme");

    if (theme === "dark") {
        document.body.classList.add("dark-mode");
    }

    // Start Counter Animation
    startCounters();
};

// ==========================
// Animated Counter
// ==========================
function startCounters() {

    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {

        counter.innerText = "0";

        const target = Number(counter.dataset.target);

        const updateCounter = () => {

            const current = Number(counter.innerText);

            const increment = Math.ceil(target / 50);

            if (current < target) {

                counter.innerText = Math.min(current + increment, target);

                setTimeout(updateCounter, 30);

            } else {

                counter.innerText = target;

            }

        };

        updateCounter();

    });

}
// ==========================
// Search Recent Posts
// ==========================

const searchInput = document.getElementById("searchInput");

if (searchInput) {

    searchInput.addEventListener("keyup", function () {

        const filter = this.value.toLowerCase();

        const rows = document.querySelectorAll("table tbody tr");

        rows.forEach(row => {

            const text = row.innerText.toLowerCase();

            row.style.display = text.includes(filter) ? "" : "none";

        });

    });

}