<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Get form data
    $name    = htmlspecialchars(trim($_POST["name"]));
    $email   = htmlspecialchars(trim($_POST["email"]));
    $phone   = htmlspecialchars(trim($_POST["phone"]));
    $message = htmlspecialchars(trim($_POST["message"]));

    // Validate data (very basic)
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Invalid email format.";
        exit;
    }

    // Example: Send email (optional)
    $to = "your-email@charactersmile.shop"; // Replace with your email
    $subject = "New Message from Website Contact Form";
    $body = "Name: $name\nEmail: $email\nPhone: $phone\nMessage:\n$message";
    $headers = "From: $email";

    if (mail($to, $subject, $body, $headers)) {
        echo "Thank you! Your message has been sent.";
    } else {
        echo "Sorry, something went wrong. Try again later.";
    }

} else {
    echo "Invalid request.";
}
?>