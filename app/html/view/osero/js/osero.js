// 手番フラグ
var turn=0

// オセロの動作
var act = (p) => {
 if(turn === 0 && p.attr("class").substring(0) === "pin"){
  p.attr("class", "b_active");
  $("#oinf").attr("class", "osero-info w")
  turn = 1
 }else if(turn === 1 && p.attr("class").substring(0) === "pin"){
  p.attr("class","w_active");
  $("#oinf").attr("class", "osero-info b")
  turn = 0;
 }else{
  console.log("error");
 }
}


// コマの自動配置テスト用
function auto_create(){
 var ban_ini = [];
  for(var i = 1; i < 9; i++){
   for(var o = 1; o < 9; o++){
     ban_ini.push(`${i}-${o}`);
   }
  }
 for(var i = 0; i < 20; i++){
   var at = Math.floor(Math.random() * (ban_ini.length))
   if(i % 2 !== 0){
    $(`#${ban_ini[at]}`).attr("class", "b_active")
   }else{
    $(`#${ban_ini[at]}`).attr("class", "w_active")
   }
 }
}

// 裏返すコマを特定する処理
// 5.どこまで続くか？
var target_cont = (p, tl, nlp) =>{
  // ポイントの座標を取得
  tmp_box = []
  brank = nlp.split(":")
  rp_y = Number(brank[2])
  rp_x = Number(brank[3])
  var sep = brank[0].split("-")

  if(rp_y === 1){
  var upval_y = -1
 }else if(rp_y === -1){
  var upval_y = 1
 }else{
  var upval_y = 0
 }

 if(rp_x === 1){
  var upval_x = -1
 }else if(rp_x === -1){
  var upval_x = 1
 }else{
  var upval_x = 0
 }

  var point_color = p.attr("class").substring(0,1)
  var brank_color = $(`#${brank[0]}`).attr("class").substring(0,1)
  var flag = false
  // 隣の色が続いているかを確認
  while(flag !== true){
    var y = Number(sep[0])
    var x = Number(sep[1])

    var point = `${y + (upval_y)}-${x + (upval_x)}`

    if(((y + upval_y) > 0 && y +(upval_y) < 9) && ((x + (upval_x)) > 0 && (x + (upval_x) < 9))){
      var nc = $(`#${point}`).attr("class").substring(0,1)
     }else{
      var nc = false
     }

    if(nc === point_color){

      tl.push(brank[0])
      if(tmp_box[tmp_box.length - 1] !== 1){
       for(var i = 0; i < tmp_box.length; i++){
        tl.push(tmp_box[i])
       }
      }
      flag = true
    }else if(nc === brank_color){
      tmp_box.push(point)

      if(rp_y === 1){
       upval_y += -1
      }else if(rp_y === -1){
       upval_y += 1
      }else{
       upval_y = 0
      }

      if(rp_x === 1){
       upval_x += -1
      }else if(rp_x === -1){
       upval_x += 1
      }else{
       upval_x = 0
      }
    }else{
      tmp_box.push(1)
      flag = true
    }
  }
}

// 4.囲っているかの確認
var target_bet = (p, tl, nl, rp) =>{
 var sep = rp.split(":")
 var sep_p = sep[0].split("-")

 var rp_y = Number(sep[2])
 var rp_x = Number(sep[3])

 if(rp_y === 1){
  var upval_y = -1
 }else if(rp_y === -1){
  var upval_y = 1
 }else{
  var upval_y = 0
 }

 if(rp_x === 1){
  var upval_x = -1
 }else if(rp_x === -1){
  var upval_x = 1
 }else{
  var upval_x = 0
 }

 var ck_y = ((Number(sep_p[0])+(upval_y)) > 0 && (Number(sep_p[0])+(upval_y)) < 9)? Number(sep_p[0])+(upval_y) : 99
 var ck_x = ((Number(sep_p[1])+(upval_x)) > 0 && (Number(sep_p[1])+(upval_x)) < 9)? Number(sep_p[1]) + (upval_x) : 99

 var check_point = `${ck_y}-${ck_x}`
 var model_color = p.attr("class").substring(0, 1)
 var check_color = (ck_y !== 99 && ck_x !== 99)? $(`#${check_point}`).attr("class").substring(0, 1) : "p"

 if(check_color === "p"){

 }else if(model_color === check_color){
  tl.push(sep[0])
 }else{
  nl.push(rp)
 }

}

