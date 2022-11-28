var data = 66;

switch (typeof data) {
    case 'string':
        console.log('String')
        break;
    case 'number':
        console.log('Number')
        break;
    case 'boolean':
        console.log('Bollean')
        break;
    default:
        console.log('No')
}