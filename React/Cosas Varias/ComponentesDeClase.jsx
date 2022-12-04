import React from "react";

class NombreComponente extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      completada: true,
      color: azul,
      prioridad: 1,
    };
    this.setState({
      completada: false,
      color: verde,
      prioridad: 2,
    });
  }

  render() {
    return (
      <h1>
        {this.props.nombreDelProp}
        {this.state.nombrePropiedad}
      </h1>
    );
  }
}
