function RestaurantDetails({displayedFood}){
    return (
        <div id="restaurant-details-section">
            <h1>Restaurant: <span id="detail-restaurant">{displayedFood.restaurant}</span></h1>
            <h1>Location: <span id="detail-location">{displayedFood.address}</span></h1>
        </div>
    );
}

export default RestaurantDetails;