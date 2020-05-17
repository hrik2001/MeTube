const container = document.getElementsByTagName("BODY")[0];
const button=document.querySelector("#but");
const heading=document.querySelector("#heading");
const para =document.querySelector("#para");


var selected_theme = localStorage.getItem("theme");

if(selected_theme =="dark"){
     console.log(selected_theme);
     button.checked=true;
     dark_theme();
}
else{
    console.log("none");
}


button.addEventListener("change", dark_theme);


function dark_theme(){
   


  
 
    if(button.checked){
        localStorage.setItem("theme","dark");
        console.log("helo");
        
        heading.classList.add("text-color-white");

        para.classList.add("color-white");
        container.classList.add("color-black");
    
    }
    else{
        localStorage.setItem("theme","normal");
        console.log("hi");
        heading.classList.remove("text-color-white");
        para.classList.remove("color-white");
        container.classList.remove("color-black");}

    }
