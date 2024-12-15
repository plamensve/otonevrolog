function openForm(day, hour) {
    const modal = document.getElementById("appointmentModal");
    if (modal) {
        modal.style.display = "flex";
        document.getElementById("day").value = day;
        document.getElementById("hour").value = hour;
    }
}



function validateAndSubmitForm(event) {
    event.preventDefault();
    const form = document.getElementById("appointmentForm");
    if (!form) return;

    if (form.checkValidity()) {
        const formData = new FormData(form);
        fetch(form.action, {
            method: form.method,
            body: formData,
            headers: {
                "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")?.value || "",
            },
        })
        .then((response) => {
            if (response.ok) {
                const surveyModal = document.getElementById("surveyModal");
                const formModal = document.getElementById("formModal"); // ID на модалния прозорец

                if (surveyModal) {
                    surveyModal.style.display = "flex";
                }

                if (formModal) {
                    formModal.style.display = "none"; // Скриване на формата след събмит
                }

                form.reset(); // Изчистване на данните във формата
            } else {
                return response.text().then((text) => {
                    alert(`Failed to submit the form: ${text}`);
                });
            }
        })
        .catch(() => alert("An error occurred. Please try again."));
    } else {
        form.reportValidity();
    }
}


document.addEventListener("DOMContentLoaded", () => {
    const closeButton = document.getElementById("closeForm");
    if (closeButton) {
        closeButton.addEventListener("click", () => {
            const modal = document.getElementById("appointmentModal");
            if (modal) {
                modal.style.display = "none";
                console.log("Modal closed");
            }
        });
    } else {
        console.error("Close button not found");
    }
});
