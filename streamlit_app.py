import streamlit
import pandas

streamlit.title('New Healthy Menu')

streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 and Blueberry oatmeal')
streamlit.text(' 🥗 Kale,soinach and rocket smoothiee')
streamlit.text(' 🐔 Hard boiled egg and French toast')
streamlit.text(' 🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
