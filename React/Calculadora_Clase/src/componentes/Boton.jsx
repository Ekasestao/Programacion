import React from "react";
import "../stylesheets/Boton.css";

class Boton extends React.Component {
  esOperador = (valor) => {
    return isNaN(valor) && valor !== "." && valor !== "=";
  };

  render() {
    return (
      <button
        className={`boton-contenedor ${
          this.esOperador(this.props.children) ? "operador" : ""
        }`.trim()}
        onClick={() => this.props.manejarClick(this.props.children)}
      >
        {this.props.children}
      </button>
    );
  }
}

export default Boton;
