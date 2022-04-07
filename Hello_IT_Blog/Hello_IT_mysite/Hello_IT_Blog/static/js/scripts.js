//Skrypt do przewijania w górę przy pomocy guzika
button = document.getElementsByClassName("btn_top");
window.onscroll = function() {scrollFunction()};

function scrollFunction(){
    for(var i=0;i<button.length;i++){
        if(document.body.scrollTop > 250 || document.documentElement.scrollTop > 250){
            button[i].style.display = "block";
        } else {
            button[i].style.display = "none";
        }
    }
}

function GoUp(){
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

//Skrypt do ukrywania i pokazywania divów na stronie "O nas"
function showDetails(pk) {
var class_name = document.getElementsByClassName("card");
    for(var i=0;i<class_name.length;i++) {
        if(class_name[i].id == pk){
            if(class_name[i].style.display == "none"){
                class_name[i].style.display = "block"
            }else{
                class_name[i].style.display = "none"
            }
        }
        else
            class_name[i].style.display = "none";
    }
}