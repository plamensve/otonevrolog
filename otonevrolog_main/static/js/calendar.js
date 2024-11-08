document.addEventListener("DOMContentLoaded", function() {
    flatpickr("#calendar", {
        inline: true,
        enableTime: false,
        dateFormat: "Y-m-d",
        locale: {
            firstDayOfWeek: 1 // Започва седмицата от понеделник
        }
    });
});
