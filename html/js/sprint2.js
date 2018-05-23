//
// sprint2.js
//

var NAKANO = {};
NAKANO.SPRINT2 = {};
NAKANO.SPRINT2.p = 0;
NAKANO.SPRINT2.maxp = 9;
// NAKANO.SPRINT2.maxp = 99;
NAKANO.SPRINT2.initial = undefined;
NAKANO.SPRINT2.uservec = [];
NAKANO.SPRINT2.geo = [];
NAKANO.SPRINT2.shops = [];

// instance of this class will be used in recommendation pages
// var Shop = function (name, dist, img0, img1, genre, price, summary) {
var Shop = function (sid, name, genre, price, tel, lat, lng, dist, geo, review, photo_shop, photo_food, bhours, links) {
    this.sid = sid;
    this.name = name;
    this.genre = genre;
    this.price = price;
    this.tel = tel;
    this.lat = lat;
    this.lng = lng;
    this.dist = dist;
    this.geo = geo;
    this.review = review;
    this.photo_shop = photo_shop;
    this.photo_food = photo_food;
    if (bhours) {
        this.bhours = bhours;
    } else {
        this.bhours = '';
    }
    if (links) {
        this.links = '<a href="'+links+'" target="_blank">'+links+'</a>';
    } else {
        this.links = '';
    }
};

// 
NAKANO.SPRINT2.prev = function() {
    if (NAKANO.SPRINT2.p > 0) {
        $('body').removeClass('last');
        $('.main.p'+NAKANO.SPRINT2.p).removeClass('active');
        NAKANO.SPRINT2.p -= 1;
        if (NAKANO.SPRINT2.p == 0) {
            $('body').addClass('first');
        }
        $('.main.p'+NAKANO.SPRINT2.p+' .fadable').css('opacity', 0);
        $('.main.p'+NAKANO.SPRINT2.p+' .fadable').animate({'opacity': 1});
        $('.main.p'+NAKANO.SPRINT2.p).addClass('active');
    }
};

// when no-control fired
NAKANO.SPRINT2.no = function() {
    var sid = parseInt($('.main.active').attr('data-sid'), 10);
    NAKANO.SPRINT2.trackEvent('ShopSelection', 'no', sid);

    // $('.main.p'+NAKANO.SPRINT2.p).css('display', 'none');
    $('.main.p'+NAKANO.SPRINT2.p).removeClass('active');
    // $('.main.p'+NAKANO.SPRINT2.p).remove();
    if (NAKANO.SPRINT2.p == NAKANO.SPRINT2.maxp) {



        // last page
        NAKANO.SPRINT2.p = 0;

        // welcome page again
        $('body').removeClass('last');
        // $(NAKANO.SPRINT2.welcome).insertAfter('header');
        $('.container .dynamic').html(NAKANO.SPRINT2.welcome);
        setTimeout(function () {
            NAKANO.SPRINT2.activateControls();
        }, 100);
    } else {
        $('body').removeClass('first');
        if (NAKANO.SPRINT2.p == -1 + NAKANO.SPRINT2.maxp) {
            $('body').addClass('last');
        }
        NAKANO.SPRINT2.p += 1;
        $('.main.p'+NAKANO.SPRINT2.p+' .fadable').css('opacity', 0);
        $('.main.p'+NAKANO.SPRINT2.p+' .fadable').animate({'opacity': 1});
        // $('.main.p'+NAKANO.SPRINT2.p).css('display', 'block');
        $('.main.p'+NAKANO.SPRINT2.p).addClass('active');
    }
};

// start dragging control. class 'cragging' is just for z-index
// store initial pos for stop event(animation)
NAKANO.SPRINT2.start = function(e, ui) {
    NAKANO.SPRINT2.WIDTH = $('.container').width();
    NAKANO.SPRINT2.START = parseInt($(this).css('left'), 10);
    $(this).addClass('dragging');
    NAKANO.SPRINT2.initial = parseInt($(this).css('left'), 10);
};

