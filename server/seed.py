from app import app
from models import db, Food

with app.app_context():
    Food.query.delete()

    food1 = Food(name="Lucky Six Soup Dumplings", image="https://raw.githubusercontent.com/this-is-how-it-should-be/food/refs/heads/main/assets/images/lucky_six_soup_dumplings.png", description="A mouthwatering medley of six uniquely-flavored soup dumplings, made with all-natural ingredients.", restaurant="Nan Xiang Soup Dumplings - Flushing", address="39-16 Prince St #104, Flushing, NY 11354", google_maps_link="https://maps.app.goo.gl/kmd36LoHzbmoWYXw8?g_st=com.google.maps.preview.copy", yelp_link="https://yelp.to/csN5cFyYNw")
    food2 = Food(name="Tokyo Tonkotsu Shouyu Ramen", image="https://raw.githubusercontent.com/this-is-how-it-should-be/food/refs/heads/main/assets/images/tokyo_tonkotsu_shouyu.png", description="Served with Chashu Pork, Half Marinated Egg, Corn, Bamboo Shoots, Wakame, Scallion, Nori (Pork Broth).", restaurant="KYURAMEN - Flushing", address="133-42 37th Ave, Flushing, NY 11354", google_maps_link="https://maps.app.goo.gl/YJ8hJwh8Y2KNiroj7?g_st=com.google.maps.preview.copy", yelp_link="https://yelp.to/eysxvTDWRG")
    food3 = Food(name="Crazy Nana Roll", image="https://raw.githubusercontent.com/this-is-how-it-should-be/food/refs/heads/main/assets/images/crazy_nana_roll.png", description="Filled with shrimp tempura, spicy tuna, along with a layer of spicy lobster, mango, eel and avocado. Topped with a fried soft shell crab and sprinkled with crab crunch.", restaurant="Izakaya Nana", address="141-28 Northern Blvd, Flushing, NY 11354", google_maps_link="https://maps.app.goo.gl/vbMX61xamxjwTFXn9?g_st=com.google.maps.preview.copy", yelp_link="https://yelp.to/PkDyYPrzIy")
    food4 = Food(name="Lamb Tikka", image="https://raw.githubusercontent.com/this-is-how-it-should-be/food/refs/heads/main/assets/images/lamb_tikka.png", description="Tender chunks of lamb, marinated in special seasonings and grilled to perfection on skewers.", restaurant="Kabul Kabab House", address="42-51 Main St, Flushing, NY 11355", google_maps_link="https://maps.app.goo.gl/spgtrzfMFQUrynk1A?g_st=com.google.maps.preview.copy", yelp_link="https://yelp.to/q4-SIIlEHo")
    
    db.session.add_all([food1, food2, food3, food4])
    db.session.commit()

    print("🌱 Foods successfully seeded! 🌱")