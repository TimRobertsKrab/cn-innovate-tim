function hello(x){
    console.log("Hello World");
}

function taskHider(){
    let element = document.getElementById("task-box");
    element.classList.toggle("task-box"); 
}

function darkMode(){
    let element = document.getElementsByTagName("body");
    element.classList.toggle("bg-danger")
}

