use('test')
db.createCollection('test1')
/*
db.test1.insertMany([
    {
        'name':'Raju',
        'age': 15
    },
    {
        'name' : 'Seetaram',
        'age' : 14
    },
    {
        'name' : 'Ram',
        'age' : 16
    }
])
*/

//db.test1.find()
db.test1.aggregate([
    {
        $group : 
        {
            _id : '$name', avgAge : {$avg : '$age'}
        }
    }
])