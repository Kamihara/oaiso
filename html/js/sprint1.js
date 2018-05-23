//
// sprint1.js
//

var NAKANO = {};
NAKANO.SPRINT1 = {};

// when you have the geo-location, this part will be called.
NAKANO.SPRINT1.onGeolocation = function(pos) {
    var lat = pos.coords.latitude;
    var lon = pos.coords.longitude;
    $.ajax({
        type: 'GET',
        url: 'http://nakano02.aiit.ac.jp/oaiso/shops',
        data: 'lat='+lat+'&long='+lon,
        success: function(json) {
            //json = $.parseJSON(ret);
            if(typeof json !='object') {
                alert('Sorry! invalid json data');
            } else {
                var output = '<li>'+json[0].shop_name+'</li>';
                output += '<li>'+json[1].shop_name+'</li>';
                output += '<li>'+json[2].shop_name+'</li>';
                $('ul.geotest').html(output);
            }
        },
        error: function() {
            $('ul.geotest').html('<li>Ajax failed</li>');
        }
    });

    // for stab
    // var stab = '[{"shop_name": "\u5927\u4e95\u753a\u307e\u3093\u3077\u304f", "address1": "\u6771\u4eac\u90fd", "address2": "\u54c1\u5ddd\u533a", "address3": "\u5927\u4e95", "address4": "\uff11\u2212\uff11\uff11\u2212\uff11\uff10", "lat": "35.6075849118055", "lng": "139.7320011794560"}, {"shop_name": "\u5927\u4e95\u753a \u9ce5\u4e03", "address1": "\u6771\u4eac\u90fd", "address2": "\u54c1\u5ddd\u533a", "address3": "\u6771\u5927\u4e95", "address4": "\uff15\u2212\uff12\uff15\u2212\uff12\uff10", "lat": "35.6061386466755", "lng": "139.7374671251660"}, {"shop_name": "\u5927\u4e95\u753a\u306e\u3072\u3082\u306e\u5c4b", "address1": "\u6771\u4eac\u90fd", "address2": "\u54c1\u5ddd\u533a", "address3": "\u6771\u5927\u4e95", "address4": "\uff15-\uff14-\uff11\uff12 \u9234\u6728\u30d3\u30eb", "lat": "35.6073953491653", "lng": "139.7360759239420"}]';
    // json = $.parseJSON(stab);
    // var output = '<li>'+json[0].shop_name+'</li>';
    // output += '<li>'+json[1].shop_name+'</li>';
    // output += '<li>'+json[2].shop_name+'</li>';
    // $('ul.geotest').html(output);
};

$(function(){

    // geo location
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(pos) {
                NAKANO.SPRINT1.onGeolocation(pos);
            }, 
            function(err) {
                alert('No Position available');
            },
            {});
    } else {
        alert('No Geolocation funcs available');
    }
});