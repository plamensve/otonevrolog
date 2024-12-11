// function validateAndSubmitForm(event) {
//     event.preventDefault();
//     const form = document.getElementById("appointmentForm");
//     const profilePk = document.getElementById("profile-pk").value;
//
//     if (form.checkValidity()) {
//         // Показваме модалния прозорец
//         document.getElementById("surveyModal").style.display = "flex";
//
//         // При натискане на "Yes"
//         document.getElementById("survey-yes").onclick = async function () {
//             const formData = new FormData(form);
//
//             try {
//                 const response = await fetch(form.action, {
//                     method: form.method,
//                     body: formData,
//                     headers: {
//                         "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
//                     },
//                 });
//
//                 if (response.ok) {
//                     // След успешното изпращане, пренасочваме
//                     window.location.href = `/accounts/profile/${profilePk}/ask/`;
//                 } else {
//                     alert("Failed to save appointment. Please try again.");
//                 }
//             } catch (error) {
//                 console.error("Error submitting form:", error);
//                 alert("An error occurred. Please try again.");
//             }
//         };
//
//         // При натискане на "No"
//         document.getElementById("survey-no").onclick = async function () {
//             try {
//                 const formData = new FormData(form);
//                 const response = await fetch(form.action, {
//                     method: form.method,
//                     body: formData,
//                     headers: {
//                         "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
//                     },
//                 });
//
//                 if (response.ok) {
//                     alert("Appointment saved successfully.");
//                     document.getElementById("surveyModal").style.display = "none";
//                 } else {
//                     alert("Failed to save appointment. Please try again.");
//                 }
//             } catch (error) {
//                 console.error("Error submitting form:", error);
//                 alert("An error occurred. Please try again.");
//             }
//         };
//     } else {
//         // Показваме грешки и скриваме `surveyModal`
//         form.reportValidity();
//         document.getElementById("surveyModal").style.display = "none";
//     }
// }
