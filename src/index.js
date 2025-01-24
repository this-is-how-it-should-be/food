const foodMenuDivElement = document.getElementById("food-menu")
const foodDetailsSectionDivElement = document.getElementById("food-details-section")
const restaurantDetailsSectionDivElement = document.getElementById('restaurant-details-section')
const detailImageElement = document.getElementById("detail-image")
const detailNameElement = document.getElementById('detail-name')
const detailRestaurantElement = document.getElementById('detail-restaurant')
const detailLocationElement = document.getElementById('detail-location')
const directionsLinkElement = document.getElementById('directions-link')
const yelpLinkElement = document.getElementById('yelp-link')
const foodDescriptionTextElement = document.getElementById('food-description-text')

fetch("https://raw.githubusercontent.com/this-is-how-it-should-be/food/refs/heads/main/db.json")
.then(response => response.json())
.then(data => {
    const foods = data.foods
    foods.forEach(addFoodImageToRestaurantMenu)
    displayFoodDetails(foods[0])
    foodDetailsSectionDivElement.style.display = "block"
    restaurantDetailsSectionDivElement.style.display = "block"
})

function addFoodImageToRestaurantMenu(food){
    const imgElement = document.createElement("img")
    imgElement.src = food.image
    imgElement.addEventListener('click', () => {
        displayFoodDetails(food)
    })
    foodMenuDivElement.appendChild(imgElement)
}

function displayFoodDetails(food){
    detailImageElement.src = food.image
    detailNameElement.textContent = food.name
    foodDescriptionTextElement.textContent = food.description
    detailRestaurantElement.textContent = food.restaurant
    detailLocationElement.textContent = food.address
    directionsLinkElement.href = food.google_maps_link
    yelpLinkElement.href = food.yelp_link
}