// left button dragging finished
NAKANO.SPRINT2.stop = function(e, ui) {
    $(e.target).animate({top: "0px", left: NAKANO.SPRINT2.initial},
        {complete: function() {
        }
    });

    // clear z-index for future use
    $(e.target).removeClass('dragging');

    // dnd
    NAKANO.SPRINT2.END = parseInt($(this).css('left'), 10);
    var delta = Math.abs(NAKANO.SPRINT2.START - NAKANO.SPRINT2.END) / NAKANO.SPRINT2.WIDTH;
    if (delta > 0.75) {
        // fire dnd
        NAKANO.SPRINT2.no();
        $('.main.p'+NAKANO.SPRINT2.p).css('visibility', 'none');
    }
};

// for yes-control
NAKANO.SPRINT2.yesbtn = function(e, ui) {
    var sid = parseInt($('.main.active').attr('data-sid'), 10);
    NAKANO.SPRINT2.trackEvent('ShopSelection', 'yes', sid);
    $(e.target).removeClass('dragging');
    $(e.target).animate({top: "0px", left: NAKANO.SPRINT2.initial});

    // 
    NAKANO.SPRINT2.END = parseInt($(this).css('left'), 10);
    var delta = Math.abs(NAKANO.SPRINT2.START - NAKANO.SPRINT2.END) / NAKANO.SPRINT2.WIDTH;
    if (delta > 0.75) {
        tel = $('.main.active .control .right').attr('data-pn');
        // fire dnd
        // todo xxx. tel can be string 'no data'
        location.href = 'tel:'+tel;
    }
};

// when loading completed, controls are activated
NAKANO.SPRINT2.activateControls = function() {
    $('.control .left').draggable({
        axis:'x',
        start: NAKANO.SPRINT2.start,
        stop: NAKANO.SPRINT2.stop
    });
    $('.control .right').draggable({
        axis:'x',
        start: NAKANO.SPRINT2.start,
        stop: NAKANO.SPRINT2.yesbtn
    });
    $('.control .left').droppable({
        drop: function(e, ui) {
        }
    });

    // user selection
    $('.welcome .set0 li a').click(function () {
        NAKANO.SPRINT2.uservec = [];
        var imageIndex = parseInt($(this).attr('data-index'), 10);
        NAKANO.SPRINT2.trackEvent('Preference', '1st', imageIndex);
        NAKANO.SPRINT2.uservec.push(imageIndex);
        $('.welcome .set0').removeClass('active');
        $('.welcome .set1').addClass('active');
    });
    // $('.welcome .set1 li a').click(function () {
    //     var imageIndex = parseInt($(this).attr('data-index'), 10);
    //     NAKANO.SPRINT2.trackEvent('Preference', '2nd', imageIndex);
    //     NAKANO.SPRINT2.uservec.push(imageIndex);
    //     $('.welcome .set1').removeClass('active');
    //     $('.welcome .set2').addClass('active');
    // });
    $('.welcome .set1 li a').click(function () {
        var imageIndex = parseInt($(this).attr('data-index'), 10);
        NAKANO.SPRINT2.trackEvent('Preference', '3rd', imageIndex);
        NAKANO.SPRINT2.uservec.push(imageIndex);
        $('.welcome .set1').removeClass('active');
        $('.welcome .set2').addClass('active');
    });
    $('.welcome .set2 li a').click(function () {
        var imageIndex = parseInt($(this).attr('data-index'), 10);
        NAKANO.SPRINT2.trackEvent('Preference', '4th', imageIndex);
        NAKANO.SPRINT2.uservec.push(imageIndex);
        $('.welcome .set2').removeClass('active');
        $('.welcome .set3').addClass('active');
    });
    $('.welcome .set3 li a').click(function () {
        var imageIndex = parseInt($(this).attr('data-index'), 10);
        NAKANO.SPRINT2.trackEvent('Preference', '5th', imageIndex);
        NAKANO.SPRINT2.uservec.push(imageIndex);
        $('.welcome .set3').removeClass('active');

        // price range
        //   低×低=低, 中×中=中, 高×高=高, 低×中=中, 中×低=中, 高×中=高, 中×高=高, 低×高=中, 高×低=中
        //   each price range is defined in html as: 低: 0, 中: 1, 高:2
        // var vec_price = [],
        //     vec_price_low = [1,0,0],
        //     vec_price_middle = [0,1,0],
        //     vec_price_high = [0,0,1],
        //     buf = NAKANO.SPRINT2.uservec[0] * NAKANO.SPRINT2.uservec[1];
        // if (NAKANO.SPRINT2.uservec[0] == 0 && NAKANO.SPRINT2.uservec[1] == 0) {
        //     vec_price = vec_price_low;
        // } else if (buf <= 1) {
        //     vec_price = vec_price_middle;
        // } else {
        //     vec_price = vec_price_high;
        // }
        var vec_price = [0,0,0];
        vec_price[NAKANO.SPRINT2.uservec[0]] = 1;
        
        // purpose of going there is: eats = [1,0,0,0], drinks = [0,1,0,0],
        //   atmosphere = [0,0,1,0], quickneasy = [0,0,0,1]
        //   second option may set some value to 0.5
        var vec_purpose = [0,0,0,0];
        vec_purpose[NAKANO.SPRINT2.uservec[1]] = 1;
        if (NAKANO.SPRINT2.uservec[1] != NAKANO.SPRINT2.uservec[2]) {
            vec_purpose[NAKANO.SPRINT2.uservec[2]] = 0.5;
        }

        // are you going to go there alone? yes: [1,0], no: [0,1]
        var vec_group = [0,0];
        vec_group[NAKANO.SPRINT2.uservec[3]] = 1;

        NAKANO.SPRINT2.uservec = vec_price.concat(vec_purpose).concat(vec_group);
        NAKANO.SPRINT2.onEvent();
    });

    // next, prev
    $('.sname img.icon.prev').click(function() {
        NAKANO.SPRINT2.prev();
    });
    $('.sname img.icon.next').click(function() {
        NAKANO.SPRINT2.no();
    });
};

