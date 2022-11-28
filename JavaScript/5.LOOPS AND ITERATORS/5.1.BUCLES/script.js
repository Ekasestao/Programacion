var players = ["Altuve", "Bregman", "Correa", "Springer"];

/* for (var i = 0; i < players.length; i++) {
    console.log(players[i]);
} */

/* for (e in players) {
    console.log(players[e]);
} */

players.forEach(function (element) {
  console.log(element); //Más moderno y recomendado
});
