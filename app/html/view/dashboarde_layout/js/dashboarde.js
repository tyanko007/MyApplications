// page init
const mySwiper = new Swiper('.swiper-container', {
  loop: true,
  slidesPreView: 1,
  spaceBetween: 0,
  pagenation: {
    el: ".swiper-pagenation",
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  breakpoints: {
    1300: {
      slidesPerView: 1,
      spaceBetween: 0
    }
  }
});

var sbbc_ini = 0;
if(sbbc_ini !== 0){
  if(sbbc == true){
    $(".sidebar-conf-menu").show();
  }
}else{
  $(".sidebar-conf-menu").hide();
  sbbc_ini = 1;
  sbbc = false;
}
// end

// function line
function sbbc_click(){
  if(sbbc_ini !== 0 && sbbc === false){
    $(".sidebar-conf-menu").show(500);
    sbbc = true;
  }else{
    $(".sidebar-conf-menu").hide(500);
    sbbc = false;
  }
}
// end

// run
function switchByWidth(){
    if (window.matchMedia('(max-width: 900px)').matches) {
        // スマホサイズ
        $(".navigation").show();
        $(".sidebar").hide();
        $(".console").attr("class", "console short");
        $("img").attr("width", "500px")
        $("img").attr("height", "250px")
    } else if (window.matchMedia('(min-width:901px)').matches) {
        // PCサイズ
        $(".navigation").hide();
        $(".sidebar").show();
        $(".console").attr("class", "console long");
        $("img").attr("width", "")
        $("img").attr("height", "500px")
    }
}

//ロードとリサイズの両方で同じ処理を付与する
window.onload = switchByWidth;
window.onresize = switchByWidth;

$("#sidebar-conf-btn-funcS").click(function(){
  sbbc_click();
});
$("#sidebar-conf-btn-funcP").click(function(){
  sbbc_click();
});
