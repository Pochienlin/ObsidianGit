# Web Application Development II | CSS

Archive?: No
End: January 18, 2022 3:15 PM
Start: January 18, 2022 12:00 PM
Tags: [IS216]

# Overview

1. What is CSS? 
2. Three ways to use CSS
3. CSS properties

## Main Concepts

1. 

# What is CSS?

CSS = Cascading Style Sheets

- One of the three core technology of Web (frontend) development
    
    [https://www.w3schools.com/css/](https://www.w3schools.com/css/)
    

**HTML:** Content, *nouns*

**CSS**: Presentation, *adjectives* 

**Javascript**: Dynamic effects, *verbs*

By using CSS, we separate the content of a web page from the presentation (format & styling) of that content.

CSS enables us to make all pages of our website look similar and consistent.

CSS allows us to make site-wide formatting changes by making edits to a single file.

<aside>
💡 Main point summary

</aside>

- **Example**
    
    Given wk2example1.html, changing `mystyle1.css` to `mystyle2.css` changes the look.
    

## Using CSS

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
    

# CSS Syntax

**The syntax of CSS**

- Example
    
    ```css
    p {
    		color: red;
    		font-style: italic;
    		text-align: center; 
    }
    ```
    

```css
selector { property: value; }
```

*We can define as many properties as we wish for a selector.

A semicolon must be placed after each CSS declaration. Omitting this semicolon is the
single most common mistake made by those learning CSS.

# CSS Comments

**Single-line comment**

```css
/* this is a comment */
```

**Multi-line comment**

```css
/*
This is
a
comment
*/
```

## Using CSS

![Untitled](Web%20Applic%20e5ae9/Untitled.png)

[In-class exercise 1](Web%20Applic%20e5ae9/In-class%20e%20604ef.md)

# CSS Syntax: selector

**There are many selectors in CSS.** 

A reference list is [here](https://www.w3schools.com/cssref/css_selectors.asp):

## Element selector

```css
p {
	color: blue;
	text-align: center;
}
h1, h2 {
	color: blue; 
	text-align: left;
}
```

## ID Selector

```css
#emphasis { font-style: italic;
}
<p id="emphasis">
	This is a unique paragraph that deserves an emphasis.
</p>
```

## Class Selector

```css
.normal {
	color: black;
}
.center {
	text-align: center;
}
```

Note that an element can belong to multiple classes.

- Example
    
    Example: wk2example5.html
    
    ```css
    <p class="normal">This is a paragraph that
    shares the style properties with the following
    paragraph.</p>
    ```
    
    ```css
    <p class="normal">This is a paragraph that
    shares the style properties with the
    paragraph above.</p>
    ```
    
    ```css
    <p class="normal center">This is also a
    normal paragraph but is centered.</p>
    ```
    
- **Some Exotic Examples of other selectors**
    
    ![Untitled](Web%20Applic%20e5ae9/Untitled%201.png)
    

# Cascading

A browser processes all CSS code, including those introduced by all three ways, and applies the following cascading order.

- Example
    
    **Example:** *wk2example6.html*
    
    ```css
    <head>
    <style type="text/css"> h2 {color:red;}</style>
    
    </head>
    
    <body>
    <h2 style="color: green;">CAUTION</h2>
    
    </body>
    What color is “CAUTION”?
    ```
    
    - Answer
        
        Green, since inline takes precedence over internal
        

[In-class exercise 2](Web%20Applic%20e5ae9/In-class%20e%2094fbc.md)

1. Inline style has first priority
2. Internal style sheet has second priority
3. External style sheet has third priority
4. Web browser default has lowest priority

# CSS: Properties

**There are many properties and corresponding values.**

A reference list is [here](https://www.w3schools.com/cssref/):

**Examples:** *wk2example8.html*

### Text display properties

`Color:` specify the color of the text

`Text-align:` specify horizontal alignment

`Text-decoration:` e.g.,

```css
*p { text-decoration: line-through; }*
```

### **Display properties**

Specifies how an element is displayed with
respect to other elements. Every HTML
element has a default display value.

- Example: wk2example9.html
    
    ```css
    .normal {
    	display: inline;
    }
    ```
    

Value “inline” means to display like <span>.

- block: displayed on a new line
- inline: displayed inline with the previous element, i.e., place this element next to the previous one.
- none: hidden (used with JavaScript to hide/show elements depending on logic)

# CSS: Values

- Examples: wk2example11.html
    
    Color values
    
    - hex color value (Google): #eab01c
    - rgb values : (30, 200, 0)
    - rgba: red, green, blue, alpha (where alpha is 0 means “fully transparent” and 1 means “fully opaque”)

**Each property is associated with multiple values.**

Check out the list of values associated with
each property [here](https://www.w3schools.com/cssref/default.asp)

# Units of Measurement

**Absolute length:**

- in (inches)
- cm (centimeters)
- px (pixels, 1px = 1/96*1inch)

**Relative length:**

- % (percentage)
- em (relative to the font-size)
- vw (relative to 1% of the width of the viewport - browser window size)

Some CSS values such as values for font-size, width, height, margin, and padding have different units of measurement

[In-class exercise 3](Web%20Applic%20e5ae9/In-class%20e%2045dd6.md)

# Box model

![Untitled](Web%20Applic%20e5ae9/Untitled%202.png)

In CSS, every HTML element is a box.

A box consists of: the content, the padding, the border and the margin.

Every part of a box can be decorated through CSS.

**Content**: text or images

**Padding**: an area around the content and inside the border; padding is transparent

**Border**: a border that goes around the padding and content

**Margin**: an area outside the border; margin is transparent

# Decorating Content and Border

**Property width and height and border** (whose value is composed of width, style, and color)

- Example: wk2example12.html
    
    ```css
    centerdiv1 {
    width: 400px;
    margin: auto;
    border: 3px solid black;
    }
    centerdiv2 { max-width: 400px; margin: auto;
    border: 3px solid blue;
    }
    ```
    
    ![Untitled](Web%20Applic%20e5ae9/Untitled%203.png)
    

Use border-left, border-right, border-top, border-bottom properties to specifically style the left, right, top, or bottom of a border separately

- **Example:** *wk2example13.html*
    
    ```css
    <p style=“border-left: 5px dotted red”>
    This has a special border
    </p>
    ```
    
    ![Untitled](Web%20Applic%20e5ae9/Untitled%204.png)
    

Use border-radius property to create rounded borders

- You can specify different radius for the four corners.
- The radius can be absolute length or percentage (of the height or width).
- Example *wk2example13.html*
    
    ```css
    .circle {
    width: 150px; height: 150px;
    border-radius: 90%;
    border: 2px solid red;
    }
    ```
    

Use margin-top, margin-right, margin-bottom, margin-left properties to create space around (top, right, bottom, and left) an element’s content, outside of its border.

- **Example:** *wk2example14.html*
    
    ```css
    .box {
    text-align: center;
    width: 150px;
    height: 150px;
    border-radius: 10%;
    border: 2px solid red;
    margin-top: 30px;
    margin-bottom: 30px;
    margin-right: 50px;
    margin-left: 50px;
    }
    ```
    

Additionally, property values can be specified with the following.

- auto - horizontally center the element
within its container
- length - specifies a margin in px, pt, cm, etc.
- % - specifies a margin in % of the width of the containing element
- inherit - specifies that the margin should be inherited from the parent element
- **Example:** *wk2example14.html*
    
    ```css
    .box {
    text-align: center;
    width: 150px;
    height: 150px;
    border-radius: 10%;
    border: 2px solid red;
    /* top right bottom left */
    **margin: 30px 50px 30px 50px;**
    }
    ```
    

# Decorating padding

Use padding-top, padding-right, padding-bottom, padding-left properties to generate space around an element's content, inside the border.

- **Example:** *wk2example15.html*
    
    ```css
    .box {
    text-align: center;
    width: 150px;
    height: 150px;
    border-radius: 10%;
    border: 2px solid red;
    **padding-top: 22px;**
    }
    ```
    

[Exercise 4](Web%20Applic%20e5ae9/Exercise%204%20dd015.md)

When using shorthand:

```
padding: 20px 50px 20px 30px
/* sequence is top right bottom left

padding: 20px 50px 20px
/* padding; top-bottom right-left */
```

# Table styling

[In-class example](Web%20Applic%20e5ae9/In-class%20e%20aa733.md)

**Property border**: specify border size, style (solid, dashed, dotted) and color, e.g., 

```jsx
table, th, td { border: 1px dashed blue; }
```

**Property border-bottom**: horizon dividers for <th> and <td>, e.g., 

```jsx
th, td { border-bottom: 1px solid black; }
```

**Property border-collapse**: collapse into a single border, e.g.,

See: Example

```jsx
table { border-collapse: collapse; }
```

**Property tr:hover** : highlight table rows on mouse over, e.g.,

```jsx
tr:hover { background-color: red; }
```

# Position Properties

![Untitled](Web%20Applic%20e5ae9/Untitled%205.png)

# Overlapping elements

When elements are positioned, they can overlap other elements.

The [z-index](https://www.w3schools.com/cssref/tryit.asp?filename=trycss_anim_z-index) property specifies the stack order of an element (which element should be placed in front of, or behind, the others).

An element can have a positive or negative stack order

**Example**

```css
img {
position: absolute;
left: 0px;
top: 0px;
z-index: -1;}
```

# Link properties `<a/>`

Links can be styled with any CSS property (e.g. color, font-family, background, etc.).

links can also be styled differently depending on what state they are in.

- a:link - a normal, unvisited link
- a:visited - a link the user has visited
- a:hover - a link when the user mouses over it
- a:active - a link at the moment it is clicked

**Example:** *wk2example18.html*

```css
/* unvisited link */
a:link { color: red; }
/* visited link */
a:visited { color: green; }
/* mouse over link */
a:hover { color: hotpink; }
/* selected link */
a:active { color: blue; }
```

# List Properties

List style properties can be used to style
ordered lists (<ul>) and unordered lists (<ol>):

- Set different markers
- Set an image as marker
- Add background colors

See: Example

```css
<ul class="a"> 
	<li>Coffee</li> 
	<li>Tea</li>
</ul>

<ol class="c">
	<li>Coffee</li> 
	<li>Tea</li> 
</ol>

ul.a { 
	list-style-image: url(`img.png`); 
} 
ol.c { 
	list-style-type: upper-roman; 
}
```

# Styling forms

```css
input { width: 100%}
input[type=text] { ... }
input[type=password] { ... }
input[type=text] {
background-color: white;
background-image: url('search.jpg');
background-position: 5px;
background-repeat: no-repeat;
padding: 12px 20px 12px 40px;
}
```

We can use various CSS properties we have learnt to improve the look of HTML forms

**Example:** *wk2example20.html*

E**xample**: *wk2exmaple21.html*

add width, border, background-color styles to your select menu

```css
select {
width: 100%;
padding: 16px 20px;
border: none;
border-radius: 4px;
background-color: #f1f1f1;
}
```

**Example:** styling buttons

[In-class exercise 6](Web%20Applic%20e5ae9/In-class%20e%206c606.md)

```css
input[type=button], input[type=submit],
input[type=reset] {
background-color: #4CAF50;
border: none;
color: white;
padding: 16px 32px;
text-decoration: none;
margin: 4px 2px;
cursor: pointer;
}
```