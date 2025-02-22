# Libraries import
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data import
df4 = pd.read_csv("df44.csv")
df5 = pd.read_csv("df5.csv")
df6 = pd.read_csv("df6.csv")
df8 = pd.read_csv("df88.csv")
df_predictions_sarima = pd.read_csv("df_predictions_sarima.csv")

# Interface
st.title("Analytical Dashboard")
st.sidebar.header("Selection of Visualizations")

# Graphics
opcion = st.sidebar.radio("Select a graphic:", [
    "Rentability of different sizes of products",
    "Evolution of Sells for Top Products",
    "Prediction of Sells for Next Months",
    "Sales Prediction by Product",
    "Top 20 Profitable Products",
    "top_20_less_profitable"
])

# Graphic 1: Rentability of different sizes of products
if opcion == "Rentability of different sizes of products":
    st.subheader("Rentability of different sizes of products")
    tamaño = df6["space"]
    porcentaje = df6["rentability_percentage"]
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(tamaño, porcentaje, color="blue")
    ax.set_xlabel("Space that a product occupies")
    ax.set_ylabel("Rentability (%)")
    ax.set_title("Rentability by size of products")
    
    st.pyplot(fig)

# Graphic 2: Evolution of Sales for Top Products
elif opcion == "Evolution of Sells for Top Products":
    st.subheader("Evolution of Sales for Top Products")
    sells_by_products_evo = df8.groupby(['month', 'products'])['total_revenue'].sum().unstack()
    top_productos = sells_by_products_evo.sum().nlargest(5).index  # Top 5 best-selling products
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sells_by_products_evo[top_productos].plot(ax=ax, marker='o')
    ax.set_title("Revenue Evolution of Top-Selling Products")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")
    ax.legend(title="Product")
    ax.grid()
    
    st.pyplot(fig)

# Graphic 3: Prediction of Sells for Next Months
elif opcion == "Prediction of Sells for Next Months":
    st.subheader("Prediction of Sells for Next Months")
    predicted_revenue = df_predictions_sarima.groupby("month")["predicted_total_revenue"].sum()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(predicted_revenue.index, predicted_revenue.values, marker='o', linestyle='-', color="blue", label="Predicted Revenue")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Predicted Revenue")
    ax.set_title("Prediction of Sells for Next Months")
    ax.legend()
    ax.grid()
    
    st.pyplot(fig)
    
    file_name = "predicted_revenue_analysis.png"
    fig.savefig(file_name, dpi=150, bbox_inches="tight")
    
    with open(file_name, "rb") as file:
        st.download_button(label="Download Graph", data=file, file_name="predicted_revenue_analysis.png", mime="image/png")

# Graphic 4: Sales Prediction by Product
elif opcion == "Sales Prediction by Product":
    st.subheader("Sales Prediction by Product")
    selected_product = st.selectbox("Select a Product:", df_predictions_sarima["products"].unique())
    subset = df_predictions_sarima[df_predictions_sarima["products"] == selected_product]
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(subset["month"], subset["predicted_units_sold"], marker='o', linestyle='-', label=selected_product)
    ax.set_xlabel("Month")
    ax.set_ylabel("Predicted Units Sold")
    ax.set_title(f"Sales Prediction: {selected_product}")
    ax.legend()
    ax.grid()
    
    st.pyplot(fig)
    
    file_name = f"sales_prediction_{selected_product.replace(' ', '_')}.png"
    fig.savefig(file_name, dpi=150, bbox_inches="tight")
    
    with open(file_name, "rb") as file:
        st.download_button(label="Download Graph", data=file, file_name=file_name, mime="image/png")

# Graphic 5: Top 20 Profitable Products
elif opcion == "Top 20 Profitable Products":
    st.subheader("Top 20 Profitable Products")
    productos_rentables = df5.groupby("products")["predicted_rentability"].mean().sort_values(ascending=False)
    top_rentables = productos_rentables.head(20)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(top_rentables.index[::-1], top_rentables[::-1], color="royalblue", edgecolor="black")
    ax.set_xlabel("Predicted Profitability")
    ax.set_ylabel("Product")
    ax.set_title("Top 20 Profitable Products")
    ax.grid(axis="x", linestyle="--", alpha=0.6)
    
    st.pyplot(fig)

# Graphic 6: Top 20 Less Profitable Products
elif opcion == "top_20_less_profitable":
    st.subheader("Top 20 Less Profitable Products")
    productos_no_rentables = df5.groupby("products")["predicted_rentability"].mean().sort_values(ascending=True)
    top_no_rentables = productos_no_rentables.head(20)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(top_no_rentables.index[::-1], top_no_rentables[::-1], color="red", edgecolor="black")
    ax.set_xlabel("Predicted Profitability")
    ax.set_ylabel("Product")
    ax.set_title("Top 20 Less Profitable Products")
    ax.grid(axis="x", linestyle="--", alpha=0.6)
    
    st.pyplot(fig)


