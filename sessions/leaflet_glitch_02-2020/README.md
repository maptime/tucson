# **February**

## Playing with Web Maps

SIGN IN: https://hackmd.io/@maptimeTUS/ryyvaDhm8

**For starters:**

Leaflet is "an open-source JavaScript library
for mobile-friendly interactive maps" and a common (and great) way to display your data.
https://leafletjs.com/index.html

Glitch is a tool for creating web apps, such as maps, as well as a community of web app enthusiasts from around the world. 
https://glitch.com/

Example of a Leaflet.js starter app with map added already for you.
https://starter-leaflet.glitch.me/

Basic tutorial on how to make a web map with Leaflet (and GeoJSONs)
https://glitch.com/culture/make-a-web-map-with-leaflet/
Youtube video associated with the above link. 
https://www.youtube.com/watch?v=uea6fpYUn1I&t=598s

Quick Start Guide from Leaflet
https://leafletjs.com/examples/quick-start/


**"Remix to Edit"**

Clicking on the "Remix" button of any Leaflet map on Glitch will allow you to edit the map and make it your own.  It makes a new project on your Glitch account and gives you a randomly generated name like "Buttery-waltz" or "Torch-redcurrant."  Like everything in the app, the project name can be changed and the code/files altered once you've "remixed" the app.  

**"Show"**

This button allows you to few your map in real-time and displays changes as you make them in the script.  If nothing shows up on the map, altering your code is most likely required. 


*The pane on the left-hand side of the app will display assets, env, README.md, index.html, script.js and style.css.*

### Breakdown

**Assets:**

•	Any file from your computer can be placed here. 
•	Any data for the project, images or geojsons or shapefiles. 
•	Uploading is an option with the button on the top.
 
•	For my example, I added the https://opendata.arcgis.com/datasets/7e33977fe38941d38a3c3e8bca5de158_1.geojson into the Assets folder in order to reference the data in the script.


**Index.html:**

•	HTML code block that outlines your map. 
•	Directs CSS styles to the map and javascript code into the map and references the script.js
•	Includes map title, descriptions, etc. 
•	Able to be shown a live preview at “Show” button on the top
•	Sets up the order of your page (i.e. Title, description/link, map, Glitch button with a link to the glitch itself)

**Script.js**

•	Where you can do things with the data
•	Using JavaScript, making the map is your first step by defining it and adding a tileLayer a.k.a. basemap tiles
•	Next, you specific event handlers are functions that respond to events on the page which are defined first so they can each be attached to the data layer and triggered on specific events. 
•	Insert the data using the fetch( “INSERT YOUR GEOJSON HERE”)
•	From here, more functions can be done with the data, for example adding and customizing a pop up on your map or adding a legend.

**Style.css**

•	CSS files add styling rules to your content
•	Fonts, colors, height/width, popup colors, and positioning of popups are all defined here. 

