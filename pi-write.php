<?php

$pin = $_GET['pin'];
$mode = $_GET['io'];
$command = "sudo python pinwrite.py $mode $pin";

//echo($command);

$result = shell_exec($command);

echo($result);



?>