//
NAKANO.SPRINT2.parseJson = function (obj) {
    var ret = {
        "sid": "",
        "sname": "",
        "genre": "",
        "price": "",
        "tel": null,
        "lat": -1,
        "lng": -1,
        "dist": -1,
        "geo": "",
        "review": "",
        "photo_food": "",
        "photo_shop": "",
        "bhours": "",
        "links": ""
    };

    ret.sid = obj.id;
    ret.sname = obj.shop_name;
    ret.genre = obj.genre;
    ret.tel = obj.tel;
    ret.bhours = obj.bussiness_hours;
    ret.links = obj.links;
    ret.lat = parseFloat(obj.lat);
    ret.lng = parseFloat(obj.lng);
    try {
        var lunch_min = numberWithCommas(obj.budget_lunch_min);
        var lunch_max = numberWithCommas(obj.budget_lunch_max);
        ret.price = '<span class="lunch">￥'+lunch_min+'~'+lunch_max+'</span>';
    } catch (e) {
        console.log('error during parsing json... continue...');
    }
    try {
        var dinner_min = numberWithCommas(obj.budget_dinner_min);
        var dinner_max = numberWithCommas(obj.budget_dinner_max);
        ret.price += '<span class="dinner">￥'+dinner_min+'~'+dinner_max+'</span>';
    } catch (e) {
        console.log('error during parsing json... continue...');
    }
    try {
        ulat = NAKANO.SPRINT2.geo[0];
        ulng = NAKANO.SPRINT2.geo[1];
    } catch (e) {
        console.log('error during parsing json... continue...');
    }
    try {
        ret.dist = Math.floor(1000*distance(ret.lat, ret.lng, ulat, ulng, 'K'));
        ret.geo = 'https://maps.google.com/maps?q='+ret.lat.toString()+','+ret.lng.toString()+'+'+obj.shop_name;
    } catch(e) {
        console.log('error during parsing json... continue...');
    }
    try {
        ret.review = obj.review;
        if (ret.review == 'null' || !ret.review) {
            ret.review = '';
        }
    } catch(e) {
        console.log('error during parsing json... continue...');
    }
    try {
        ret.photo_shop = obj.photo_shop;
        ret.photo_food = obj.photo_food;
    } catch(e) {
        console.log('error during parsing json... continue...');
    }
    return ret;
}

