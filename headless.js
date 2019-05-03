const net = require('net');
const puppeteer = require('puppeteer');

Object.size = function(obj) {
  var size = 0, key;
  for (key in obj) {
      if (obj.hasOwnProperty(key)) size++;
  }
  return size;
};

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('http://iot.d.chainvu.com/admin/aim/aimlogentry/');
  await page.type('#id_username', '');
  await page.type('#id_password', '');
  await page.click('[type="submit"]');
  console.log('something here');

  await page.waitForSelector('#result_list > tbody > tr').catch(e => {console.log(e);});

  console.log('db is displayed');
  var aimsDataObj = await page.$$eval('#result_list > tbody > tr', aims => {
    var data = {};
    var aimCount = 0;
    for (var aim of aims) {
      var aimProperties = aim.getElementsByTagName('td');
      var tempValueObj = {};
      
      for (var aimProperty of aimProperties) {
        if (aimProperty.classList.contains('field-event_type')) {
          tempValueObj['event_type'] = aimProperty.innerHTML;
        } 
        else if (aimProperty.classList.contains('field-aim')) {
          tempValueObj['aim'] = aimProperty.innerHTML;
        }
      }
      
      var aimUrl = aim.getElementsByTagName('a')[0].href;
      tempValueObj['timestampUrl'] = aimUrl;
      data[aimCount] = tempValueObj;
      aimCount = aimCount + 1;
    }
    return data;
  });
  
  for (var i = 0; i < Object.size(aimsDataObj); i ++) {
    var tempAimDataObj = aimsDataObj['' + i];
    var tempUrl = tempAimDataObj.timestampUrl;
    await page.goto(tempUrl);
    var date = await page.$eval('#id_timestamp_0', e => {
      return e.getAttribute('value');
    });
    var time = await page.$eval('#id_timestamp_1', e => {
      return e.getAttribute('value');
    });
    var timestamp = date + ' ' + time;
    tempAimDataObj['timestamp'] = timestamp;
    //console.log(timestamp);
  }

  aimsDataObj['end'] = 'Avengers';
  
  const aimsDataJSON = JSON.stringify(aimsDataObj);
  const client = new net.Socket();
  client.connect(10000, 'localhost', function() {
    console.log('Connected');
    client.write(aimsDataJSON);
  });
  console.log(aimsDataObj);
  
  await browser.close();
})();