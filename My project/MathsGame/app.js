let score = 0;
let timer ;
let correctAnswer;
let level=1;
let time=0;

function generateEquation() {
    // generate two random numbers between 1 to 10
    const num1 = Math.floor(Math.random()*10)+1
    const num2 = Math.floor(Math.random()*10)+1

    // select a random operator
    operators = ["+","-","*","/"]
    const operator = operators[Math.floor(Math.randow() *
        operators.length
        )]
        let equation = num1 +" "+operator +" "+ num2 +" =?"
        document.getElementById("equation").innerText=equation;

        switch (operator){
            case '+':
                correctAnswer = Number(num1)+Number(num2)
                break
        case '-':
                correctAnswer = Number(num1)-Number(num2)
                break
         case '*':
                correctAnswer = Number(num1)*Number(num2)
                break
        case '/':
                correctAnswer = Number(num1)/Number(num2)
                break

        }
        console.log("correct answer: ",correctAnswer)
    
}
generateEquation()