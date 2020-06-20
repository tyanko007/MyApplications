<?php
// ログイン情報の格納
$cid = "admin";
$cpw = "admin";

if($_SERVER["REQUEST_METHOD"] == "POST"){
    $id = $_POST["name"];
    $pw = $_POST["pass"];

    if($id == $cid && $pw == $pw){
      header("Locaiton: ./accept.html");
      exit;
    }else{
      header("Locaiton: ./deny.html");
      exit;
    }
}

?>
<!DOCTYPE html>
<html lang="ja" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>ログインスクレイピング</title>
  </head>
  <body>
    <h2>ログイン情報を入力してください</h2>
    <form action="#" method="post">
      <label for="name">ID</label><input type="text" name="name" id="name">
      <label for="pass">PW</label><input type="password" name="pass" id="pass">
      <input type="submit" name="login" value="login">
    </form>
  </body>
</html>
