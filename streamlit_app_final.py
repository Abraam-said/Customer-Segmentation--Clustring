
import streamlit as st
import numpy as np
import pandas as pd

# Read data
df = pd.read_csv("Clustered_data.csv")
pivot_total = pd.read_csv("Clustered_pivot.csv")

# Function to get recommendations
def get_Recommendation(User):
    Cluster = df[df["User_Id"] == int(User)]["Cluster"].unique()[0]
    df_cluster = df[df["Cluster"] == Cluster]
    df_cluster = df_cluster.groupby("Mer_Name")["Trx_Vlu"].sum().nlargest(3)

    # Stylish output
    st.markdown(f"## Recommendations for User {User}")
    for index, mer in enumerate(df_cluster.index, start=1):
        st.success(f"**Recommendation {index}:** {mer}")

# Main Streamlit App
def main():
    # Set page title and styles
    st.set_page_config(page_title="Merchant Recommendations", page_icon="🛍️", layout="wide")

    # Add a title in the middle of the page using Markdown and CSS
    st.markdown("<h1 style='text-align: center; color:#f07c24'>Merchant Recommendation App 🛍️</h1>", unsafe_allow_html=True)

    # User input for User Id
    User = st.text_input("Enter User Id", help="Enter the User Id for personalized recommendations")

    # Button to trigger recommendations
    if st.button("Get Recommendations"):
        get_Recommendation(User)

# Run the app
if __name__ == "__main__":
    main()
