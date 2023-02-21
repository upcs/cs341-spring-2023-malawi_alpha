<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Login</title>
        <meta content='width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no' name='viewport'>
        <link href="loginStyle.css" rel="stylesheet" type="text/css" />

    </head>
    <body class="skin-black">
    
<?php
echo hash('ripemd160', '123');
?>

        <div class="container" style="margin-top:30px">
          <div class="col-md-4 col-md-offset-4">
              <div class="panel panel-default">
            <div class="panel-heading"><h3 class="panel-title"><strong></strong></h3></div>
            <div class="panel-body">
              <form name="form1" role="form" action = "authentication.php" onsubmit = "return validation()" method="post">
                <div class="form-group">
                  <label for="token">Token</label>
                  <input type="password" class="form-control" style="border-radius:0px" id="token" name="token" placeholder="Enter Token">
                </div>
                <div class="form-group">
                  <a href="forgotToken.php">Forgot Token? </a>
                </div>
                <button type="submit" class="btn btn-sm btn-primary" name="btn_login">Log in</button>
              </form>
            </div>
          </div>
          </div>
        </div>
<script>  
            function validation()  
            {  
                var token=document.form1.token.value;  
                if(token.length=="") {  
                    alert("Token Field is Empty");  
                    return false;  
                }         
            }  
        </script>  
    </body>
</html>
