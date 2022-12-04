import React from "react";
import "../stylesheets/BotonClear.css";

class BotonClear extends React.Component {
  render() {
    return (
      <div className="boton-clear" onClick={this.props.manejarClear}>
        {this.props.children}
      </div>
    );
  }
}

export default BotonClear;
