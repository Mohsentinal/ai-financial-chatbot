import logging

# Configure logging
logging.basicConfig(filename="data/chatbot_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

def log_interaction(user_input, response):
    """
    Logs user input and chatbot response.
    """
    logging.info(f"User: {user_input}")
    logging.info(f"Chatbot: {response}")

def calculate_compound_interest(principal, rate, time, n=1):
    """
    Calculate compound interest.
    Args:
        principal (float): Initial amount of money.
        rate (float): Annual interest rate (in decimal form, e.g., 0.05 for 5%).
        time (float): Number of years the money is invested for.
        n (int): Number of times interest is compounded per year (default is 1).
    Returns:
        float: The amount of money accumulated after n years, including interest.
    """
    return principal * (1 + rate / n) ** (n * time)
