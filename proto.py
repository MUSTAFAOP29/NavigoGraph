import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Title
st.set_page_config(page_title="Customer Journey Mapping", layout="wide")
st.title("Customer Journey Mapping Using Graph Theory")

st.markdown("""
This interactive interface simulates user interactions across a typical e-commerce platform. Based on your interactions (clicks), a customer journey graph will be generated.
""")

st.sidebar.header("Simulated Website Navigation")

# Session state to record interactions
if 'journey_data' not in st.session_state:
    st.session_state.journey_data = []
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Homepage'

# Function to log transition
def log_transition(new_page):
    st.session_state.journey_data.append((st.session_state.current_page, new_page))
    st.session_state.current_page = new_page

# Sidebar buttons for navigation
if st.sidebar.button("Go to Homepage"):
    log_transition("Homepage")

if st.sidebar.button("Browse Products"):
    log_transition("Product Page")

if st.sidebar.button("View Cart"):
    log_transition("Cart")

if st.sidebar.button("Customer Support"):
    log_transition("Support")

if st.sidebar.button("Proceed to Checkout"):
    log_transition("Checkout")

if st.sidebar.button("Make Payment"):
    log_transition("Payment Success")

# Display user journey so far
st.subheader("Interaction Log")
if st.session_state.journey_data:
    df_journey = pd.DataFrame(st.session_state.journey_data, columns=["From", "To"])
    df_journey["Weight"] = 1
    df_summary = df_journey.groupby(["From", "To"]).count().reset_index()
    st.dataframe(df_summary)

    # Generate Graph Button
    if st.button("Generate Customer Journey Graph"):
        G = nx.DiGraph()
        for index, row in df_summary.iterrows():
            G.add_edge(row['From'], row['To'], weight=row['Weight'])

        fig, ax = plt.subplots(figsize=(10, 6))
        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2500, edge_color='gray', arrows=True)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("Customer Journey Graph")
        st.pyplot(fig)
else:
    st.info("Start interacting with the sidebar to simulate user navigation across the platform.")
