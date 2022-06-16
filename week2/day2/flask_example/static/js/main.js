function hello(x){
    console.log("Hello World");
}

function taskHider(){
    let element = document.getElementById("task-box");
    element.classList.toggle("task-box"); 
}

function darkMode(){
    let element = document.body
    element.classList.toggle("bg-danger")
    element.classList.toggle("bg-dark")
}

function displayDate(){
    document.getElementById("date").innerHTML = Date();
}


