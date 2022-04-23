# In-class exercise 3

Given *Ex3-paragraph.html*, create the view on the right using *Internal Style sheets*.

Do not worry about the exact font - something similar will do

![Untitled](In-class%20e%2045dd6/Untitled.png)

- Question
    
    ```css
    <!DOCTYPE html>
    <html>
        <head>
            <style type="text/css">
                /* todo: fill the following so that the page looks like the one on the slide */
            </style>
        </head>
        
        <body>
            
    
            <h2> HTML element displayed differently </h2>
            
         
            <h3> First Paragraph </h3>
            
            <div>
                Lorem ipsumLorem ipsum dolor sit amet <p class="none"> IS216 </p>, consectetur adipiscing elit. Aenean suscipit eros at mi auctor tincidunt. 
                Nulla orci arcu, egestas non metus non, tempus sollicitudin velit. Nullam interdum massa sapien, in congue 
                ipsum convallis eget. Sed ut bibendum magna.
            <div>
         
            
            <h3> First Paragraph New Class </h3>        
            
            <div class="newclassdiv">
                Lorem ipsum dolor sit amet <p class="inline"> IS216 </p>, consectetur adipiscing elit. Aenean suscipit eros at mi auctor tincidunt. 
                Nulla orci arcu, egestas non metus non, tempus sollicitudin velit. Nullam interdum massa sapien, in congue 
                ipsum convallis eget. Sed ut bibendum magna.
            </div>
            
            <h3> First Paragraph </h3>
            
            <div>
                Lorem ipsum dolor sit amet <p class="block"> IS216 </p>, consectetur adipiscing elit. Aenean suscipit eros at mi auctor tincidunt. 
                Nulla orci arcu, egestas non metus non, tempus sollicitudin velit. Nullam interdum massa sapien, in congue 
                ipsum convallis eget. Sed ut bibendum magna.
            </div>
                 
         
            <h3> First Paragraph Special </h3>
                
            <div id="specialdiv">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean suscipit eros at mi auctor tincidunt. 
                Nulla orci arcu, egestas non metus non, tempus sollicitudin velit. Nullam interdum massa sapien, in congue 
                ipsum convallis eget. Sed ut bibendum magna.
            </div>
    
            
            <h3> First Paragraph New Class </h3>
            
            <div class="newclassdiv">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean suscipit eros at mi auctor tincidunt. 
                Nulla orci arcu, egestas non metus non, tempus sollicitudin velit. Nullam interdum massa sapien, in congue 
                ipsum convallis eget. Sed ut bibendum magna.
            </div>
            
            
            <h3> First Paragraph </h3>
            
            <div>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean suscipit eros at mi auctor tincidunt. 
                Nulla orci arcu, egestas non metus non, tempus sollicitudin velit. Nullam interdum massa sapien, in congue 
                ipsum convallis eget. Sed ut bibendum magna.
            </div>     
        
            
        </body>
    </html>
    ```
    
- Solution
    
    ```css
    h3 {
    	font-style: italic;
    	color: blueviolet;
    }
    body {
    	font-family: 'Courier New', Courier, monospace;
    }
    .newclassdiv{
    	text-align: center;
    	background-color: yellow;
    	font-family: Georgia, 'Times New Roman', Times, serif;
    	font-size: larger;
    }
    .inline{
    	display:inline;
    	color: red;
    }
    .block{
    	display: block;
    	color:pink;
    	font-style: bold;
    }
    .none{
    	display: none;
    }
    #specialdiv{
    	color: red;
    	font-size: small;
    	font-family: Arial, Helvetica, sans-serif;
    }
    ```