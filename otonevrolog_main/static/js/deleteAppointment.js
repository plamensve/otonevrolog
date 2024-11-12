function openModal(appointmentId) {
    document.getElementById("confirmModal").style.display = "flex";
    document.getElementById("confirmDelete").onclick = function(event) {
        event.preventDefault(); // Предотвратява презареждането на формуляра
        deleteAppointment(appointmentId);
    };
}

function closeModal() {
    document.getElementById("confirmModal").style.display = "none";
}

function deleteAppointment(appointmentId) {
    console.log("Deleting appointment..."); // Проверка дали функцията се извиква
    fetch(`/patient/delete_appointment/${appointmentId}/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // Показва отговора от сървъра в конзолата
        if (data.success) {
            closeModal(); // Затваря модалния прозорец
            window.location.reload();
            document.getElementById(`appointment-${appointmentId}`).remove(); // Премахва елемента от DOM
             // Презарежда страницата
        } else {
            alert(data.error || "Failed to delete appointment.");
        }
    })
    .catch(error => console.error('Error:', error));
}

