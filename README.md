# This Is How Food Should Be

## Introduction

This is a webpage that displays images of the most mouth-watering foods imaginable. When a food image is clicked, the details for the food will be displayed in the section below the images including an enlarged image of the food, the name of the food, a description of the food, the name of the restaurant where the food came from, the location of the restaurant, a clickable link that takes you to the Google Maps location for the restaurant, and a clickable link that takes you to the Yelp page for the restaurant.

All you need to do is click on the image of a food that you like, you'll see all of the information for the food and restaurant where that image was taken, and then off you go to your next food adventure. Excited? Great! After all - this is how food should be! Mouthwatering and exciting! Have fun! :wink:

This webpage was built with Flask.

## Local Setup Instructions

Here are local setup instructions necessary for opening this webpage locally on your browser. Please note that you'll need to use a terminal that can execute git commands to be able to run the commands in steps 1 and 3 of these local setup instructions.

1. Run the following command in your terminal to create a copy of this repository in your computer:

    ```sh
    git clone https://github.com/this-is-how-it-should-be/food.git
    ```

2. Run the following command in your terminal to change your current working directory to the `food` directory:

    ```sh
    cd food
    ```

3. Run the following command in your terminal to switch to the `flask` branch of this repository:

    ```sh
    git checkout flask
    ```

4. Run the following command in your terminal to create a virtual environment for this project and install the dependencies from the `Pipfile.lock` file:

    ```sh
    pipenv install
    ```

5. Run the following command in your terminal to activate this project's virtual environment:

    ```sh
    pipenv shell
    ```

6. Run the following command in your terminal to change your current working directory to the `server` directory:

    ```sh
    cd server
    ```

7. Run the following command in your terminal to run the Flask app:

    ```sh
    python app.py
    ```

8. Open [http://localhost:4000](http://localhost:4000) to view the webpage in your browser.