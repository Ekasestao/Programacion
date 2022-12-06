// npm i prop-types
import PropTypes from "prop-types";

Componente.PropTypes = {
  nombreProp: PropTypes.tipoDeDato.isRequired, // Tipo de dato: string, number, boolean...
};

Componente.defaultProps = {
  nombreProp: "Valor por defecto",
};
