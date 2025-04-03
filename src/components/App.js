import Header from "./Header";
import FoodMenu from "./FoodMenu";

import { useState, useEffect } from "react";

function App() {

  const [foods, setFoods] = useState([]);

  useEffect(getFoods, [])

  function getFoods(){
    fetch("https://raw.githubusercontent.com/this-is-how-it-should-be/food/refs/heads/main/db.json")
    .then(response => response.json())
    .then(data => {
      setFoods(data.foods)
    })
  }

  return (
    <>
      <Header/>
      <FoodMenu/>
    </>
  );
}

export default App;
