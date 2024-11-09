function openForm(day, hour) {
    document.getElementById("appointmentModal").style.display = "flex";
    document.getElementById("day").value = day;
    document.getElementById("hour").value = hour;
}

function validateAndSubmitForm(event) {
    event.preventDefault();
    const form = document.getElementById("appointmentForm");

    if (form.checkValidity()) {
        form.submit(); // Изпраща формата само ако е валидна
    } else {
        form.reportValidity(); // Показва съобщения за грешка, без да затваря модала
    }
}

function closeForm() {
    document.getElementById("appointmentModal").style.display = "none";
}
