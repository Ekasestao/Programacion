var student = {
    name: 'Ekaitz',
    age: 12,
    city: 'Sestao'
};

for (var key in student) {
    console.log(key + ' => ' + student[key]);
}