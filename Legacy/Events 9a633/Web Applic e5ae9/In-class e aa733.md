# In-class example

Given Ex5.html, provide an external CSS style sheet named Ex5.css so that the page looks like the one below. Note that the table stretches to the full width of the page. Do not worry about the exact color.

[Ex5.html](In-class%20e%20aa733/Ex5.html)

- solution
    
    ```css
    h2{
        color: blue;
    }
    h3{
        font-style: italic;
    }
    table{
        width:100%;
    }
    td,th{
        border: 1px solid black;
        
    }
    td{
        width: 10%;
        text-align: left;
    
    }
    .redbox{
        background-color:pink;
    }
    .greenbox{
        background-color:#95e6bc;
    }
    
    .cellbold{
        font-weight: bold;
    }
    ```