// 
NAKANO.SPRINT2.EmbedValues = function (tmp, args, index) {
    try {
        tmp = tmp.replace('%%index%%', index);
        tmp = tmp.replace('%%sid%%', args.sid);
        tmp = tmp.replace('%%name%%', args.name);
        tmp = tmp.replace('%%genre%%', args.genre);
        tmp = tmp.replace('%%img0%%', args.photo_shop);
        tmp = tmp.replace('%%img1%%', args.photo_food);
        tmp = tmp.replace('%%price%%', args.price);
        tmp = tmp.replace('%%tel%%', args.tel);
        tmp = tmp.replace('%%dist%%', args.dist);
        tmp = tmp.replace('%%geo%%', args.geo);
        tmp = tmp.replace('%%summary%%', args.review);
        tmp = tmp.replace('%%bhours%%', args.bhours);
        tmp = tmp.replace('%%links%%', args.links);
        return tmp;
    } catch (e) {
        return null;
    }
};

// from the server!
NAKANO.SPRINT2.AjaxResponse = function (json) {

    if (!json) {
        console.log('json is null');
    }

    if (json.length < NAKANO.SPRINT2.maxp + 1) {
        NAKANO.SPRINT2.maxp = json.length - 1;
        console.log('data length is not perfect but go');
        NAKANO.SPRINT2.ajaxok = true;
    }

    // if (NAKANO.SPRINT2.ajaxok) {

    //     // 
    //     if(typeof json !='object' || json.length < NAKANO.SPRINT2.maxp + 1) {
    //         NAKANO.SPRINT2.ajaxok = false;
    //         console.log('Sorry! invalid json data');
    //         if (json.length < NAKANO.SPRINT2.maxp + 1) {
    //             console.log('length < max');
    //         }
    //     }
    // }
    if (NAKANO.SPRINT2.ajaxok) {
        NAKANO.SPRINT2.shops = [];

        var ret = undefined;
        for (var i = 0; i <= NAKANO.SPRINT2.maxp; i++) {
            ret = NAKANO.SPRINT2.parseJson(json[i]);
            NAKANO.SPRINT2.shops.push(new Shop(ret.sid, ret.sname, ret.genre, ret.price, ret.tel, ret.lat, ret.lng, ret.dist, ret.geo, ret.review, ret.photo_food, ret.photo_shop, ret.bhours, ret.links));
        }






        // var ret = NAKANO.SPRINT2.parseJson(json[0]);
        // NAKANO.SPRINT2.shops.push(new Shop(ret.sid, ret.sname, ret.genre, ret.price, ret.tel, ret.lat, ret.lng, ret.dist, ret.geo, ret.review, ret.photo_food, ret.photo_shop, ret.bhours, ret.links));
        // ret = NAKANO.SPRINT2.parseJson(json[1]);
        // NAKANO.SPRINT2.shops.push(new Shop(ret.sid, ret.sname, ret.genre, ret.price, ret.tel, ret.lat, ret.lng, ret.dist, ret.geo, ret.review, ret.photo_food, ret.photo_shop, ret.bhours, ret.links));
        // ret = NAKANO.SPRINT2.parseJson(json[2]);
        // NAKANO.SPRINT2.shops.push(new Shop(ret.sid, ret.sname, ret.genre, ret.price, ret.tel, ret.lat, ret.lng, ret.dist, ret.geo, ret.review, ret.photo_food, ret.photo_shop, ret.bhours, ret.links));
        // ret = NAKANO.SPRINT2.parseJson(json[3]);
        // NAKANO.SPRINT2.shops.push(new Shop(ret.sid, ret.sname, ret.genre, ret.price, ret.tel, ret.lat, ret.lng, ret.dist, ret.geo, ret.review, ret.photo_food, ret.photo_shop, ret.bhours, ret.links));
        // ret = NAKANO.SPRINT2.parseJson(json[4]);
        // NAKANO.SPRINT2.shops.push(new Shop(ret.sid, ret.sname, ret.genre, ret.price, ret.tel, ret.lat, ret.lng, ret.dist, ret.geo, ret.review, ret.photo_food, ret.photo_shop, ret.bhours, ret.links));
    } else {
        console.log('Sorry! Ajax failed. error workaround is not implemented. sorry. maybe todo');
    }

    var html = [];

    for (var i = 0; i <= NAKANO.SPRINT2.maxp; i++) {
        // NAKANO.SPRINT2.maxp[i]
        html.push(NAKANO.SPRINT2.EmbedValues(NAKANO.SPRINT2.stab2, NAKANO.SPRINT2.shops[i], i));
    };

    // html.push(NAKANO.SPRINT2.EmbedValues(NAKANO.SPRINT2.stab2, NAKANO.SPRINT2.shops[0], 0));
    // html.push(NAKANO.SPRINT2.EmbedValues(NAKANO.SPRINT2.stab2, NAKANO.SPRINT2.shops[1], 1));
    // html.push(NAKANO.SPRINT2.EmbedValues(NAKANO.SPRINT2.stab2, NAKANO.SPRINT2.shops[2], 2));
    // html.push(NAKANO.SPRINT2.EmbedValues(NAKANO.SPRINT2.stab2, NAKANO.SPRINT2.shops[3], 3));
    // html.push(NAKANO.SPRINT2.EmbedValues(NAKANO.SPRINT2.stab2, NAKANO.SPRINT2.shops[4], 4));

    // var p0 = NAKANO.SPRINT2.stab2;
    // p0 = p0.replace('%%index%%', 0);
    // p0 = p0.replace('%%sid%%', NAKANO.SPRINT2.shops[0].sid);
    // p0 = p0.replace('%%name%%', NAKANO.SPRINT2.shops[0].name);
    // p0 = p0.replace('%%genre%%', NAKANO.SPRINT2.shops[0].genre);
    // p0 = p0.replace('%%img0%%', NAKANO.SPRINT2.shops[0].photo_shop);
    // p0 = p0.replace('%%img1%%', NAKANO.SPRINT2.shops[0].photo_food);
    // p0 = p0.replace('%%price%%', NAKANO.SPRINT2.shops[0].price);
    // p0 = p0.replace('%%tel%%', NAKANO.SPRINT2.shops[0].tel);
    // p0 = p0.replace('%%dist%%', NAKANO.SPRINT2.shops[0].dist);
    // p0 = p0.replace('%%geo%%', NAKANO.SPRINT2.shops[0].geo);
    // p0 = p0.replace('%%summary%%', NAKANO.SPRINT2.shops[0].review);
    // p0 = p0.replace('%%bhours%%', NAKANO.SPRINT2.shops[0].bhours);
    // p0 = p0.replace('%%links%%', NAKANO.SPRINT2.shops[0].links);

    // var p1 = NAKANO.SPRINT2.stab2;
    // p1 = p1.replace('%%index%%', 1);
    // p1 = p1.replace('%%sid%%', NAKANO.SPRINT2.shops[1].sid);
    // p1 = p1.replace('%%name%%', NAKANO.SPRINT2.shops[1].name);
    // p1 = p1.replace('%%genre%%', NAKANO.SPRINT2.shops[1].genre);
    // p1 = p1.replace('%%img0%%', NAKANO.SPRINT2.shops[1].photo_shop);
    // p1 = p1.replace('%%img1%%', NAKANO.SPRINT2.shops[1].photo_food);
    // p1 = p1.replace('%%price%%', NAKANO.SPRINT2.shops[1].price);
    // p1 = p1.replace('%%tel%%', NAKANO.SPRINT2.shops[1].tel);
    // p1 = p1.replace('%%dist%%', NAKANO.SPRINT2.shops[1].dist);
    // p1 = p1.replace('%%geo%%', NAKANO.SPRINT2.shops[1].geo);
    // p1 = p1.replace('%%summary%%', NAKANO.SPRINT2.shops[1].review);
    // p1 = p1.replace('%%bhours%%', NAKANO.SPRINT2.shops[1].bhours);
    // p1 = p1.replace('%%links%%', NAKANO.SPRINT2.shops[1].links);

    // var p2 = NAKANO.SPRINT2.stab2;
    // p2 = p2.replace('%%index%%', 2);
    // p2 = p2.replace('%%sid%%', NAKANO.SPRINT2.shops[2].sid);
    // p2 = p2.replace('%%name%%', NAKANO.SPRINT2.shops[2].name);
    // p2 = p2.replace('%%genre%%', NAKANO.SPRINT2.shops[2].genre);
    // p2 = p2.replace('%%img0%%', NAKANO.SPRINT2.shops[2].photo_shop);
    // p2 = p2.replace('%%img1%%', NAKANO.SPRINT2.shops[2].photo_food);
    // p2 = p2.replace('%%price%%', NAKANO.SPRINT2.shops[2].price);
    // p2 = p2.replace('%%tel%%', NAKANO.SPRINT2.shops[2].tel);
    // p2 = p2.replace('%%dist%%', NAKANO.SPRINT2.shops[2].dist);
    // p2 = p2.replace('%%geo%%', NAKANO.SPRINT2.shops[2].geo);
    // p2 = p2.replace('%%summary%%', NAKANO.SPRINT2.shops[2].review);
    // p2 = p2.replace('%%bhours%%', NAKANO.SPRINT2.shops[2].bhours);
    // p2 = p2.replace('%%links%%', NAKANO.SPRINT2.shops[2].links);

    $(html.join('')).insertAfter('.container .welcome');

    $('.main').on('click', function() {
        var sid = parseInt($('.main.active').attr('data-sid'), 10);
        NAKANO.SPRINT2.trackEvent('Shop', 'tabelog', sid);
    });

    // console.log($(window).width());
    // console.log($('.main.active h2.sname').width());
    // var scale = $('.main.p0 h2.sname').width() / $(window).width();
    // if (scale < 1) {
    //     $('.main.p0 h2.sname').css('transform', 'scale('+scale+')');
    // }
    // scale = $('.main.p1 h2.sname').width() / $(window).width();
    // if (scale < 1) {
    //     $('.main.p1 h2.sname').css('transform', 'scale('+scale+')');
    // }
    // scale = $('.main.p2 h2.sname').width() / $(window).width();
    // if (scale < 1) {
    //     $('.main.p2 h2.sname').css('transform', 'scale('+scale+')');
    // }

    // first page
    $('body').addClass('first');
    $('body').removeClass('last');
    $('.main.p0').addClass('active');
    $('.welcome').remove();
    NAKANO.SPRINT2.activateControls();
};

