<?php

// echo 'editar.php?id=1&color=success&descripción=este es un color verde';

$id = $_GET['id'];
$color = $_GET['color'];
$descripcion = $_GET['descripción'];

/* echo $id;
echo '<br>';
echo $color;
echo '<br>';
echo $descripcion; */

include_once 'conexion.php';

$sql_editar = 'UPDATE colores SET color = ?, descripción = ? WHERE id = ?';
$sentencia_editar = $pdo->prepare($sql_editar);
$sentencia_editar->execute(array($color, $descripcion, $id));

//Cerramos conexión entre base de datos y sentencia
$sentencia_editar = null;
$pdo = null;
header('location:index.php');
