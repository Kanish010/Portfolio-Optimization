# Portfolio Optimization with Neural Networks, Monte Carlo Simulations and Quantum Annealing
This Python script provides a graphical user interface (GUI) for portfolio optimization using neural network predictions and Monte Carlo simulations. The script utilizes the Yahoo Finance API to fetch historical stock data, TensorFlow for building and training the neural network, and the scipy library for portfolio optimization.

# Dependencies:
Before running the script, make sure to install the required libraries by executing the following command in your terminal or command prompt:

pip install numpy yfinance scipy tensorflow tkinter cirq mysql.connector

# Classes
### NeuralNetOptimizer:
The NeuralNetOptimizer class contains methods for fetching historical stock data, building and training a neural network, and performing portfolio optimization based on neural network predictions.

### MonteCarloOptimizer:
The MonteCarloOptimizer class implements methods for fetching historical stock data, performing Monte Carlo simulations for portfolio optimization, and displaying results.

### QuantumAnnealingOptimizer:
The QuantumAnnealingOptimizer class levrages quantum computing techniques, aims to find optimal portfolio weights efficiently, potentially offering advantages over classical methods. 

### PortfolioGUI:
The PortfolioGUI class provides a graphical user interface for users to input the number of stocks and initiate the portfolio optimization process. It utilizes instances of NeuralNetOptimizer and MonteCarloOptimizer to perform optimization and displays results in a scrollable text widget. Allows the user to choose between using the Neural Network or the Monte Carlo Simulation through a widget on the GUI. 

### DatabaseManager
The DatabaseManager class is designed to handle database operations related to storing stock symbols and portfolio information such as the type of optimizer used and the weight assigned to each stock in the portfolio. The class establishes a connection to a local database and inserts the relevant data into the database. The database can be created by running the schema in "database_schema.sql". 

# Disclaimer
This script is provided for educational purposes only and should not be considered as financial advice. Always conduct thorough research and consult with financial professionals before making investment decisions.