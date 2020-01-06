var emr = prompt("Ju lutem shkruani Emrin");
var mbiemr = prompt("Ju lutem shkruani Mbiemrin");
var mosh = prompt("Shkruani Moshen");
var gjatsi= prompt("Shruani gjatesine");
var kafsh= prompt("Shrkuani emrin e qenit tuaj")
alert("Faleminderit shume per kohen tuaj")

var name = null;
var eage = null;
var hight = null;
var animal = null;

if (emr[0]===mbiemr[0]) {
  name = true;
}else {
  name = false;
}
if (mosh==27) {
  eage = true;
}else {
  eage = false;
}
if (gjatsi==175) {
  hight = true;
}else {
  hight = false;
}

if (kafsh[kafsh.length-1] === "y") {
  animal = true;
}else {
  animal= false;
}
if (name && eage && hight && animal) {
  console.log("Ti je spiuni e un jam i lumtur");
}else {
  console.log("Ska asgje interesante");
}
