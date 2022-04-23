# Position
UID: 202202271540
Tags: #🌲
Links:  [[Web app development]] [[CSS]] [[Bootstrap CSS]] [[Bootstrap Documentation]]

Use these shorthand utilities for quickly configuring the position of an element.

# [Common values](https://getbootstrap.com/docs/4.1/utilities/position/#common-values)
Quick positioning classes are available, though they are not responsive.
```html
<div class="position-static">...</div>
<div class="position-relative">...</div>
<div class="position-absolute">...</div>
<div class="position-fixed">...</div>
<div class="position-sticky">...</div>
```

## [Fixed top](https://getbootstrap.com/docs/4.1/utilities/position/#fixed-top)
Position an element at the top of the viewport, from edge to edge. Be sure you understand the ramifications of fixed position in your project; you may need to add additional CSS.
```html
<div class="fixed-top">...</div>
```

## [Fixed bottom](https://getbootstrap.com/docs/4.1/utilities/position/#fixed-bottom)
Position an element at the bottom of the viewport, from edge to edge. Be sure you understand the ramifications of fixed position in your project; you may need to add additional CSS.
```html
<div class="fixed-bottom">...</div>
```

## [Sticky top](https://getbootstrap.com/docs/4.1/utilities/position/#sticky-top)
Position an element at the top of the viewport, from edge to edge, but only after you scroll past it. The `.sticky-top` utility uses CSS’s `position: sticky`, which isn’t fully supported in all browsers.

**IE11 and IE10 will render `position: sticky` as `position: relative`.** As such, we wrap the styles in a `@supports` query, limiting the stickiness to only browsers that can render it properly.
```html
<div class="sticky-top">...</div>
```