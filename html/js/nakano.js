//
// nakano.js
//

var NAKANO = {};
NAKANO.TOP = {};

NAKANO.conditions = {};
NAKANO.conditions.isIE = navigator.userAgent.indexOf('MSIE') != -1;
NAKANO.conditions.isMobile = false;
NAKANO.conditions.isTablet = false;
NAKANO.conditions.isIOS = false;
var ua = window.navigator.userAgent.toLowerCase();
if (ua.indexOf('iphone') != -1 || ua.indexOf('ipod') != -1) {
    NAKANO.conditions.isIOS = true;
    NAKANO.conditions.isMobile = true;
}
if (ua.indexOf('android') != -1 && ua.indexOf('mobile') != -1) {
    NAKANO.conditions.isMobile = true;
}
if (ua.indexOf('ipad') != -1) {
    NAKANO.conditions.isTablet = true;
}

if (ua.indexOf('android') != -1 && ua.indexOf('mobile') == -1) {
    NAKANO.conditions.isTablet = true;
}

// 
NAKANO.has = function (selector) {
    return $(selector).length != 0;
};

$(function(){

    // geo location test
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(pos) {
                var lat = pos.coords.latitude;
                var lon = pos.coords.longitude;
                var out = '緯度: '+lat;
                out += '<br>';
                out += '経度: '+lon;
                $('.geotest').html(out);

                // ここからAjax呼ぶ
                // todo
            }, 
            function(err) {}, {});
    } else {
        alert('No Geolocation available');
    }
});