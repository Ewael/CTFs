<?php
    session_start();
    if (!isset($_SESSION["logged_in"]) || $_SESSION["logged_in"] !== "logged")
    {
        header("Location: /login.php");
        die();
    }
?>