function clearscreen(){
    document.getElementById("result").value="";
}

function setscreenValue(value){
    document.getElementById("result").value+=value;
}

function calculateResult(){
    const resultElement = document.getElementById("result");
    const expression = resultElement.value.trim();

    if (expression === ''){
      resultElement.value= "Enter an Expression";
      return;
    }

    try{
        resultElement.value=eval(expression);
    } 
    catch (e){
        resultElement.value="Invalid expression";
    }
}