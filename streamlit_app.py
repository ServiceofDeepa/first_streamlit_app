import streamlit;
streamlit.title('My parents New Healthy Diner');
streamlit.header ('Breakfast Menu');
streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal');
streamlit.text ('🥗 Kale, Spinach & Rocket Smoothie');
streamlit.text ('🐔 Hard-Boiled Free-Range Egg');
streamlit.text ('🥑🍞 Avocado Toast');
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# To pick fruits by name
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_Selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruit_Selected];

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# Formatting the data output.. take the data version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Display the data as a table
streamlit.dataframe(fruityvice_normalized)
