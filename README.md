# OOP Coffee Machine

This is a Python-based coffee machine simulation that demonstrates basic object-oriented programming principles. The application allows users to order coffee, process payments, and manage resources using a simple command-line interface.

## Files

- **`main.py`**: The main driver of the coffee machine application. Handles user interactions and integrates with other components to fulfill coffee orders.
- **`menu.py`**: Defines the `Menu` and `MenuItem` classes. Manages the available menu items and provides functionality to search for specific drinks.
- **`coffee_maker.py`**: Defines the `CoffeeMaker` class. Handles the resources required to make coffee and checks if sufficient resources are available.
- **`money_machine.py`**: Defines the `MoneyMachine` class. Manages payment processing and keeps track of the profit.

## Requirements

1. **Print Report**: Displays a report of the available resources and profit.
2. **Check Resources**: Determines if there are enough resources to make a requested drink.
3. **Process Coins**: Handles the insertion of coins and calculates the total amount.
4. **Check Transaction**: Validates if the payment is sufficient and processes the transaction.
5. **Make Coffee**: Prepares the coffee and updates the resources accordingly.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/oop-coffee-machine2.git
    ```

2. Navigate to the project directory:
    ```bash
    cd oop-coffee-machine2
    ```

3. Ensure you have Python installed. You can check this by running:
    ```bash
    python --version
    ```

4. Run the application:
    ```bash
    python main.py
    ```

## Usage

1. When you run the application, you will be prompted with a menu of available drinks.
2. Enter the name of the drink you want to order.
3. Insert the required coins when prompted.
4. The machine will check if resources are sufficient and if the payment is correct.
5. If everything is in order, your coffee will be prepared, and you can choose to order more or exit.

## Example

```plaintext
Order Please menu are latte/espresso/cappuccino: latte
Please insert coins.
How many quarters?: 1
How many dimes?: 1
How many nickles?: 0
How many pennies?: 0
Here is $0.60 in change.
Here is your latte ☕️. Enjoy!
you wanna have something more. type y for yes, anything else for no: n
