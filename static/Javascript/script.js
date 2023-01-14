
// const TopWear = document.querySelector("#Top_wear");
// const TopList = document.querySelector(".Top_List");

// const BottomWear = document.querySelector("#Bottom_Wear");
// const BottomList = document.querySelector(".Bottom_List");

// TopWear.onclick = ()=>{
//     // TopList.classList.toggle("showtop")
//     document.getElementsByClassName("Top_List").style.display = "block";
// }
// BottomWear.onclick = ()=>{
//     // BottomList.classList.toggle("showbottom")
//     document.getElementsByClassName("Bottom_List").style.display = "block";
// }

let Wear = ["Top Wear","Bottom Wear"];
let TopWear = ["Shirt","T-Shirt","Kurta"];
let BottomWear = ["Jeans","Pajama","Lower"];

let slct1 = document.getElementById("slct1");
let slct2 = document.getElementById("slct2");

Wear.forEach(function addWear(item) {
    let option = document.createElement("option");
    option.text = item;
    option.value = item;
    slct1.appendChild(option);
});

slct1.onchange = function(){
    slct2.innerHTML = "<option></option>";
    if(this.value == "Top Wear"){
        addToSlct2(TopWear);
    }
    if(this.value == "Bottom Wear"){
        addToSlct2(BottomWear);
    }
}

function addToSlct2(arr) {
    arr.forEach(function(item){
        let option = document.createElement("option");
        option.text =item;
        option.value = item;
        slct2.appendChild(option);
    })
    
}

