//1..0 Variables
//COMMENT
/*
Multiline Comment
*/
//1..1 Variable types
var integer = 12;
var flt = 12.3;
var a_string = "Hello";
var chr = 'm';
var bool = false;
const PI = 3.14;
var a = 1, b = 2, c = a + b;
// delete a; // variable is not really deleted

//Operations
var operations = (12 + 12 -12 )/ 12 * 2;
console.log(a_string + " World!\n");
console.log(Math.floor(11/3));

// Type and type casting
if (typeof a =='number'){
  console.log("a is a number");
}
bool = Boolean(a)
a_string = String(a)
a = Number(a_string)

//Other Variable types
var tuples_using_arrays = ["int", 12, 12.3];
var arr = [2,3,5,8];

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

//2..0 INPUT/OUTPUT
console.log(a);             // write to the browser console
// document.write(a);          // write to the HTML
// alert(a);                   // output in an alert box
// confirm("Really?");         // yes/no dialog, returns true/false depending on user click
// prompt("Your age?","0");    // input dialog. Second argument i

//Node.js code
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})
readline.question(`What's your name?\n`, (name) => {
  console.log(`Hi ${name}!`)
  readline.close()
})

var fs = require('fs');
var readMe = fs.readFileSync('readMe.txt', 'utf8');
console.log(readMe);

//3..0 LOGIC FLOW
//for loop
for (var i of arr){
  console.log(i);
}
//array loop
var sum = 0;
for (var i = 0; i < arr.length; i++) {
    sum += arr[i];
}
//while loop
var i = 1;                      // initialize
while (i < 100) {               // enters the cycle if statement is true
    i += 1;
}
//if else
if(a_string == String(a)){
  a = Number(a_string);
}

var is_even = 12 % 2 == 0? "even": "odd";

// Switch Case
var day = 6;
switch(day){
	case 5:
		console.log("\nIt is Saturday\n");
		break;
	case 6:
		console.log("\nIt is Sunday\n");
		break;
	default:
		console.log("\nIt is not yet the weekend :/\n");
}

try{
  throw "No actual error here. Move on.";
} catch(err){
  console.log(err);
} finally{
  console.log("This code executes regardless");
}

//4..0 Function
// Default arguments
function addNumbers(a, b=12) {
    return a + b; ;
}
function addNumbers(a) {
    return a + 123;
}

// Higher Order Function
function execute(action){
  action()
}
// Executing higher order function
var lambda = function(){console.log("Higher Order Functions")};
execute(lambda);


for (var i = 0; i < 5; i++) {
  console.log(Math.random())
}

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
class VIP extends User{
  constructor(name, email){
    super(name,email)
  }
}
console.log(new User("John", "Doe@gmail.com").getName());
