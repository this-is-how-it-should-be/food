const foodMenuDivElement = document.getElementById("food-menu")
const foodDetailsSectionDivElement = document.getElementById("food-details-section")
const restaurantDetailsSectionDivElement = document.getElementById('restaurant-details-section')
const detailImageElement = document.getElementById("detail-image")
const detailNameElement = document.getElementById('detail-name')
const detailRestaurantElement = document.getElementById('detail-restaurant')
const detailLocationElement = document.getElementById('detail-location')

fetch("http://localhost:3000/foods")
.then(response => response.json())
.then(foods => {
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
    detailRestaurantElement.textContent = food.restaurant
    detailLocationElement.textContent = food.address
    detailLocationElement.href = food.google_maps_link
}