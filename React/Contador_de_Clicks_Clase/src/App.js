import React from "react";
import "./App.css";
import Boton from "./componentes/Boton.jsx";
import Contador from "./componentes/Contador.jsx";
import freeCodeCampLogo from "./images/freecodecamp-logo.png";

class App extends React.Component {
  constructor() {
    super();
    this.state = { numClicks: 0 };
    this.hacerClick = this.hacerClick.bind(this);
    this.reiniciarContador = this.reiniciarContador.bind(this);
  }

  hacerClick() {
    this.setState(({ numClicks }) => ({ numClicks: numClicks + 1 }));
  }

  reiniciarContador() {
    this.setState({ numClicks: 0 });
  }

  render() {
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
          <Contador numClicks={this.state.numClicks} />
          <Boton
            texto="Click"
            botonClick={true}
            manejarClick={this.hacerClick}
          />
          <Boton
            texto="Reiniciar"
            botonClick={false}
            manejarClick={this.reiniciarContador}
          />
        </div>
      </div>
    );
  }
}

export default App;
