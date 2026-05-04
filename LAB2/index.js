function readNumber(){
    return prompt("Please enter the number: ");
}
function square(n){
    return n*n;
}
function factorial(n){
    if(n==0 || n==1){
        return 1;
    }
    return factorial(n-1)*n;
}

let number = readNumber();

document.getElementById("question1").innerHTML="The square of"+number+"is"+square(number);
document.getElementById("question2").innerHTML="The factorial of"+number+"is"+factorial(number);