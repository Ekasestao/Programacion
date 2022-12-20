let mensaje: string = "Hola Mundo";

mensaje = "Chanchito feliz";

mensaje = "Chao Mundo";

console.log(mensaje);
console.log(typeof []);

/**
 * Tipos JS
 * number
 * string
 * boolean
 * null
 * undefined
 * object
 * function
 *
 * Tipos TS
 * any (No usar)
 * unknown
 * never
 * arrays
 * tuplas
 * Enums
 *
 * Tipos inferidos
 */

let extincionDinosaurios = 76_000_000;
let dinosaurioFavorito = "T-rex";
let extintos = true;

function canchitoFeliz(config: any) {
  return config;
}

let animales: string[] = ["chanchito", "feliz", "felipe"];
let nums: number[] = [1, 2, 3];
let checks: boolean[] = [];
let num2: Array<number> = [];

// animales.map(x => x.) Sugiere tipo de dato

let tupla: [number, string[]] = [1, ["chanchito feliz", "chanchito felipe"]];

const chica = "s",
  mediana = "m",
  grande = "l",
  extragrande = "xl";

enum Talla {
  Chica = "s", //n
  Mediana = "m", //n+1
  Grande = "l", //n+2
  ExtraGrande = "xl", //n+3
}

const variable1 = Talla.Grande;
console.log(variable1);

const enum LoadingState { //Const antes de Enum para que el código JS quede más optimizado
  Idle,
  Loading,
  Success,
  Error,
}

const estado = LoadingState.Success; //Const variable para saber el valor de cada Enum

// Type para crear un tipo personalizado
type Direccion = {
  numero: number;
  calle: string;
  pais: string;
};

type Persona = {
  readonly id: number; //Readonly para no poder cambiar el valor
  nombre?: string; //Poner ? para hacerla opcional
  talla: Talla;
  direccion?: Direccion;
};

const objeto: Persona = {
  id: 1,
  talla: Talla.Mediana,
};
objeto.nombre = "Hola Mundo"; //Añadir al objeto
objeto.direccion = {
  numero: 1,
  calle: "Sotera de la Mier",
  pais: "España",
};

const arr: Persona[] = [];
console.log(objeto);