// 3.対象の確認と対象からの距離
var target_ope = (p, cp) =>{
 var res = []
 for(var i = 0; i < cp.length; i++){
  var color = p.attr("class").substring(0,1)
  var sep = cp[i].split(":")
  var pp = p.attr("id").split("-")
  var cpp = sep[0].split("-")
  var dis_y = Number(pp[0]) - Number(cpp[0])
  var dis_x = Number(pp[1]) - Number(cpp[1])

  if(color === sep[1]){
   res.push(`${sep[0]}:${false}`)
  }else{
   res.push(`${sep[0]}:${true}:${dis_y}:${dis_x}`)
  }
 }
 return res
}

// 2.座標に駒は置かれてるか？色は？
var target_conf = (tp, bp) =>{
 var res = []
 for(var i = 0; i < 8; i++){
  if(bp[i] === true){
   tp_class = $(`#${tp[i]}`).attr("class")

   if(tp_class !== "pin"){
    res.push(`${tp[i]}:${tp_class.substring(0,1)}`)
   }
  }
 }
 return res
}

// 1.存在する座標か？
var target_bool = (p, tp) => {

 res = []

 for(var ia = 0; ia < 8; ia++){
  var tmp = tp[ia].split("-")
  var x_tmp = (Number(tmp[1]) > 0 && Number(tmp[1]) < 9)? true : false;
  var y_tmp = (Number(tmp[0]) > 0 && Number(tmp[0]) < 9)? true : false;
  if(x_tmp === true && y_tmp === true){
   res.push(true)
  }else{
   res.push(false)
  }
 }

 return res

}

// 0.確認する座標の取得
var target_get = (p) => {
 var sp = p.attr("id").split("-")
 // 8方向の座標取得
 var fl = String((Number(sp[0]) - 1) + "-" + (Number(sp[1]) - 1)) // 左上
 var fm = String((Number(sp[0]) - 1) + "-" + sp[1]) // 中上
 var fr = String((Number(sp[0]) - 1) + "-" + (Number(sp[1]) + 1)) // 右上
 var sl = String(sp[0] + "-" + (Number(sp[1]) - 1)) // 中左
 var sr = String(sp[0] + "-" + (Number(sp[1]) + 1)) // 中右
 var tl = String((Number(sp[0]) + 1) + "-" + (Number(sp[1]) - 1)) // 下左
 var tm = String((Number(sp[0]) + 1) + "-" + sp[1]) // 下中
 var tr = String((Number(sp[0]) + 1) + "-" + (Number(sp[1]) + 1)) // 下右
 // まとめ
 var ap = [fl, fm, fr, sl, sr, tl, tm, tr]

 return ap
}

// end

// 裏返し処理
var target_action = (p, tl) =>{
 for(var i = 0; i < tl.length; i++){
    $(`#${tl[i]}`).attr("class", p.attr("class"))
  }
}

// action zone
function action(b){
 var end = 0;
 var turn_list = []
 var next_list = []
 act(b)

 var tg = target_get(b)
 var tg_bool = target_bool(b, tg)
 var tg_conf = target_conf(tg, tg_bool)
 var tg_ope = target_ope(b, tg_conf)

 for(var i = 0; i < tg_ope.length; i++){
  flag_c = tg_ope[i].split(":")
  if(flag_c[1] === "true"){
   target_bet(b, turn_list, next_list, tg_ope[i])
  }
 }

 console.log(tg_bool)

 next_list.push(0)
 for(var i = 0; i < next_list.length; i++){
  if(next_list[i] === 0){
   target_action(b, turn_list)
  }else{
    target_cont(b, turn_list, next_list[i])
  }
 }
}


// タップ時動作
$("#1-1").on("click", function(){
  action($("#1-1"))
});

$("#1-2").on("click", function(){
  action($("#1-2"))
});

$("#1-3").on("click", function(){
  action($("#1-3"))
});

$("#1-4").on("click", function(){
  action($("#1-4"))
});

