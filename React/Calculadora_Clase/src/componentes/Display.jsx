import React from "react";
import "../stylesheets/Display.css";

class Display extends React.Component {
  render() {
    return <div className="input">{this.props.input}</div>;
  }
}

export default Display;
