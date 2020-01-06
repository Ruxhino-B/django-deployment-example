// var nr1 = document.querySelector("#nr1")
// var nr2 = document.querySelector("#nr2")
// var nr3 = document.querySelector("#nr3")
// var nr4 = document.querySelector("#nr4")
// var nr5 = document.querySelector("#nr5")
// var nr6 = document.querySelector("#nr6")
// var nr7 = document.querySelector("#nr7")
// var nr8 = document.querySelector("#nr8")
// var nr9 = document.querySelector("#nr9")

//Kap butonin i cili ka id #
var restart = document.querySelector("#b")

//Kap te gjitha katroret
var katror = document.querySelectorAll("td")

//Per te fshire te gjith katroret
function fshiKatroret() {
  for (var i = 0; i < katror.length; i++) {
    katror[i].textContent = '';
  }
}

restart.addEventListener("click",fshiKatroret);

//Kontrollon nqs jan plotesuar katroret

function katrorNdrysho() {
  if (this.textContent === '') {
    this.textContent = 'X';
  }else if (this.textContent === 'X') {
    this.textContent = 'O';
  }else {
    this.textContent ='';
  }
}

for (var i = 0; i < katror.length; i++) {
  katror[i].addEventListener('click',katrorNdrysho)
}



// nr1.addEventListener("click",function () {
//   if (nr1.textContent === '') {
//     nr1.textContent = 'X';
//   }else if (nr1.textContent === 'X') {
//     nr1.textContent = 'O';
//   }else {
//     nr1.textContent = '';
//   }
// })
//
//
//   nr2.addEventListener("click",function () {
//     if (nr2.textContent === '') {
//       nr2.textContent = 'X';
//     }else if (nr1.textContent === 'X') {
//       nr2.textContent = 'O';
//     }else {
//       nr2.textContent = '';
//     }
//   })
//
//       nr3.addEventListener("click",function () {
//         if (nr3.textContent === '') {
//           nr3.textContent = 'X';
//         }else if (nr1.textContent === 'X') {
//           nr3.textContent = 'O';
//         }else {
//           nr3.textContent = '';
//         }
//       })
//
//
//         nr4.addEventListener("click",function () {
//           if (nr4.textContent === '') {
//             nr4.textContent = 'X';
//           }else if (nr1.textContent === 'X') {
//             nr4.textContent = 'O';
//           }else {
//             nr4.textContent = '';
//           }
//         })
//
//           nr5.addEventListener("click",function () {
//             if (nr5.textContent === '') {
//               nr5.textContent = 'X';
//             }else if (nr5.textContent === 'X') {
//               nr5.textContent = 'O';
//             }else {
//               nr5.textContent = '';
//             }
//           })
//
//             nr6.addEventListener("click",function () {
//               if (nr6.textContent === '') {
//                 nr6.textContent = 'X';
//               }else if (nr6.textContent === 'X') {
//                 nr6.textContent = 'O';
//               }else {
//                 nr6.textContent = '';
//               }
//             })
//
//               nr7.addEventListener("click",function () {
//                 if (nr7.textContent === '') {
//                   nr7.textContent = 'X';
//                 }else if (nr7.textContent === 'X') {
//                   nr7.textContent = 'O';
//                 }else {
//                   nr7.textContent = '';
//                 }
//               })
//
//                 nr8.addEventListener("click",function () {
//                   if (nr8.textContent === '') {
//                     nr8.textContent = 'X';
//                   }else if (nr1.textContent === 'X') {
//                     nr8.textContent = 'O';
//                   }else {
//                     nr8.textContent = '';
//                   }
//                 })
//
//                   nr9.addEventListener("click",function () {
//                     if (nr9.textContent === '') {
//                       nr9.textContent = 'X';
//                     }else if (nr9.textContent === 'X') {
//                       nr9.textContent = 'O';
//                     }else {
//                       nr9.textContent = '';
//                     }
//                   })
