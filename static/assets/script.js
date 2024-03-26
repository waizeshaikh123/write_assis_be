let ser = document.querySelector(".anchor ")
let services = document.querySelector(".services-section");

var a = 1;
ser.addEventListener("click" ,function(){
    if(a == 1){
        services.style.display = "block";
        a = 0;
    }
    else{
        services.style.display = "none"
        a = 1
    }
})

// $(function(){
//     $('.anchor').on('click', function() {
//         $('.services-section').css({
//             display:'block';
//         });
//     });
// });