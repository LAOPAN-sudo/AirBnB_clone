# 0x01. AirBnB clone - Web static
## 0. Inline styling
[Task 0](./0-index.html) Write an HTML page that displays a header and a footer.
----
**Layout**
1. Body:
- no margin
- no padding
2. Header:
- color #FF0000 (red)
- height: 70px
- width: 100%
3. Footer:
- color #00FF00 (green)
- height: 60px
- width: 100%
- text Best School center vertically and horizontally
- always at the bottom at the page
## 1. Head styling
[Task 1](./1-index.html)Write an HTML page that displays a header and a footer by using the style tag in the head tag (same as [Task 0](./0-index.html))
## 2. CSS files
[Task 2](./2-index.html) Write an HTML page that displays a header and a footer by using CSS files (same as [Task 1](./1-index.html))
-----
**You must have 3 CSS files:**
- styles/2-common.css: for global style (i.e. the body style)
- styles/2-header.css: for header style
- styles/2-footer.css: for footer style
## 3. Zoning done!
[Task 3](./3-index.html) Write an HTML page that displays a header and footer by using CSS files (same as [Task 2](./2-index.html))
-----
**Layout:**

1. Common:
- no margin
- no padding
- font color: #484848
- font size: 14px
- font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;
- icon in the browser tab
2. Header:
- color: white
- height: 70px
- width: 100%
- border bottom 1px #CCCCCC
- logo align on left and center vertically (20px space at the left)
3. Footer:
- color white
- height: 60px
- width: 100%
- border top 1px #CCCCCC
- text Best School center vertically and horizontally
- always at the bottom at the page
## 4. Search!
[Task 4](./4-index.html) Write an HTML page that displays a header, footer and a filters box with a search button.
-----
**Layout: (based on [Task 3](./3-index.html))**
1. Container:
- between header and footer tags, add a div:
- classname: container
- max width 1000px
- margin top and bottom 30px - it should be 30px under the bottom of the header - (screenshot)
- center horizontally
2. Filter section:
- tag section
- classname filters
- inside the .container
- color white
- height: 70px
- width: 100% of the container
- border 1px #DDDDDD with radius 4px
3. Button search:
- tag button
- text Search
- font size: 18px
- inside the section filters
- background color #FF5A5F
- text color #FFFFFF
- height: 48px
- width: 20% of the section filters
- no borders
- border radius: 4px
- center vertically and at 30px of the right border
- change opacity to 90% when the mouse is on the button
## 5. More filters
[Task 5](./5-index.html) Write an HTML page that displays a header, footer and a filters box.
----
**Layout: (based on [Task 4](./4-index.html))**

1. Locations and Amenities filters:
- tag: div
- classname: locations for location tag and amenities for the other
- inside the section filters (same level as the button Search)
- height: 100% of the section filters
- width: 25% of the section filters
- border right #DDDDDD 1px only for the first left filter
2. contains a title:
- tag: h3
- font weight: 600
- text States or Amenities
- contains a subtitle:
- tag: h4
- font weight: 400
- font size: 14px
- text with fake contents
## 6. It's (h)over
[Task 6]() Write an HTML page that displays a header, footer and a filters box with dropdown.
-----
**Layout: (based on [Task 5](./5-index.html))**

Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter div:
1. tag ul
- classname popover
- text should be fake now
- inside each div
- not displayed by default
- color #FAFAFA
- width same as the div filter
- border #DDDDDD 1px with border radius 4px
- no list display
2. Location filter has 2 levels of ul/li:
- state -> cities
- state name must be display in a h2 tag (font size 16px)
## 7. Display results
[Task 7]() Write an HTML page that displays a header, footer, a filters box with dropdown and results.
----
