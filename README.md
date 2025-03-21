# NavigoGraph
Customer Journey Mapping Using Graph Theory is a web app that simulates user interactions on an e-commerce platform. It generates a visual graph to analyze customer behavior, providing insights into navigation patterns, conversion rates, and drop-off rates, helping businesses optimize user experience and decision-making.

# Customer Journey Mapping Using Graph Theory

This project simulates user interactions across a typical e-commerce platform and generates a graph to visualize the customer journey. The goal is to understand customer behavior by mapping their movement through various pages on the website.

## Features

- **Simulate Website Navigation**: Interact with the platform by navigating through different pages, such as Homepage, Product Page, Cart, Checkout, and Payment.
- **Graph Generation**: Generate a directed graph that shows the flow of customer interactions between different pages.
- **Metrics**: Track key metrics like conversion rate and drop-off rate based on user interactions.
- **Downloadable Graph**: Save the generated customer journey graph as an image for further analysis or reporting.
- **Reset Functionality**: Clear the entire journey to start fresh, simulating a new user's journey.

## How it Works

- The user navigates through different pages of the website.
- The journey data (page transitions) is recorded and used to generate a graph using NetworkX.
- The generated graph provides a visual representation of customer behavior and movement.
- Metrics such as conversion rate and drop-off rate are displayed to analyze how users are interacting with the platform.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/customer-journey-mapping.git
    ```

2. Navigate to the project directory:
    ```bash
    cd customer-journey-mapping
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Technologies Used

- **Streamlit**: For building the interactive web interface.
- **NetworkX**: For graph creation and analysis.
- **Matplotlib**: For rendering the graph visually.
- **Pandas**: For handling and processing the journey data.

## Metrics

- **Conversion Rate**: The percentage of users who successfully reach the "Payment Success" page.
- **Drop-off Rate**: The percentage of users who exit before reaching the "Payment Success" page.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to open issues or contribute to the project!


