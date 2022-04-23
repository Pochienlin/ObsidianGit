## Using CSS
UID: 202202271312
Tags: #🌲
Links: [[Web app development]]


**Three ways**

- *Inline style*: CSS code is placed directly into an HTML element within the `<body>` section of a web page. (not typical)
    - To define an inline CSS style, we simply add the style attribute to an HTML element with the CSS declaration as the attribute value.
    
    <aside>
    💡 Inline style applies to one tag only.
    
    </aside>
    - **Example:** *wk2example2.html*
        
        ```html
        <body> 
        	<h2 style="color:red;"> CAUTION: Icy Road Conditions </h2> 
        	<h2> Please Slow Down! </h2> 
        </body>
        ```
        
- *Internal style sheet*: CSS code is placed into a separate, dedicated area within the `<head>` section of a Web page.
    
    <aside>
    💡 Styles declared in the internal style sheet affect all matching elements on the page.
    
    </aside>
    - Example: wk2example3.html
        
        Style `{color: red;}` applies to all `<h2/>` tags
        
        ```html
        <head>
        	<style type="text/css">
        		h2 {color:red;}
        	</style> 
        </head> 
        
        <body>
        	<h2>CAUTION: Icy Road Conditions</h2>
        	<h2>Please Slow Down!</h2> </body>
        ```
        
- *External style sheet*: CSS code is placed into a `separate file` and then linked to a web page.
    
    The real power of using an external style sheet is that multiple web pages on our site can link to the same style sheet.
    
    The external style sheet contains one or more selector-property-value triples.
    
    - **Example:**
        
        wk2ex4.css
        wk2ex4page1.html
        wk2ex4page2.html
        wk2ex4page3.html
        
        Change wk2ex4.css changes the style of all linked pages
        
    
    <aside>
    💡 Styles declared in an external style sheet will affect all matching elements on all web pages that link to the style sheet.
    
    </aside>
    