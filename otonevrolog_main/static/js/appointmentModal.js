function validateAndSubmitForm(event) {
    event.preventDefault(); // Спира стандартното поведение на формата
    const form = document.getElementById("appointmentForm");

    if (form.checkValidity()) {
        // Асинхронно изпращане на формата
        const formData = new FormData(form);
        fetch(form.action, {
            method: form.method,
            body: formData,
            headers: {
                "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
            },
        })
            .then((response) => {
                if (response.ok) {
                    // Показва втория модален прозорец при успешна заявка
                    document.getElementById("surveyModal").style.display = "flex";
                } else {
                    alert("Failed to submit the form. Please try again.");
                }
            })
            .catch((error) => {
                console.error("Error submitting the form:", error);
                alert("An error occurred. Please try again.");
            });
    } else {
        // Показва съобщения за грешки и скрива втория модален прозорец
        form.reportValidity();
        document.getElementById("surveyModal").style.display = "none";
    }
}

function openForm(day, hour) {
    document.getElementById("appointmentModal").style.display = "flex";
    document.getElementById("day").value = day;
    document.getElementById("hour").value = hour;
}

function closeForm() {
    document.getElementById("appointmentModal").style.display = "none";
}
