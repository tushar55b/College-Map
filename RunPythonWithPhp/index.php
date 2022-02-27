<html>
    <head>
        <title>
            Home Page
        </title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/js/bootstrap.bundle.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <link rel="stylesheet" href="./index.css">
    </head>
    <body>
        <div class="main-page containerfluid">
            <div class="common-page">
                <img  src="../Images/frontside.jpg" style="position: absolute; height: 80%; width: 100%; opacity: 0.7;">
                <div><img class="img-logo " src="../Images/findDSC Logo.png"></div>
            </div>
             <div class="row" id="search-result"style="top: 500px;">
                 
             </div>

             <!-- Footer -->
        <footer class="page-footer font-small special-color-dark pt-4"  style="background-color: #6351ce;">

               

        <!-- Copyright -->
        <div class="footer-copyright text-center py-3">© 2020 Copyright:FindDSC
  
        </div>
        <!-- Copyright -->
    
        </footer>
            <!-- Footer -->
        </div>
            

    <script>
        var xhr=new XMLHttpRequest();
        xhr.onload=() =>
        {
            if(xhr.status === 200) 
            { 
                document.getElementById("search-result").innerHTML = xhr.responseText ; 
            }
        };
        xhr.open('GET', './search.php ', true);
        xhr.send(null);
    </script>

    </body>
</html>