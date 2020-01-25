var express = require('express');

var router = express.Router();

const MongoClient = require('mongodb').MongoClient
const url = 'mongodb://localhost:27017'
const dbName = 'andybao'

router.post('/', function (req, res) {
    var v = req.body.value
    var t = req.body.timestamp
    const client = new MongoClient(url)
    client.connect(function(err){
        const db = client.db(dbName);
        const collection = db.collection('temperatures')
        collection.insertOne({value: v, timestamp: t});
        client.close();
        res.send('POST respond');
    });
})

router.delete('/', function (req, res) {
    const client = new MongoClient(url)
    client.connect(function(err){
        const db = client.db(dbName);
        const collection = db.collection('temperatures')
        collection.deleteMany({});
        client.close();
        res.send('DELETE respond');
    });
})

router.get('/', function (req, res) {
    const client = new MongoClient(url)
    client.connect(function(err){
        const db = client.db(dbName);
        const collection = db.collection('temperatures')
        collection.find({}).toArray(function(err, docs) {
            client.close();
            res.send(docs)
          });
    });
})

module.exports = router;