use('College');
/*
db.createCollection('faculty');

db.faculty.insertMany(
    [
        {
            "name":"Raju",
            "gender":"Male",
            "subject":"UHV",
            "city":"Pune",
            "salary":100000
        },
        {
            "name":"Kaju",
            "gender":"Female",
            "subject":"ADS",
            "city":"Kolhapur",
            "salary":130000
        },
        {
            "name":"Raku",
            "gender":"Male",
            "subject":"DT",
            "city":"Satara",
            "salary":50000
        },
        {
            "name":"Ralo",
            "gender":"Female",
            "subject":"DBMS",
            "city":"Mumbai",
            "salary":150000
        },
        {
            "name":"Maju",
            "gender":"Male",
            "subject":"QSIP",
            "city":"Pune",
            "salary":100000
        }
    ]
);
*/

let q1 = db.faculty.findOne();
console.log(q1);
console.log("\n");

let q2 = db.faculty.find({salary:{$gt:135000}});
console.log(q2);
console.log("\n");

let q3 = db.faculty.update({"name":"Maju"}, {$set:{city : "Pimpri"}});
let q3out = db.faculty.findOne({"name":"Maju"});
console.log(q3out);
console.log("\n");

let q4 = db.faculty.deleteOne({"city":"Satara"});
console.log(db.faculty.find());
console.log("\n");

let q5 = db.faculty.deleteMany({});
console.log(db.faculty.find());
console.log("\n");

let q6 = db.faculty.drop();