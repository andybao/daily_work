var express = require('express');
var router = express.Router();
var request = require('request');

/* GET home page. */
router.get('/', function(req, res, next) {
    request('http://localhost:3000/apis', function (error, response, body){
        var data_array = JSON.parse(body);
        var data_length = data_array.length;
        // console.log('body:', data_array[0].value);

        res.render('index', { length: data_length, data_array: data_array });
    });
});

router.post('/', function (req, res) {
    res.send('Got a POST request')
})

module.exports = router;
