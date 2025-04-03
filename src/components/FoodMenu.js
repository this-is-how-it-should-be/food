function FoodMenu({foods}){

    const imgElements = foods.map(food => {
        return <img key={food.id} src={food.image} alt={food.name}/>
    })

    return (
        <div id="food-menu">
            {imgElements}
        </div>
    );
}

export default FoodMenu;