NAKANO.SPRINT2.onEvent = function(pos) {
    if (NAKANO.SPRINT2.uservec.length * NAKANO.SPRINT2.geo.length) {

        // start loading
        lat = NAKANO.SPRINT2.geo[0].toString();
        lng = NAKANO.SPRINT2.geo[1].toString();
        $('.trying').remove();
        NAKANO.SPRINT2.ajaxok = false;

        //
        console.log('lat: '+lat);
        console.log('lng: '+lng);
        $.ajax({
            type: 'GET',
            url: '/oaiso/shop_info',
            data: {"lat":lat, "lng":lng, "uvec":NAKANO.SPRINT2.uservec.join(',')},
            success: function(json) {
                NAKANO.SPRINT2.ajaxok = true;
                NAKANO.SPRINT2.AjaxResponse(json);
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                console.log(errorThrown);
                NAKANO.SPRINT2.ajaxok = false;
                NAKANO.SPRINT2.AjaxResponse(null);
            }
        });
    } else if (NAKANO.SPRINT2.uservec.length == 0) {
        console.log('ユーザー選択を待っています。');
    } else if (NAKANO.SPRINT2.geo.length == 0) {
        console.log('位置情報を待っています。');
    }
};

// triggered by the browser
NAKANO.SPRINT2.onGeolocation = function(pos) {
    if (pos.coords.latitude < 0 || pos.coords.longitude < 0) {
        console.log('Invalid geo-location. use dummy geo location will be used.');
        pos.coords.latitude = 35.606222;
        pos.coords.longitude = 139.734861;
        NAKANO.SPRINT2.geo.push(pos.coords.latitude);
        NAKANO.SPRINT2.geo.push(pos.coords.longitude);
    } else {
        NAKANO.SPRINT2.geo.push(pos.coords.latitude);
        NAKANO.SPRINT2.geo.push(pos.coords.longitude);
        console.log('Geo location is available.');
    }
    NAKANO.SPRINT2.onEvent();
};

