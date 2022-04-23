# In-class exercise 2

Given ex2.html, read the text and identify the problems. Fix the bugs so that the text is consistent with its style.

- Question
    
    ```css
    <!doctype html>
    <html>
    
    <head>
        <link rel="stylesheet" type="text/css" href="wk2ex6.css">
        <style type="text/css">
            p {
                color: blue;
                text-align: center;
            }
    
            h1,
            h2 {
                color: red;
                text-align: left;
            }
    
            .normal {
                color: green;
            }
    
            .center {
                text-align: center;
            }
    
            #emphasis {
                font-style: italic;
            }
        </style>
    </head>
    
    <body>
        <p>This should be blue and in the center.</p>
        <h2>This should be red and on the left.</h2>
        <h1 id="normal">This should be green.</h1>
        <h1 id="center">This should be in the center.</h1>
        <h1 id="normal center">This should be green and in the center.</h1>
    </body>
    
    </html>
    ```
    

[Ex2.html](In-class%20e%2094fbc/Ex2.html)

- Solution
    - id types cannot apply to more than one, whereas classes can
    - for internal style sheet, use `<style text="text/css"> ... </style>`, not `type="text/css"`
    
    ```css
    <!doctype html>
    <html>
    	<head>
    	    <link rel="stylesheet" type="text/css" href="wk2ex6.css">
    	    <style text="text/css">
    	        p {
    	            color: blue;
    	            text-align: center;
    	        }
    	
    	        h1,
    	        h2 {
    	            color: red;
    	            text-align: left;
    	        }
    	
    	        .normal {
    	            color: green;
    	        }
    	
    	        .center {
    	            text-align: center;
    	        }
    	
    	        #emphasis {
    	            font-style: italic;
    	        }
    	    </style>
    	</head>
    	<body>
    	    <p>This should be blue and in the center.</p>
    	    <h2>This should be red and on the left.</h2>
    	    <h1 class="normal">This should be green.</h1>
    	    <h1 class="center">This should be in the center.</h1>
    	    <h1 class="normal center">This should be green and in the center.</h1>
    	</body>
    </html>
    ```
    

[Ex2.html](In-class%20e%2094fbc/Ex2%201.html)