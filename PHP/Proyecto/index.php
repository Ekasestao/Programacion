<?php

include_once 'conexion.php';

//LEER
$sql_leer = 'SELECT * FROM colores';

$gsent = $pdo->prepare($sql_leer);
$gsent->execute();

$resultado = $gsent->fetchAll();

//var_dump($resultado);

//AGREGAR
if ($_POST) {
  $color = $_POST['color'];
  $descripcion = $_POST['descripción'];

  $sql_agregar = 'INSERT INTO colores (color, descripción) VALUES (?,?)';
  $sentencia_agregar = $pdo->prepare($sql_agregar);
  $sentencia_agregar->execute(array($color, $descripcion));

  //Cerramos conexión entre base de datos y sentencia
  $sentencia_agregar = null;
  $pdo = null;
  header('location:index.php');
}

if ($_GET) {
  $id = $_GET['id'];

  $sql_unico = 'SELECT * FROM colores WHERE id=?';
  $gsent_unico = $pdo->prepare($sql_unico);
  $gsent_unico->execute(array($id));
  $resultado_unico = $gsent_unico->fetch();

  //
  $gsent_unico = null;
}

?>

<!doctype html>
<html lang="es">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Proyecto</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
  <script src="https://kit.fontawesome.com/ea909c5d2d.js" crossorigin="anonymous"></script>
</head>

<body>

  <div class="container mt-5">

    <div class="row">

      <div class="col-md-6">

        <?php foreach ($resultado as $dato) : ?>

          <div class="alert alert-<?php echo $dato['color'] ?> text-uppercase" role="alert">

            <?php echo $dato['color'] ?>
            -
            <?php echo $dato['descripción'] ?>

            <a href="eliminar.php?id=<?php echo $dato['id'] ?>" class="float-end me-1 text-decoration-none">

              <i class="fa-solid fa-trash"></i>

            </a>

            <a href="index.php?id=<?php echo $dato['id'] ?>" class="float-end me-3 text-decoration-none">

              <i class="fa-regular fa-pen-to-square"></i>

            </a>

          </div>

        <?php endforeach ?>

      </div>

      <div class="col-md-6">

        <?php if (!$_GET) : ?>

          <h2>AGREGAR ELEMENTOS</h2>

          <form method="POST">

            <input type="text" class="form-control" name="color">

            <input type="text" class="form-control mt-3" name="descripción">

            <button class="btn btn-primary mt-3">Agregar</button>

          </form>

        <?php endif ?>

        <div class="col-md-6">

          <?php if ($_GET) : ?>

            <h2>EDITAR ELEMENTOS</h2>

            <form method="GET" action="editar.php">

              <input type="text" class="form-control" name="color" value="<?php echo $resultado_unico['color'] ?>">

              <input type="text" class="form-control mt-3" name="descripción" value="<?php echo $resultado_unico['descripción'] ?>">

              <input type="hidden" name="id" value="<?php echo $resultado_unico['id'] ?>">

              <button class="btn btn-primary mt-3">Agregar</button>

            </form>

          <?php endif ?>

        </div>

      </div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>

</body>

</html>

<?php

//Cerramos conexión entre base de datos y sentencia
$pdo = null;
$gsent = null;

?>