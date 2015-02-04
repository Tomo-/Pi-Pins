<?php

$pin = $_GET['pin'];

$command = "sudo python pinread.py $pin";

$result = shell_exec($command);

echo($result);


?>
