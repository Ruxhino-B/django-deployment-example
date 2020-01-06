// //Problem 1: Sleeping in
// function sleepIn(weekday, vacation) {
//   if (!weekday || vacation) {
//     return true;
//   }
//   return false;
// }

//Problem 2: MONKEY TROUBLE
// function truble(asmile, bsmile) {
//   if (asmile && bsmile) {
//     return true;
//   }else if (!asmile && !bsmile) {
//     return true
//   }
//   return false;
// }

//Problem 3
// function stringTimes(str,n) {
//   var returnStr="";
//   var i=0;
//   while (i<n) {
//     returnStr=returnStr+str
//     i++
//   }
//   return returnStr;
// }
// function stringTimes(str,n) {
//   returnStr="";
//   for (var i = 0; i < n; i++) {
//     returnStr+= str;
//   }
//   return returnStr;
// }


//Problem 4
// function luckySum(a,b,c){
//   if (a == 13) {
//     return 0;
//   }else if (b == 13) {
//     return a;
//   }else if (c == 13) {
//     return(a+b);
//   }
//   return(a+b+c)
// }


// function caught_speeding(speed, is_birthday) {
//   if (is_birthday) {
//     speed-=5;
//   }
//   if (speed<60) {
//     return 0;
//     }
//   if (speed>60 && speed<80) {
//     return 1;
//   }
//   return 2;
// }


function makeBricks(small, big, goal) {
  return (goal%(small+big) == 0);
}
