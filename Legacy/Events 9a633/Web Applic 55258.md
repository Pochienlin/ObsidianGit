# Web Application Development II | Bootstrap

Archive?: No
End: January 25, 2022 3:15 PM
Start: January 25, 2022 12:00 PM

# Overview

Bootstrap

- What is Bootstrap?
- How to use Bootstrap
- Bootstrap examples

## Main Concepts

1. 

# What is Bootstrap?

> “The most popular HTML, CSS, and JS framework for developing responsive, mobile first projects on the web.”
> 

Full details are at: [www.getbootstrap.com](http://www.getbootstrap.com/)

Bootstrap is a giant collection of handy, reusable bits of code written in HTML, CSS, and JavaScript. It’s a front-end development framework that enables developers to quickly build fully responsive websites.

In programmers’ language: `Bootstrap = bootstrap.min.css + bootstrap.min.js`

## Bootstrap highlights

Examples: [https://getbootstrap.com/docs/5.1/examples/](https://getbootstrap.com/docs/5.1/examples/)

- Download the source code of the examples and customize accordingly if you wish.

- Bootstrap’s responsive grid
- Bootstrap’s Responsive Images
- Bootstrap’s Components
- Bootstrap’s JavaScript
...

# Using Bootstrap

Using BootstrapCDN (CDN: Content Delivery Network)

- A system of distributed servers (network) that deliver webpages and other Web content to a user based on the geographic locations of the user, the origin of the webpage and a content delivery server.

<aside>
💡 This will load the libraries through the CDN - not from your local server.

</aside>

```html
<head>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css"
		rel="stylesheet“
		integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We"
		crossorigin="anonymous">
</head>
<body>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js"
		integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj"
		crossorigin="anonymous">
	</script>
</body>
```

The `integrity` attribute allows a browser to check the fetched script to ensure that the code is never loaded if the source has been manipulated.

The `crossorigin` attribute sets the mode of the request to an HTTP CORS Request. CORS stands for Cross-Origin Resource Sharing, and is a mechanism that allows resources on a web page to be requested from another domain outside their own domain.

- “anonymous” means no credentials (from your local server) will be sent over to the destination server

Get started [https://getbootstrap.com/docs/5.1/gettingstarted/introduction/](https://getbootstrap.com/docs/5.1/gettingstarted/introduction/)

The starter template | Refer to example: wk3example1.html

# Margin collapsing

# Flex boxes `Display-flex`

# Positioning