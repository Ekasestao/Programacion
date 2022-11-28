var user = { 
    name: 'Ekaitz',
    age: 12,
    city: 'Sestao',
    grades: {
        math: 90,
        science: 80,
        languaje: 100
    }
};
user.grades.coding = 99;
console.log(user.grades);