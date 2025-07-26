

// const buttons = [
//     { element: document.getElementById('twelve'), value: 0.12},
//     { element: document.getElementById('fifteen'), value: 0.18},
//     { element: document.getElementById('eighteen'), value: 0.18},
//     { element: document.getElementById('twenty'), value: 0.20},
//     { element: document.getElementById('twentyfive'), value: 0.25},
//     { 
//         element: document.getElementById('custom-tip-btn'), 
//         value: () => Number(document.getElementById('custom-tip').value) / 100 
//     }
// ]


// const numPeople = document.getElementById('total-people')
// const bill = document.getElementById('bill-amt')
// const totalBill = bill.value
// console.log(bill.value)

// function handleTipClick(tipPercentage) {
//     const billAmount = Number(bill.value)
//     const peopleCount = Number(numPeople.value)

//     if (!billAmount || !peopleCount) {
//         alert("Enter bill amount and number of people!")
//         return;
//     }


//     const tipAmount = billAmount * tipPercentage;
//     const withTip = billAmount + tipAmount;
//     const perPerson = withTip / Number(numPeople.value)
//     const rounded = Math.round(perPerson * 100) / 100 
//     document.getElementById('tip-answer').innerText = (`${tipAmount}`);
//     document.getElementById('total-per-person').innerText = (`${rounded}`)


// }

// buttons.forEach(buttonObj => {
//     buttonObj.element.addEventListener('click', () => {
//         // Get tip value dynamically (works for both preset and custom)
//         const tipValue = typeof buttonObj.value === 'function'
//             ? buttonObj.value()
//             : buttonObj.value;

//         // Validate custom tip (only if it's coming from input)
//         if (isNaN(tipValue) || tipValue <= 0) {
//             alert("Enter a valid custom tip percentage!");
//             return;
//         }

//         handleTipClick(tipValue);
//     });
// });

// document.getElementById('reset').addEventListener('click', () => {
//     // Clear inputs
//     bill.value = '';
//     numPeople.value = '';
//     document.getElementById('custom-tip').value = '';

//     // Reset displayed results
//     document.getElementById('tip-answer').innerText = '$0.00';
//     document.getElementById('total-per-person').innerText = '$0.00';
// });



// twelve.addEventListener('click', function() {
//     const tipAmount = Number(bill.value) * 0.12;
//     const withTip = Number(bill.value) + tipAmount;
//     const perPerson = withTip / Number(numPeople.value)
//     const rounded = Math.round(perPerson * 100) / 100 
//     document.getElementById('tip-answer').innerText = (`${tipAmount}`);
//     document.getElementById('total-per-person').innerText = (`${rounded}`)
// })
// 
const buttons = [
    { element: document.getElementById('twelve'), value: 0.12},
    { element: document.getElementById('fifteen'), value: 0.15},
    { element: document.getElementById('eighteen'), value: 0.18},
    { element: document.getElementById('twenty'), value: 0.20},
    { element: document.getElementById('twentyfive'), value: 0.25},
    { 
        element: document.getElementById('custom'), 
        value: () => Number(document.getElementById('custom').value) / 100 
    }
]


const numPeople = document.getElementById('total-people')
const bill = document.getElementById('bill-amt')
const totalBill = bill.value
console.log(bill.value)

function handleTipClick(tipPercentage) {
    const billAmount = Number(bill.value)
    const peopleCount = Number(numPeople.value)

    if (!billAmount || !peopleCount) {
        alert("Enter bill amount and number of people!")
        return;
    }


    const tipAmount = billAmount * tipPercentage;
    const withTip = billAmount + tipAmount;
    const perPerson = withTip / Number(numPeople.value)
    const rounded = Math.round(perPerson * 100) / 100 
    document.getElementById('tip-answer').innerText = (`${tipAmount}`);
    document.getElementById('total-per-person').innerText = (`${rounded}`)


}

buttons.forEach(buttonObj => {
    buttonObj.element.addEventListener('click', () => {
        // Get tip value dynamically (works for both preset and custom)
        const tipValue = typeof buttonObj.value === 'function'
            ? buttonObj.value()
            : buttonObj.value;

        // Validate custom tip (only if it's coming from input)
        if (isNaN(tipValue) || tipValue <= 0) {
            alert("Enter a valid custom tip percentage!");
            return;
        }

        handleTipClick(tipValue);
    });
});
// Reser Button Logic 
document.getElementById('reset').addEventListener('click', () => {
    // Clear inputs
    bill.value = '';
    numPeople.value = '';
    document.getElementById('custom-tip').value = '';

    // Reset displayed results
    document.getElementById('tip-answer').innerText = '$0.00';
    document.getElementById('total-per-person').innerText = '$0.00';

    // Remove active button highlight
    buttons.forEach(b => b.element.classList.remove('active'));
});