<?php

    require 'includes/config.php';
    require 'includes/functions.php';
    require 'includes/user.php';

    $error = "";
    /* 
     * Guest login for now is sufficient 
    */
    if ($_SERVER['REQUEST_METHOD'] === "POST")
    {
           if (isset($_POST["password"]) && isset($_POST["login"]))
           {
            if ($_POST["password"] === "Guest" && $_POST["login"] === "Guest")
            {
                session_start();
                $_SESSION["logged_in"] = "logged";
                $user = new User();
                $user->is_admin = false;
                $user->name = "Guest";
                setcookie("user_info",serialize($user));
                header("Location: /");
            }
            
           } 
           else
            {
                $error = "Please log in as Guest for now, we will add a real login page later";
            }
    }

?>


<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"/>
    <link rel="icon" type="image/x-icon" href="https://tse1.mm.bing.net/th?id=OIP.qzbYkGfWIt2E6sBB3cM1fwHaFj&pid=Api&f=1&ipt=e2aea0981c52fdf01cb0854f1f29001a06020cee54f7fa76ee818e280815ba1a&ipo=images">
    <title><?php page_title(); ?> | <?php site_name(); ?></title>
    <link href="<?php site_url(); ?>/template/style.css" rel="stylesheet" type="text/css" /> 
</head>
<body>
<div class="wrap">

    <header>
        <h1>Login page</h1>
    </header>
    <img src="https://tse1.mm.bing.net/th?id=OIP.qzbYkGfWIt2E6sBB3cM1fwHaFj&pid=Api&f=1&ipt=e2aea0981c52fdf01cb0854f1f29001a06020cee54f7fa76ee818e280815ba1a&ipo=images">
    <article>
        <h2>Please log in, for now only guest login available</h2>
        <h4 style="color: red;"><?php echo $error; ?></h4>
        <form action="" method="post">
                 <label for="login">Username:</label>
                 <input type="text" id="login" name="login" value="Guest">
                 <br><br>
                 <label for="password">Password:</label>
                 <input type="password" id="password" name="password" value="Guest">
                 <br><br>
                 <input type="submit" value="Submit">
         </form>
        
    </article>

    <footer>
        <small>&copy;<?php echo date('Y'); ?> <?php site_name(); ?>.<br><?php site_version(); ?></small>
    </footer>

</div>
</body>
</html>