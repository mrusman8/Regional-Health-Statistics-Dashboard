# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px
#def display_overview():
st.title("Overview")
data = st.header('Total Deaths')
#Add your code to display overview statistics using streamlit functions

#graph1 = px.scatter(data1, x='sepal_width', y='sepal_length', color='species', title='Graph 1')


#graph2 = px.bar(data2, x='day', y='total_bill', title='Graph 2')

#data3 = px.data.gapminder()
#graph3 = px.line(data3.query("country == 'United States'"), x='year', y='gdpPercap', title='Graph 3')
# Convert Plotly Express figures to HTML
#graph1 = data.to_html(full_html=False)
#html_graph2 = graph2.to_html(full_html=False)
#html_graph3 = graph3.to_html(full_html=False)
counter_grid_layout = f"""
<style>
    .grid-container {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
    }}
    .grid-item {{
        border: 1px solid #ddd;
        padding: 16px;
    }}
</style>
<div class="grid-container">
    <div class="grid-item">
        {data}
    </div>
    <div class="grid-item">
        {data}
    </div>
    <div class="grid-item">
        {data}
    </div>
</div>
"""

# Display the grid layout in Streamlit
st.html(counter_grid_layout, unsafe_allow_html=True)

