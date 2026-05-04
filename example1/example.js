/* function readNumber(){
    return prompt("Please enter the number: ");
}
function cube (n){
    return n*n*n;
}
let number=readNumber();

document.getElementById("question1").innerHTML="The cube of"+" "+number+" "+"is"+" "+cube(number);
*/





/*
function readNumber(){
    return prompt("Please enter the number: ");
}

function double(n){
    return n*2;
}

let number = readNumber();

document.getElementById("question2").innerHTML="The double of"+" "+number+" "+"is"+" "+double(number);
*/





/*
function readNumber(){
    return prompt("Please enter the number: ");
}
function evenOrOdd(n){
    if(n%2 == 0){
        return "Even";
    }
    else {
        return "Odd";
    }
    
}
let number=readNumber();
let result=evenOrOdd(number);

document.getElementById("question3").innerHTML=number+" "+"is"+result;
*/




/*
function readNumber(){
    return prompt("Please enter the number: ");
}
let sumtotal=0;
function sum(n){
    for(let i=0;i<=n;i++){
        sumtotal+=i;
    }
    return sumtotal;
}
let number= readNumber();
let result=sum(number);
document.getElementById("question4").innerHTML=result
*/



function readNumber() {
    return Number(prompt("Please enter the number: "));
}

function readPower() {
    return Number(prompt("Please enter the power: "));
}

function power(n, y) {
    let result = 1;

    for (let i = 1; i <= y; i++) {
        result *= n;
    }

    return result;
}

let number = readNumber();
let exponent = readPower();

let result = power(number, exponent);

document.getElementById("question5").innerHTML = result;


