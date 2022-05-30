let box = document.getElementsByClassName('brand-image');
let box2 = document.getElementsByClassName('login-logo');
let footer = document.getElementsByClassName('main-footer')

try{
    box[0].setAttribute('src', '/static/images/logo.png');
    box[0].removeAttribute("style");
}
catch(e){}

try{
    let img = box2[0].children[0].children[0];
    img.setAttribute('width', '80%')
}
catch(e){}

try{
    footer[0].children[0].innerHTML = '<b>+996 558 120 012  ITADIS</b>';
}
catch(e){}

try{
   let user_logo = document.getElementsByClassName('image')[0];
   user_logo.children[0]
}
catch(e){}

function include(url, integrity=null, crossorigin=null) {
    let script = document.createElement('script');
    script.src = url;
    if(integrity != null) script.setAttribute('integrity', integrity);
    if(crossorigin != null) script.setAttribute('crossorigin', crossorigin);
    document.getElementsByTagName('head')[0].appendChild(script);   
}



// include(
//     'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js',
//     'sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p',
//     'anonymous'
// );

// include(
//     'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js',
//     'sha512-894YE6QWD5I59HgZOGReFYm4dnWc1Qt5NtvYSaNcOP+u1T9qYdvdihz0PPSiiqn/+/3e7Jo4EaG7TubfWGUrMQ==',
//     'anonymous',
// );

// include(
//     '/static/assets/js/plugins.js'
// );

// include('/static/assets/js/plugins.js');
// include('/static/assets/js/theme.js');