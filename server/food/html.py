from food.css import css_code
from food.javascript import javascript_code

html_code = f"""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>This Is How Food Should Be</title>
        <link rel="icon" href="https://raw.githubusercontent.com/this-is-how-it-should-be/food/refs/heads/main/assets/icons/hamburger-icon.png">
        <style>{css_code}</style>
        <script>{javascript_code}</script>
    </head>

    <body>
        <header>
            <h1>🍔 This Is How Food Should Be 🍔</h1>
        </header>

        <!-- Food Menu -->
        <div id="food-menu">
            <!-- Food Images Here -->
        </div>

        <!-- Food Details -->
        <div id="food-details-section">
            <img id="detail-image" alt="Loading image..." />
            <h1 id="detail-name">Loading food name...</h1>
        </div>

        <div id="food-description-container">
            <h1 id="food-description-header">Description: <span id="food-description-text"></span></h1>
        </div>

        <!-- Restaurant Details -->
        <div id="restaurant-details-section">
            <h1>Restaurant: <span id="detail-restaurant"></span></h1>
            <h1>Location: <span id="detail-location"></span></h1>
        </div>

        <!-- Button with link to get directions via Google Maps -->
        <a id="directions-link">
            <button id="directions-button">Get Directions</button>
        </a>

        <!-- Button with link to see Yelp reviews -->
        <a id="yelp-link">
            <button id="yelp-button">See Yelp Reviews</button>
        </a>
    </body>
</html>
"""