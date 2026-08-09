// Theme toggle functionality
document.addEventListener('DOMContentLoaded', () => {
    const toggleCheckbox = document.getElementById("theme-toggle-checkbox");
    const html = document.documentElement;

    if (!toggleCheckbox) return;

    // Load saved theme from localStorage
    const savedTheme = localStorage.getItem("theme") || "light";
    html.setAttribute("data-theme", savedTheme);
    toggleCheckbox.checked = savedTheme === "dark";

    // Toggle theme on switch change
    toggleCheckbox.addEventListener("change", () => {
        if (toggleCheckbox.checked) {
            html.setAttribute("data-theme", "dark");
            localStorage.setItem("theme", "dark");
        } else {
            html.setAttribute("data-theme", "light");
            localStorage.setItem("theme", "light");
        }
    });
});