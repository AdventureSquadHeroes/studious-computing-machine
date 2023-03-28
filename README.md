# Recipe Website

This repository contains a Python application that generates recipes based on ingredients or effects of herbs. It utilizes the `https://api.spoonacular.com` API to fetch recipes and provide the user with a list of recipes that they can try out.

## Requirements

- Python 3.6 or higher
- `requests` library (`pip install requests`)
- `dotenv` library (`pip install python-dotenv`)

## Installation

1. Clone the repository to your local machine.
2. Navigate to the repository directory and create a virtual environment using `python3 -m venv env`.
3. Activate the virtual environment using `source env/bin/activate`.
4. Install the required libraries using `pip install -r requirements.txt`.
5. Create a `.env` file in the root directory and add your Spoonacular API key using the format `API_KEY=your_api_key_here`.

## Usage

1. Run the application by running `python main.py` in your terminal.
2. The application will prompt you to enter ingredients or effects of herbs that you would like to use in your recipe.
3. Enter the ingredients or effects separated by commas and press enter.
4. The application will then fetch a list of recipes that match your input and display them in the terminal.
5. Choose a recipe by entering its index and the application will display the recipe details, including the ingredients and instructions.

## Contributing

Contributions are welcome! If you would like to contribute to this repository, please follow the steps below:

1. Fork the repository and create a new branch from `main`.
2. Make your changes and test them thoroughly.
3. Create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
