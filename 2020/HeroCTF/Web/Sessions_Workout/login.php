<?php
if(isset($_POST['username']) and isset($_POST['password'])){
    if($_POST['username'] == 'HeroCTFAREdaBest' && $_POST['password'] = 'ThisISASUPERPassword'){
        $msg = 'Great you login, gg! But this is not this kind of Local File Inclusion, try again :)';
    }else{
        $msg = 'Sorry but you don\'t seem to be an admin.';
    }
} 
?