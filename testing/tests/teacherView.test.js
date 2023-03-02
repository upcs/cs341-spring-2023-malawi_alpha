
var fs = require('fs');

test ('test selectEvent', () => {


    var html = fs.readFileSync('public/index.html','utf8');
    expect(html).toEqual(expect.anything());

    document.body.innerHTML = html;
    const $ = require('jquery');

    //run tesets to see if index.html loaded correctly
    expect($('title').html()).toBe("Teacher View");
    expect($('#search-student-button').html()).toBe("Search Student");
    expect($('td.rotate-text#running-average').html()).toBe("Running Average");
})