$("#1-5").on("click", function(){
  action($("#1-5"))
});

$("#1-6").on("click", function(){
  action($("#1-6"))
});

$("#1-7").on("click", function(){
  action($("#1-7"))
});

$("#1-8").on("click", function(){
  action($("#1-8"))
});

$("#2-1").on("click", function(){
  action($("#2-1"))
});

$("#2-2").on("click", function(){
  action($("#2-2"))
});

$("#2-3").on("click", function(){
  action($("#2-3"))
});

$("#2-4").on("click", function(){
  action($("#2-4"))
});

$("#2-5").on("click", function(){
  action($("#2-5"))
});

$("#2-6").on("click", function(){
  action($("#2-6"))
});

$("#2-7").on("click", function(){
  action($("#2-7"))
});

$("#2-8").on("click", function(){
  action($("#2-8"))
});

$("#3-1").on("click", function(){
  action($("#3-1"))
});

$("#3-2").on("click", function(){
  action($("#3-2"))
});

$("#3-3").on("click", function(){
  action($("#3-3"))
});

$("#3-4").on("click", function(){
  action($("#3-4"))
});

$("#3-5").on("click", function(){
  action($("#3-5"))
});

$("#3-6").on("click", function(){
  action($("#3-6"))
});

$("#3-7").on("click", function(){
  action($("#3-7"))
});

$("#3-8").on("click", function(){
  action($("#3-8"))
});

$("#4-1").on("click", function(){
  action($("#4-1"))
});

$("#4-2").on("click", function(){
  action($("#4-2"))
});

$("#4-3").on("click", function(){
  action($("#4-3"))
});

$("#4-4").on("click", function(){
  action($("#4-4"))
});

$("#4-5").on("click", function(){
  action($("#4-5"))
});

$("#4-6").on("click", function(){
  action($("#4-6"))
});

$("#4-7").on("click", function(){
  action($("#4-7"))
});

$("#4-8").on("click", function(){
  action($("#4-8"))
});

$("#5-1").on("click", function(){
  action($("#5-1"))
});

$("#5-2").on("click", function(){
  action($("#5-2"))
});

$("#5-3").on("click", function(){
  action($("#5-3"))
});

$("#5-4").on("click", function(){
  action($("#5-4"))
});

$("#5-5").on("click", function(){
  action($("#5-5"))
});

$("#5-6").on("click", function(){
  action($("#5-6"))
});

$("#5-7").on("click", function(){
  action($("#5-7"))
});

$("#5-8").on("click", function(){
  action($("#5-8"))
});

$("#6-1").on("click", function(){
  action($("#6-1"))
});

$("#6-2").on("click", function(){
  action($("#6-2"))
});

$("#6-3").on("click", function(){
  action($("#6-3"))
});

$("#6-4").on("click", function(){
  action($("#6-4"))
});

$("#6-5").on("click", function(){
  action($("#6-5"))
});

$("#6-6").on("click", function(){
  action($("#6-6"))
});

$("#6-7").on("click", function(){
  action($("#6-7"))
});

$("#6-8").on("click", function(){
  action($("#6-8"))
});

$("#7-1").on("click", function(){
  action($("#7-1"))
});

$("#7-2").on("click", function(){
  action($("#7-2"))
});

$("#7-3").on("click", function(){
  action($("#7-3"))
});

$("#7-4").on("click", function(){
  action($("#7-4"))
});

$("#7-5").on("click", function(){
  action($("#7-5"))
});

$("#7-6").on("click", function(){
  action($("#7-6"))
});

$("#7-7").on("click", function(){
  action($("#7-7"))
});

$("#7-8").on("click", function(){
  action($("#7-8"))
});

$("#8-1").on("click", function(){
  action($("#8-1"))
});

$("#8-2").on("click", function(){
  action($("#8-2"))
});

$("#8-3").on("click", function(){
  action($("#8-3"))
});

$("#8-4").on("click", function(){
  action($("#8-4"))
});

$("#8-5").on("click", function(){
  action($("#8-5"))
});

$("#8-6").on("click", function(){
  action($("#8-6"))
});

$("#8-7").on("click", function(){
  action($("#8-7"))
});

$("#8-8").on("click", function(){
  action($("#8-8"))
});
