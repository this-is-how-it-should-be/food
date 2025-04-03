import Header from "./Header";
import FoodMenu from "./FoodMenu";

import { useState } from "react";

function App() {

  const [foods, setFoods] = useState([]);

  return (
    <>
      <Header/>
      <FoodMenu/>
    </>
  );
}

export default App;
