# Exercise 3

Open wk1exercise3.html in Chrome.

Enter two numbers and check what is printed in the console.

There are two problems. (1) You are allowed to enter non-numbers; (2) The result is not exactly the sum.

Fix the the first problem by changing the HTML part only; we will soon be able to fix the second problem with Javascript.

```html
<!doctype html>
<html>
  <head>
    <title>Demo: Get Started Debugging JavaScript with Chrome DevTools</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
    <h1>Demo: Get Started Debugging JavaScript with Chrome DevTools</h1>
    <label for="num1">Number 1</label>
    <input placeholder="Number 1" id="num1">
    <label for="num2">Number 2</label>
    <input placeholder="Number 2" id="num2">
    <button onclick="console.log(document.getElementById('num1').value+document.getElementById('num2').value)">Add Number 1 and Number 2</button>
  </body>
</html>
```

- Solution
    
    ```html
    <!doctype html>
    <html>
      <head>
        <title>Demo: Get Started Debugging JavaScript with Chrome DevTools</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
      </head>
      <body>
        <h1>Demo: Get Started Debugging JavaScript with Chrome DevTools</h1>
        <label for="num1">Number 1</label>
        <input placeholder="Number 1" type='number' id="num1">
        <label for="num2">Number 2</label>
        <input placeholder="Number 2" type='number' id="num2">
        <button onclick="console.log(document.getElementById('num1').value+document.getElementById('num2').value)">Add Number 1 and Number 2</button>
      </body>
    </html>
    ```