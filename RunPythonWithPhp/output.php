<html>
    <head>
        <title>
            Graph
        </title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/js/bootstrap.bundle.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <style>
            .output-logo
            {
                height:15%;
                display: flex;
                margin-bottom: 10px;
                background-color:#008b8b;
            }
            #pathstr {
                margin: 0 20px;
                padding: 5px 10px;
                border-radius: 5px;
                box-shadow: 0 3px 6px darkgrey;
                font-family: "Times New Roman", Times, serif;
                font-size: 1.2rem;  
            }
            #search-template
            {
                margin-top:10px;
            }
            #Call-Script
            {
                height:auto;
                min-height:500px;
            }
            @media screen and (max-width:600px) {
                div.output-logo {
                    height:50%;
                }

                .output-logo img{
                    width:100%;
                    height:100%
            }
    }
          
        </style>
    </head>

    <body>

        <div class="output-logo ">
            <img src="../Images/findDSC Logo.png"width="7%" height="100%">
            
        </div>

        <div class ="row pt-1"id="search-template"></div>
    
        <script>
            var xhr=new XMLHttpRequest();
            xhr.onload=() =>
            {
                if(xhr.status === 200) { 
                document.getElementById("search-template").innerHTML = xhr.responseText ; 
                }
            };
            xhr.open('GET', './search.php ', true);
            xhr.send(null);
        </script>

        <div id='Call-Script'><h2 align=center>Directions: <h2></div>

        <?php
            $source = $_POST['source'];
            $destination = $_POST['destination'];

            function validate(&$source,&$destination){
                if($source == $destination){
                    echo '<script>alert("Source and Destination can not be same!!!")</script>';
                }
                else{   
                    echo shell_exec('python ../PythonScripts/Finalv1_db.py ' . $source . ' ' .$destination. ' 2>&1');
                    echo '<br>';       
                };
            }
            validate($source,$destination);
        ?>

        <footer class="text-white text-center text-lg-start" style="background-color: #45637d">
            <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
            ©Copyright findDSC.
            </div>
        </footer>

    </body>   
    <script>
            $(document).ready(function(){
                function Graph(){
                $.get('tag.TXT',function(data){
                    $('#Call-Script').append(data)
                })
            }
            document.getElementById("#Call-Script").innerHTML = Graph(); 
            });
    </script>
</html>