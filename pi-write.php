<?php

$pin = escapeshellarg($_GET['pin']);
$mode = escapeshellarg($_GET['io']);
$command = "sudo python pinwrite.py $mode $pin";

//echo($command);

$result = shell_exec($command);

echo($result);



?>
