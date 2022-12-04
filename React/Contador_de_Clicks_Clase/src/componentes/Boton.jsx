import React from "react";
import "../stylesheets/Boton.css";

class Boton extends React.Component {
  render() {
    return (
      <button
        className={this.props.botonClick ? "boton-click" : "boton-reiniciar"}
        onClick={this.props.manejarClick}
      >
        {this.props.texto}
      </button>
    );
  }
}

export default Boton;
