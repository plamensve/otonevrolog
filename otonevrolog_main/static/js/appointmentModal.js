function openForm(day, hour) {
    document.getElementById("appointmentModal").style.display = "flex";
    document.getElementById("day").value = day;
    document.getElementById("hour").value = hour;
}

function validateAndSubmitForm(event) {
    event.preventDefault();
    const form = document.getElementById("appointmentForm");

    if (form.checkValidity()) {
        // Изпраща формата само ако е валидна
        form.submit();
    } else {
        // Показва съобщения за грешки, без да затваря модала
        form.reportValidity();
    }
}

function closeForm() {
    document.getElementById("appointmentModal").style.display = "none";
}
