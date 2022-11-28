/* function ageVerification(age) {
    if (age > 25) {
        console.log('Puede')
    } else {
        console.log('No puede')
    }
    age > 25 ? console.log('puede') : console.log('no puede') 
    
    let answer = age > 25 ? 'puede' : 'no puede'
    console.log(answer)
}

ageVerification() */

function adminControls(user) {
    /* if (user) {
        if (user.admin) {
            console.log('Controles');
        } else {
            console.log('Necesita admin');
        }
    } else {
        console.log('Necesitas logearte');
    } */

    let response = user ? (user.admin ? 'Controles' : 'Necesitas admin') : 'Necesitas logearte';
    console.log(response)
}

let userOne = {
    name:'Ekaitz',
    admin: true
}

let userTwo = {
    name:'Leo',
    admin: false
}

let userThree = null

adminControls(userThree);