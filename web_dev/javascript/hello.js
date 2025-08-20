console.log("Hello");
name = "TonyStark";
age = 24;
price = 146.67;
x = null;
y = undefined;
console.log(name);
console.log(age);
console.log(price);
console.log(x);
console.log(y);
booleanVal = true;
console.log(typeof booleanVal);
bigIntval = BigInt("12354530940")
symbolVal = Symbol("Kya be Lavde")

// object
const student = {
    fullName : "Gandu",
    age : 100,
    cgpa : 7.77,
    isPass : true
};

console.log(student["fullName"]); // avghad aahe
console.log(student.age); // sopa aahe

student.age = student.age - 50;
console.log(student.age);

const product = {
    productName : "Parker Jotter Standard CT Ball Pen",
    rating : 4,
    isDeal : true,
    price : 270,
    offer : 5
};

console.log(product);

const profile = {
    profileName : "Bhartiya Janta Party",
    posts : 195,
    followers : 569000,
    following : 4,
    profileInfo : "Sattadhari Paksha in Maharashtra"
};

console.log(profile);