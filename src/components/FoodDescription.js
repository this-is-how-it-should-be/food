function FoodDescription({displayedFood}){
    return (
        <div id="food-description-container">
            <h1 id="food-description-header">
                Description: 
                <span id="food-description-text">{displayedFood.description}</span>
            </h1>
        </div>
    );
}

export default FoodDescription;