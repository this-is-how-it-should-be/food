function FoodMenu({foods, updateDisplayedFood}){

    const imgElements = foods.map(food => {
        return <img onClick={() => updateDisplayedFood(food)} key={food.id} src={food.image} alt={food.name}/>
    })

    return (
        <div id="food-menu">
            {imgElements}
        </div>
    );
}

export default FoodMenu;