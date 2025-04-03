import Header from "./Header";
import FoodMenu from "./FoodMenu";
import FoodDetails from "./FoodDetails";
import FoodDescription from "./FoodDescription";
import RestaurantDetails from "./RestaurantDetails";

import { useState, useEffect } from "react";

function App() {

  const [foods, setFoods] = useState([]);
  const [displayedFood, setDisplayedFood] = useState(null)

  useEffect(getFoods, [])

  function getFoods(){
    fetch("https://raw.githubusercontent.com/this-is-how-it-should-be/food/refs/heads/main/db.json")
    .then(response => response.json())
    .then(data => {
      setFoods(data.foods)

      if(data.foods.length > 0){
        const firstFood = data.foods[0]
        setDisplayedFood(firstFood)
      }
    })
  }

  return (
    <>
      <Header/>
      <FoodMenu foods={foods}/>
      {displayedFood ? <FoodDetails displayedFood={displayedFood}/> : null}
      {displayedFood ? <FoodDescription displayedFood={displayedFood}/> : null}
      {displayedFood ? <RestaurantDetails displayedFood={displayedFood}/> : null}
    </>
  );
}

export default App;
