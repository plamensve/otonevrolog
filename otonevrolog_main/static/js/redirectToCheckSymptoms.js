function redirectToCheckSymptoms(pk, appointment_pk) {
    if (!pk) {
        console.error("PK is undefined or null");
        return;
    }
    window.location.href = `/accounts/profile/${pk}/patient_symptoms/`;
}