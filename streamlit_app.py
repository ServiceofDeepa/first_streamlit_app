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
#fruit_Selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado':'Strawberries','Calories'])
#fruit_Selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),[[False, True, False]])



#fruits_to_show = my_fruit_list.loc[fruit_Selected];
#fruits_to_show = my_fruit_list.loc[[False, True, False]];

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
