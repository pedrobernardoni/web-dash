import streamlit as st
import pandas as pd

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Select a book", books)

df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_filtered = df_reviews[df_reviews["book name"] == book]

book_title = df_book["book title"].iloc[0]
st.title(f"{book_title}")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Price", f"$ {df_book['book price'].iloc[0]}")
col2.metric("Rating", df_book["rating"].iloc[0])
col3.metric("Year of Publication", df_book["year of publication"].iloc[0])
col4.metric("Genre", df_book["genre"].iloc[0])

st.divider()
st.subheader("Customer Reviews")

for row in df_reviews_filtered.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.markdown(
        f"<div style='text-align: justify;'>{row[5]}</div>",
        unsafe_allow_html=True
    )
