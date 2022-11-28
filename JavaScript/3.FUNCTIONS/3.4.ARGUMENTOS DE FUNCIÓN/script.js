function fullName(firstName, lastName, language) {
    var language = language || 'Español';
    return lastName.toUpperCase() + ', ' + firstName.toUpperCase() + ' - ' + language;
}

fullName('Ekaitz', 'Campo');