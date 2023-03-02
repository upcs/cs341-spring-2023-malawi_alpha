
var fs = require('fs');

test ('test selectEvent', () => {


    var html = fs.readFileSync('public/printout.html','utf8');
    expect(html).toEqual(expect.anything());

    document.body.innerHTML = html;
    const $ = require('jquery');

    //Test if other html files loaded correctly
    expect($('h1').html()).toBe("This is a test prinout page");
})