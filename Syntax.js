function addNumbers(a, b) {
    return a + b; ;
}

function execute(action){
  action()
}
//COMMENT
  /*
  Comment
  */
var integer = 12;
var flt = 12.3;
var a_string = "Hello";
var char = 'm'
var arr = [2,3,5,8];
var bool = false;
const PI = 3.14;
var a = 1, b = 2, c = a + b;
var tuples_using_arrays = ["int", 12, 12.3]
var operations = (12 + 12 -12 )/ 12 * 2
if (typeof a =='number'){
  console.log("a is a number");
}
bool = Boolean(a)
a_string = String(a)
a = Number(a_string)

var lambda = function(){console.log("Higher Order Functions")};
execute(lambda);

for (var i of arr){
  console.log(i);
}

var sum = 0;
for (var i = 0; i < arr.length; i++) {
    sum += arr[i];
}

var i = 1;                      // initialize
while (i < 100) {               // enters the cycle if statement is true
    i += 1;
}

if(a_string == String(a)){
  a = Number(a_string);
}

for (var i = 0; i < arr.length; i++) {
  if(i % 2 == 0){
    sum += arr[i];
  } else{
    sum -= arr[i];
  }

}
// delete a; // variable is not really deleted

console.log(a);             // write to the browser console
// document.write(a);          // write to the HTML
// alert(a);                   // output in an alert box
// confirm("Really?");         // yes/no dialog, returns true/false depending on user click
// prompt("Your age?","0");    // input dialog. Second argument i

arr.toString();
arr.join(",");
arr.pop();            // Last element
arr.push(12);
arr[arr.length] = 12; // Same as push
arr.shift();         // First element
arr.sort();
arr.unshift(15);
delete arr[0];
arr.splice(1,2);
arr.reverse();
arr.sort(function(a, b){return a > b })

try{
  throw "No actual error here. Move on.";
} catch(err){
  console.log(err);
} finally{
  console.log("This code executes regardless");
}

//Node.js code
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})
readline.question(`What's your name?`, (name) => {
  console.log(`Hi ${name}!`)
  readline.close()
})

for (var i = 0; i < 5; i++) {
  console.log(Math.random())
}

var fs = require('fs');
var readMe = fs.readFileSync('readMe.txt', 'utf8');
console.log(readMe);

//Standalone object
var user = {
  name:"John",
  email:"Doe@gmail.com",
  getName(){
    console.log(this.name);
  }
}
console.log(user.name);
var key = "name";
console.log(user[key]);
user.getName();
class User{
  constructor(name, email){
    this.name = name;
    this.email = email
  }
  getName(){
    return this.name;
  }
}
console.log(new User("John", "Doe@gmail.com").getName());
