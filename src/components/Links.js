function Links({displayedFood}){
    return (
        <>
            <a id="directions-link" href={displayedFood.google_maps_link}>
                <button id="directions-button">Get Directions</button>
            </a>
            <a id="yelp-link" href={displayedFood.yelp_link}>
                <button id="yelp-button">See Yelp Reviews</button>
            </a>
        </>
    )
}

export default Links;