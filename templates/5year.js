document.addEventListener("DOMContentLoaded", function () {
    const numOfPopups = 21;

// Loop through popups and attach event listeners
for (let i = 1; i <= numOfPopups; i++) {
    const popupId = `popup${i}`;

    // Open popup event listener
    document.querySelector(`#open-${popupId}`).addEventListener("click", function () {
        document.querySelector(`.${popupId}`).classList.add("active");
    });

    // Close popup event listener
    document.querySelector(`.${popupId} .close-btn${i}`).addEventListener("click", function () {
        document.querySelector(`.${popupId}`).classList.remove("active");
    });
}

});
