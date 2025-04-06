javascript_code = """
document.addEventListener('DOMContentLoaded', updateDOM)

function updateDOM(){
    const foodDetailsSectionDivElement = document.getElementById("food-details-section")
    const restaurantDetailsSectionDivElement = document.getElementById('restaurant-details-section')

    fetch("http://localhost:4000/foods")
    .then(response => response.json())
    .then(foods => {
        foods.forEach(addFoodImageToRestaurantMenu)
        
        if(foods.length > 0){
            displayFoodDetails(foods[0])
            foodDetailsSectionDivElement.style.display = "block"
            restaurantDetailsSectionDivElement.style.display = "block"
        }
    })
}

function addFoodImageToRestaurantMenu(food){
    const imgElement = document.createElement("img")
    imgElement.src = food.image
    imgElement.addEventListener('click', () => {
        displayFoodDetails(food)
    })

    const foodMenuDivElement = document.getElementById("food-menu")
    foodMenuDivElement.appendChild(imgElement)
}

function displayFoodDetails(food){
    const detailImageElement = document.getElementById("detail-image")    
    detailImageElement.src = food.image

    const detailNameElement = document.getElementById('detail-name')
    detailNameElement.textContent = food.name

    const foodDescriptionTextElement = document.getElementById('food-description-text')
    foodDescriptionTextElement.textContent = food.description

    const detailRestaurantElement = document.getElementById('detail-restaurant')
    detailRestaurantElement.textContent = food.restaurant
    
    const detailLocationElement = document.getElementById('detail-location')
    detailLocationElement.textContent = food.address

    const directionsLinkElement = document.getElementById('directions-link')
    directionsLinkElement.href = food.google_maps_link
    
    const yelpLinkElement = document.getElementById('yelp-link')
    yelpLinkElement.href = food.yelp_link
}
"""