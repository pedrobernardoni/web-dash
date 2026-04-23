import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

def apply_pointer_cursor_fix():
    """Force pointer cursor for select widgets and dropdown options."""
    st.markdown(
        """
        <style>
            div[data-baseweb="select"] > div {
                cursor: pointer;
            }

            div[data-baseweb="select"] * {
                cursor: pointer !important;
            }

            ul[role="listbox"] li,
            ul[role="listbox"] li * {
                cursor: pointer !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def home_page():
    st.title("Top 100 Trending Books")
    st.subheader("Customer Reviews")

    df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

    # Slider to filter books by maximum price.
    price_max = df_top100_books["book price"].max()
    price_min = df_top100_books["book price"].min()

    max_price = st.sidebar.slider("Price range 💰", price_min, price_max, price_max)
    df_filtered = df_top100_books[df_top100_books["book price"] <= max_price]

    df_filtered

    figure_one = px.bar(df_filtered["year of publication"].value_counts())
    figure_two = px.histogram(df_filtered["book price"])

    col1, col2 = st.columns(2)
    col1.plotly_chart(figure_one)
    col2.plotly_chart(figure_two)


def main():
    # Adding image to the page
    try:
        img_file = Image.open("./assets/favicon.ico")
    except FileNotFoundError:
        img_file = None

    st.set_page_config(
        page_title="BookWorms",
        page_icon=img_file if img_file else None,
        layout="wide"
    )
    apply_pointer_cursor_fix()

    pg = st.navigation(
        [
            st.Page(home_page, title="Home", icon="🏠", default=True),
            st.Page("pages/book_reviews.py", title="Book Reviews", icon="📚"),
        ]
    )
    pg.run()


if __name__ == "__main__":
    main()
