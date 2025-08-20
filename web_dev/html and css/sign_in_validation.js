// Function to validate form inputs
function validate() {
    let f_name = document.getElementById("first-name").value.trim();
    let m_name = document.getElementById("middle-name").value.trim();
    let l_name = document.getElementById("last-name").value.trim();
    let email = document.getElementById("email").value.trim();
    let aadhar = document.getElementById("Aadhar").value.trim();
    let phone = document.getElementById("Phone").value.trim();
    let password = document.getElementById("password").value.trim();
    let confirm_password = document.getElementById("confirm-password").value.trim();

    // Validate First Name
    if (f_name === "") {
        alert("Enter first name");
        return false;
    }

    // Validate Middle Name
    if (m_name === "") {
        alert("Enter middle name");
        return false;
    }

    // Validate Last Name
    if (l_name === "") {
        alert("Enter last name");
        return false;
    }

    // Validate Email with Regular Expression
    let email_regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email_regex.test(email)) {
        alert("Invalid email ID");
        return false;
    }

    // Validate Aadhar Number (12 Digits)
    if (aadhar.length !== 12 || isNaN(aadhar)) {
        alert("Not a valid Aadhar number");
        return false;
    }

    // Validate Phone Number (10 Digits)
    let phone_regex = /^[0-9]\d{9}$/; // Indian phone numbers start with 6-9
    if (!phone_regex.test(phone)) {
        alert("Invalid phone number");
        return false;
    }

    // Validate Password Length
    if (password.length < 6 || password.length > 12) {
        alert("Password should be between 6 to 12 characters.");
        return false;
    }

    // Confirm Password Match
    if (password !== confirm_password) {
        alert("Passwords do not match");
        return false;
    }

    return true;  // If all validations pass
}


// Attach validation function to the submit button
document.getElementById("Submit_Button").addEventListener("click", function(event) {
    if (!validate()) {
        event.preventDefault();  // Prevent form submission if validation fails
    }
    else {
        alert("Submission Successful");
    }
});

