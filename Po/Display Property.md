# Display Property

UID: 202202271528
Tags: #🌲
Links:  [[Web app development]] [[CSS]] [[Bootstrap CSS]] [[Bootstrap Documentation]]

## [How it works](https://getbootstrap.com/docs/4.1/utilities/display/#how-it-works)
Change the value of the [`display` property](https://developer.mozilla.org/en-US/docs/Web/CSS/display) with our responsive display utility classes. We purposely support only a subset of all possible values for `display`. Classes can be combined for various effects as you need.

## [Notation](https://getbootstrap.com/docs/4.1/utilities/display/#notation)
Display utility classes that apply to all [breakpoints](https://getbootstrap.com/docs/4.1/layout/overview/#responsive-breakpoints), from `xs` to `xl`, have no breakpoint abbreviation in them. This is because those classes are applied from `min-width: 0;` and up, and thus are not bound by a media query. The remaining breakpoints, however, do include a breakpoint abbreviation.

As such, the classes are named using the format:
-   `.d-{value}` for `xs`
-   `.d-{breakpoint}-{value}` for `sm`, `md`, `lg`, and `xl`.

Where _value_ is one of:
-   `none`
-   `inline`
-   `inline-block`
-   `block`
-   `table`
-   `table-cell`
-   `table-row`
-   `flex`
-   `inline-flex`

The media queries effect screen widths with the given breakpoint _or larger_. For example, `.d-lg-none` sets `display: none;` on both `lg` and `xl` screens.

## Examples
```html
<div class="d-inline p-2 bg-primary text-white">d-inline</div>
<div class="d-inline p-2 bg-dark text-white">d-inline</div>
```
![[Pasted image 20220227153320.png]]
```html
<span class="d-block p-2 bg-primary text-white">d-block</span>
<span class="d-block p-2 bg-dark text-white">d-block</span>
```

## [Hiding elements](https://getbootstrap.com/docs/4.1/utilities/display/#hiding-elements)
For faster mobile-friendly development, use responsive display classes for showing and hiding elements by device. Avoid creating entirely different versions of the same site, instead hide element responsively for each screen size.

To hide elements simply use the `.d-none` class or one of the `.d-{sm,md,lg,xl}-none` classes for any responsive screen variation.

To show an element only on a given interval of screen sizes you can combine one `.d-*-none` class with a `.d-*-*` class, for example `.d-none .d-md-block .d-xl-none` will hide the element for all screen sizes except on medium and large devices.

| Screen Size | Class |
|----------------|:--------|
| Hidden on all | `.d-none`|
| Hidden only on xs | `.d-none .d-sm-block` |
| Hidden only on sm | `.d-sm-none .d-md-block`|
| Hidden only on md | `.d-md-none .d-lg-block`|
| Hidden only on lg | `.d-lg-none .d-xl-block`|
| Hidden only on xl | `.d-xl-none` |
| Visible on all | `.d-block`|
| Visible only on xs |`.d-block .d-sm-none`|
| Visible only on sm | `.d-none .d-sm-block .d-md-none`|
| Visible only on md |`.d-none .d-md-block .d-lg-none`|
| Visible only on lg |`.d-none .d-lg-block .d-xl-none`|
| Visible only on xl |`.d-none .d-xl-block`|

### hide on screens smaller than lg
```html
<div class="d-lg-none">hide on screens wider than lg</div>
<div class="d-none d-lg-block">hide on screens smaller than lg</div>
```
