import "./App.css";
import Boton from "./componentes/Boton.jsx";
import freeCodeCampLogo from "./images/freecodecamp-logo.png";

function App() {
  const hacerClick = () => {
    console.log("Click");
  };

  const reiniciarContador = () => {
    console.log("Reinciar");
  };

  return (
    <div className="App">
      <div className="freecodecamp-logo-contenedor">
        <img
          className="freecodecamp-logo"
          src={freeCodeCampLogo}
          alt="Logo de freeCodeCamp"
        />
      </div>
      <div className="contenedor-principal">
        <Boton texto="Click" botonClick={true} manejarClick={hacerClick} />
        <Boton
          texto="Reiniciar"
          botonClick={false}
          manejarClick={reiniciarContador}
        />
      </div>
    </div>
  );
}

export default App;
