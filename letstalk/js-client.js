var net = require('net');

var client = new net.Socket();

var dataObj = {1:{name:'andybao', mail:'me@andybao.net'}, end:'Avengers'}
var dataJSON = JSON.stringify(dataObj);

client.connect(10000, 'localhost', function() {
	console.log('Connected');
	client.write(dataJSON);
});

/*
client.on('data', function(data) {
	console.log('Received: ' + data);
	client.destroy(); // kill client after server's response
});

client.on('close', function() {
	console.log('Connection closed');
});*/