NAKANO.SPRINT2.trackEvent = function(eventCategory, eventAction, eventLabel) {
    // I don't know why but tracking ID is gone sometimes (always gone at first time).
    ga('create', 'UA-109492916-1');
    ga('send', 'event', eventCategory, eventAction, eventLabel);
};

NAKANO.SPRINT2.updateGeo = function() {
    navigator.geolocation.getCurrentPosition(
        function(pos) {
            if (pos.coords.latitude < 0 || pos.coords.longitude < 0) {
                console.log('Invalid geo-location. new geo will be ignored.');
            } else {
                NAKANO.SPRINT2.geo = [];
                NAKANO.SPRINT2.geo.push(pos.coords.latitude);
                NAKANO.SPRINT2.geo.push(pos.coords.longitude);
                console.log('Geo location is updated.');
            }
        }, function(err) {}, {}
    );
};

// main
$(function() {
    NAKANO.SPRINT2.welcome = $('.welcome').prop('outerHTML');

    setTimeout(function () {
        $('.startup').fadeOut();
    }, 2000);

    $('.container').on('scroll', function() {
      $('.container').scrollLeft(0);
    });

    // debug get location
    var manualgeo = {};
    var raw_param = location.search.substring(1).split('&');
    for (var i = 0; i < raw_param.length; i++) {
        var buf = raw_param[i].split('=');
        manualgeo[buf[0]] = buf[1];
    }
    if (manualgeo['lat'] > 0 && manualgeo['lng'] > 0) {
        console.log('manually set geo location will be used');
        NAKANO.SPRINT2.geo.push(manualgeo['lat']);
        NAKANO.SPRINT2.geo.push(manualgeo['lng']);
        NAKANO.SPRINT2.onEvent();
    } else {
        // geo location
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                function(pos) {
                    NAKANO.SPRINT2.onGeolocation(pos);

                    // start updating
                    // every 1 minute
                    setInterval(function () {
                        NAKANO.SPRINT2.updateGeo();
                    }, 60000);
                }, 
                function(err) {
                    console.log('No Position available. Maybe blocked by browser\'s security.');
                    console.log('maybe need to set locations manually. ');

                    // for review
                    var pos = {};
                    pos.coords = {};
                    pos.coords.latitude = -1;
                    pos.coords.longitude = -1;
                    NAKANO.SPRINT2.onGeolocation(pos);
                },
                {});
        } else {
            console.log('No Geolocation funcs available');
        }
    }

    NAKANO.SPRINT2.stab2 = $('.stab2').get(0).firstChild.nodeValue;
    $('.stab2').remove();

    // actions
    NAKANO.SPRINT2.activateControls();
});
