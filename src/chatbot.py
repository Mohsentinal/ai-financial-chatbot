from transformers import pipeline
from utils import log_interaction, calculate_compound_interest

# Load GPT-Neo (1.3B) Model and Tokenizer
chat_model = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B", framework="pt")


def chatbot():
    """
    A financial chatbot with integrated GPT-Neo and compound interest calculation.
    """
    print("Welcome to the Financial Chatbot!")
    print("You can ask me financial questions or request a compound interest calculation.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Handle compound interest calculation
        if "compound interest" in user_input.lower():
            try:
                principal = float(input("Enter the principal amount: "))
                rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
                time = float(input("Enter the number of years: "))
                n = int(input(
                    "Enter the number of times interest is compounded per year (e.g., 1 for yearly, 12 for monthly): "))
                result = calculate_compound_interest(principal, rate, time, n)
                response = f"After {time} years, your investment will grow to: {result:.2f}"
                print(f"Chatbot: {response}")
            except ValueError:
                response = "Please enter valid numerical inputs."
                print(f"Chatbot: {response}")

            # Log the interaction
            log_interaction(user_input, response)
            continue

        # Generate a response using GPT-Neo
        try:
            prompt = f"You are a financial expert. Provide a clear and concise answer to: {user_input}"
            response = chat_model(prompt, max_length=150, num_return_sequences=1, temperature=0.7)
            chatbot_response = response[0]['generated_text'].strip()
            print(f"Chatbot: {chatbot_response}")

            # Log the interaction
            log_interaction(user_input, chatbot_response)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    chatbot()
