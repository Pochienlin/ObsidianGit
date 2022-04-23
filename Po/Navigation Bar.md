# Navigation bar
UID: 202202271520
Tags: #🌲 
Links: [[Web app development]] [[CSS]] [[Bootstrap CSS]] [[Bootstrap Documentation]]

## Default navbar
Navbars are responsive meta components that serve as navigation headers for your application or site. They begin collapsed (and are toggleable) in mobile views and become horizontal as the available viewport width increases.

## [How it works](https://getbootstrap.com/docs/4.1/components/navbar/#how-it-works)
Here’s what you need to know before getting started with the navbar:
-   Navbars require a wrapping `.navbar` with `.navbar-expand{-sm|-md|-lg|-xl}` for responsive collapsing and [color scheme](https://getbootstrap.com/docs/4.1/components/navbar/#color-schemes) classes.
-   Navbars and their contents are fluid by default. Use [optional containers](https://getbootstrap.com/docs/4.1/components/navbar/#containers) to limit their horizontal width.
-   Use our [spacing](https://getbootstrap.com/docs/4.1/utilities/spacing/) and [flex](https://getbootstrap.com/docs/4.1/utilities/flex/) utility classes for controlling spacing and alignment within navbars.
-   Navbars are responsive by default, but you can easily modify them to change that. Responsive behavior depends on our Collapse JavaScript plugin.
-   Navbars are hidden by default when printing. Force them to be printed by adding `.d-print` to the `.navbar`. See the [display](https://getbootstrap.com/docs/4.1/utilities/display/) utility class.
-   Ensure accessibility by using a `<nav>` element or, if using a more generic element such as a `<div>`, add a `role="navigation"` to every navbar to explicitly identify it as a landmark region for users of assistive technologies.

## [Supported content](https://getbootstrap.com/docs/4.1/components/navbar/#supported-content)
![Pasted image 20220227151847.png](app://local/%2FUsers%2Fpochienlin%2FDesktop%2FObsidian%2FPasted%20image%2020220227151847.png?1645946327788)
Navbars come with built-in support for a handful of sub-components. Choose from the following as needed:
-   `.navbar-brand` for your company, product, or project name.
-   `.navbar-nav` for a full-height and lightweight navigation (including support for dropdowns).
-   `.navbar-toggler` for use with our collapse plugin and other [navigation toggling](https://getbootstrap.com/docs/4.1/components/navbar/#responsive-behaviors) behaviors.
-   `.form-inline` for any form controls and actions.
-   `.navbar-text` for adding vertically centered strings of text.
-   `.collapse.navbar-collapse` for grouping and hiding navbar contents by a parent breakpoint.

Here’s an example of all the sub-components included in a responsive light-themed navbar that automatically collapses at the `lg` (large) breakpoint.
```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#">Disabled</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
```

### 

### [Nav](https://getbootstrap.com/docs/4.1/components/navbar/#nav)
![[Pasted image 20220227151847.png]]
Navbar navigation links build on our `.nav` options with their own modifier class and require the use of [toggler classes](https://getbootstrap.com/docs/4.1/components/navbar/#toggler) for proper responsive styling. **Navigation in navbars will also grow to occupy as much horizontal space as possible** to keep your navbar contents securely aligned.

Active states—with `.active`—to indicate the current page can be applied directly to `.nav-link`s or their immediate parent `.nav-item`s.
```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Features</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Pricing</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#">Disabled</a>
      </li>
    </ul>
  </div>
</nav>
```

And because we use classes for our navs, you can avoid the list-based approach entirely if you like.
![[Pasted image 20220227151820.png]]

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div class="navbar-nav">
      <a class="nav-item nav-link active" href="#">Home <span class="sr-only">(current)</span></a>
      <a class="nav-item nav-link" href="#">Features</a>
      <a class="nav-item nav-link" href="#">Pricing</a>
      <a class="nav-item nav-link disabled" href="#">Disabled</a>
    </div>
  </div>
</nav>
```

You may also utilize dropdowns in your navbar nav. Dropdown menus require a wrapping element for positioning, so be sure to use separate and nested elements for `.nav-item` and `.nav-link` as shown below.