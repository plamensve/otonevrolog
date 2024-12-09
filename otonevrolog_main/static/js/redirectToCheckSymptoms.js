function redirectToCheckSymptoms(pk, appointment_first_name, appointment_last_name) {
    if (!pk) {
        console.error("PK is undefined or null");
        return;
    }
    window.location.href = `/accounts/profile/${pk}/patient_symptoms/`;
}