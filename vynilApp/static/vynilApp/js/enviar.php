<?php
$usuario = $_POST['usuario'];
$name = $_POST['nombre'];
$password = $_POST['password'];
$mail = $_POST['correo'];
$phone = $_POST['telefono'];


$header = 'From: ' . $mail . " \r\n";
$header .= "X-Mailer: PHP/" . phpversion() . " \r\n";
$header .= "Mime-Version: 1.0 \r\n";
$header .= "Content-Type: text/plain";

$message = "Este mensaje fue enviado por: " . $name . " \r\n";
$message .= "Su nombre de usuario es: " . $usuario . " \r\n";
$message .= "Su e-mail es: " . $mail . " \r\n";
$message .= "Teléfono de contacto: " . $phone . " \r\n";
$message .= "Enviado el: " . date('d/m/Y', time());

$para = 'mt871486@gmail.com';
$asunto = 'Mensaje de registro';

mail($para, $asunto, utf8_decode($message), $header);

header("Location:index.html");
?>

