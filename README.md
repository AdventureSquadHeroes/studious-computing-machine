# Recipe Website

This repository contains a Python application that generates recipes based on ingredients, cuisine, type of cooking equipment, and diet. It utilizes the `https://api.spoonacular.com` API to fetch recipes and provide the user with a list of recipes that they can try out.

## Requirements

- Docker

## Installation

1. Clone the repository to your local machine.
2. Navigate to the repository directory.
3. Create a `.env` file in the root directory and add your Spoonacular API key using the format `API_KEY=your_api_key_here`.
4. Build the Docker image using the command `docker build -t my-flask-app .`.

## Usage

1. Run the application in a Docker container using the command `docker run -d -p 5000:5000 my-flask-app`.
2. Open your web browser and navigate to `http://localhost:5000`.
3. The application will prompt you to enter ingredients or effects of herbs that you would like to use in your recipe.
4. Enter the ingredients or effects separated by commas and click the "Search" button.
5. The application will then fetch a list of recipes that match your input and display them on the page.
6. Choose a recipe by clicking its title and the application will display the recipe details, including the ingredients and instructions.
7. To stop the Docker container, use the command `docker stop [CONTAINER ID]`.

## Contributing

Contributions are welcome! If you would like to contribute to this repository, please follow the steps below:

1. Fork the repository and create a new branch from `main`.
2. Make your changes and test them thoroughly.
3. Create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
