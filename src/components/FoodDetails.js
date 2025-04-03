function FoodDetails({displayedFood}){
    return (
        <div id="food-details-section">
            <img id="detail-image" src={displayedFood.image} alt={displayedFood.name} />
            <h1 id="detail-name">{displayedFood.name}</h1>
        </div>
    );
}

export default FoodDetails;