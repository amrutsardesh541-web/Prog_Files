use('snapmart');

//db.sales.find({});

let q1 = db.sales.aggregate(
    [
        {
            $group : {_id : '$category',
            totalRevenue : {$sum : {$multiply : ['$price', '$quantity']}}
            }
        }
    ]
);

console.log(q1);
console.log("\n");

let q2 = db.sales.aggregate(
    [
        {
            $group : {_id : '$product',
                mostSelling : {$sum : '$quantity'}
            }
        },
        {
            $sort: {
                quantity: -1
            }
        },
        {
            $limit: 3
        }
    ]
);
console.log(q2);
console.log("\n");

let q3 = db.sales.aggregate(
    [
        {
            $group : {_id : '$store',
                storeRevenue : {$sum : {$multiply : ['$price','$quantity']}}
            }
        }
    ]
);
console.log(q3);
console.log('\n');

let q4 = db.sales.aggregate(
    [
        {
            $group: {_id: '$category',
                avgPrice : {$avg : '$price'}
            }
        }
    ]
);
console.log(q4);