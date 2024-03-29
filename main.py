from neural_net_optimizer import NeuralNetOptimizer
from monte_carlo_optimizer import MonteCarloOptimizer
from quantum_comp_optimizer import QuantumAnnealingOptimizer
from SQL_connector import DatabaseManager
from portfolio_gui import PortfolioGUI

if __name__ == "__main__":
    nn_optimizer = NeuralNetOptimizer()
    mc_optimizer = MonteCarloOptimizer()
    qa_optimizer = QuantumAnnealingOptimizer() 
    db_manager = DatabaseManager()
    gui = PortfolioGUI(nn_optimizer, mc_optimizer, qa_optimizer)
    gui.run_gui()
