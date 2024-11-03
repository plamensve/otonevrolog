function openModal(appointmentId) {
    document.getElementById("confirmModal").style.display = "flex";
    document.getElementById("confirmDelete").onclick = function() {
        deleteAppointment(appointmentId);
    };
}

function closeModal() {
    document.getElementById("confirmModal").style.display = "none";
}

function deleteAppointment(appointmentId) {
    fetch(`/patient/delete_appointment/${appointmentId}/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
    })
    .then(response => {
        if (response.ok) {
             window.location.href = "/";  // Презарежда страницата, ако изтриването е успешно
        } else {
            alert("Failed to delete appointment.");
        }
    })
    .catch(error => console.error('Error:', error));
}

