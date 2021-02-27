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
function mode_change(){
  
}

function addcolumn(i){

  i += 1;

  var tmp_line = `<div class="addline ${i}">
                    <input type="text" name="nm ${i}" class="form-control" placeholder="column name" id="nm ${i}">
                    <select class="form-control ml-2 tl-sel" id="tp ${i}">
                      <option value="integer">integer</option>
                      <option value="varchar-128">text</option>
                      <option value="varchar-1024">longtext</option>
                      <option value="date">date</option>
                      <option value="timestamp">timestamp</option>
                    </select>`

  $(tmp_line).appendTo(".tl-addline")
  return i;
}

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
        $(".main-view").attr("class", "main-view short");
    } else if (window.matchMedia('(min-width:901px)').matches) {
        // PCサイズ
        $(".navigation").hide();
        $(".sidebar").show();
        $(".main-view").attr("class", "main-view long");
    }
}

//ロードとリサイズの両方で同じ処理を付与する
window.onload = switchByWidth;
window.onresize = switchByWidth;

var TABLE_FLAG = 0;

$("#sidebar-conf-btn-funcS").click(function(){
  sbbc_click();
});
$("#sidebar-conf-btn-funcP").click(function(){
  sbbc_click();
});
$("#linebtn").click(function(){
  TABLE_FLAG = addcolumn(TABLE_FLAG);
})
$("#change").click(function(){
  mode_change();
})
