# Exercise 1

How do we have a dropdown list with an default option?

Given wk1exercise1.html, make it so that Sunday is the default option.

Hint: Google - as all programmers do.

### wk1exercise1.html

```html
<!doctype html>
<html>
<head>
<title>Week 1 Exercise 1</title>
</head>
<body>
<!--
ToDo: Find a way to make the 'Sunday' option the default one when
the page is loaded in the browser.
-->
<select>
<option value='Monday'>Monday</option>
<option value='Tuesday'>Tuesday</option>
<option value='Sunday'>Sunday</option>
</select>
</body>
</html>
```

- Solution
    
    ```html
    <!doctype html>
    <html>
    <head>
    <title>Week 1 Exercise 1</title>
    </head>
    <body>
    <!--
    ToDo: Find a way to make the 'Sunday' option the default one when
    the page is loaded in the browser.
    -->
    <select>
    <option value='Monday'>Monday</option>
    <option value='Tuesday'>Tuesday</option>
    <option value='Sunday'selected="true">Sunday</option>
    </select>
    </body>
    </html>
    ```