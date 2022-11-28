<?php

$link = 'mysql:host=localhost;dbname=dbcolores';
$usuario = 'root';
$pass = 'Nalaoihane2002?';

try {

  $pdo = new PDO($link, $usuario, $pass);
} catch (PDOException $e) {
  print "¡Error!: " . $e->getMessage() . "<br/>";
  die();
}
