function openForm(day, hour) {
    document.getElementById("appointmentModal").style.display = "flex";
    document.getElementById("day").value = day;
    document.getElementById("hour").value = hour;
}


function closeForm() {
    document.getElementById("appointmentModal").style.display = "none";
}