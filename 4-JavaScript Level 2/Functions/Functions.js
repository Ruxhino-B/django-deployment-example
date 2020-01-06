function hello() {
  console.log("hello world");
}


function helloYou(name) {
  console.log("Hello "+name+"!");
}


function addNum(num1,num2) {
  console.log(num1+num2);
}


// nqs e lejm bosh kjo nuk e nxjerr undefined por shkr emrin Ruxhino
// nderkoh qe nqs e therret funksionin helloSomeone(xhoana) funksioni nxjerr
Pershendetje xhoana.
function helloSomeone(name="Ruxhino") {
  console.log("Pershendetje "+name);
}


function formal(name="Sam", title="Sir") {
  console.log(title + " "+name);
}


function formal(name="Sam", title="Sir") {
  return title+ " "+name;
}


function timesFive(numInput) {
  var result = numInput * 5;
  return result
}

//GLOBAL SCOPE
var v = "GLOBAL V"
var stuff = "GLOBAL STUFF"

function fun(stuff) {
  console.log(v);
  stuff = "Ndryshuar stuff brenda funksionit"
  console.log(stuff);
}

fun();
console.log(stuff);
