var employee = {
  name: "John Smith",
  job: "Programer",
  age: 31,
  nameLength: function() {
    console.log(this.name.length);
  }
}


var employee = {
  name: "John Smith",
  job: "Programer",
  age: 31,
  namePrint: function() {
    alert("Name is " + this.name + ", Job is " +this.job + ", age is "+this.age)
  }
}


var employee = {
  name: "John Smith",
  job: "Programer",
  age: 31,
  namePrint: function() {
    array = this.name.split(" ")
    console.log("Last name is" +array[1]);
  }
}
