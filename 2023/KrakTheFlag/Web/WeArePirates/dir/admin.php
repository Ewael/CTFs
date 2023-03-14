<?php


    include('includes/conn.php');    
    require 'includes/config.php';
    require 'includes/functions.php';
    require 'includes/user.php';


    $user = unserialize($_COOKIE["user_info"]);
    if (!$user->is_admin)
    {
        header("Location: /");
        die();
    }


   
    include('includes/admin_stuff.php');
    $user = unserialize($_COOKIE["user_info"]);
    if (!$user->is_admin)
    {
        header("Location: /");
        die();
    }

    $admin_name = $user->get_name();


    /*
     * checking processes, I'll add more for more informations accessible from admin page
     */

    $status_checker = new CheckStatus();
    $status_checker->status = "df -h /";
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
        <h1>Admin Page</h1>
    </header>

    <article>
        <h2 style="color: blue;">Welcome <?php echo $admin_name ?></h2>
        <h3>FileSystem Status:</h3>
        <code style="white-space: pre-line"><?php echo $status_checker; ?></code>
        <br><br>
        Other Status check incomming....


        
    </article>

    <footer>
        <small>&copy;<?php echo date('Y'); ?> <?php site_name(); ?>.<br><?php site_version(); ?></small>
    </footer>

</div>
</body>
</html>