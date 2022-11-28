var age = 16;

if (age <= 10) {
    console.log('Kid')
    console.log('Not drive')
    console.log('Not rent')
} else if (age >= 16 && age < 25) {
    console.log('Not kid')
    console.log('Drive')
    console.log('Rent')
} else if (age >= 25) {
    console.log('No kid')
    console.log('Drive')
    console.log('Rent')
}