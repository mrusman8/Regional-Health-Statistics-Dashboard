import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Read the data
data_path = r"C:\Users\PMLS\Downloads\wb eda data.xlsx"
df = pd.read_excel(data_path)

st.title('Pakistan Statistic Dashboard')

# Set the index to the 'Years' column
df.set_index('Years', inplace=True)

original_start_year = df.index.min()
original_end_year = df.index.max()

# Function to filter data based on selected options
def filter_data(df, options, start_year, end_year):
    filtered_df = df.loc[start_year:end_year, options]
    return filtered_df

# Function to render page
def render_page(page_name):
    if page_name == 'Population':
        st.header('Population')
        options = st.multiselect('Select Data',
                                 ['Population, total', 'Population, female', 'Population, male', 'Urban population',
                                  'Rural population'])
        plot_type = st.selectbox('Select Plot Type', ['Line Plot', 'Bar Plot'])

        start_year = st.slider('Select Start Year', min_value=original_start_year, max_value=original_end_year,
                               value=original_start_year, step=1)
        end_year = st.slider('Select End Year', min_value=original_start_year, max_value=original_end_year,
                             value=original_end_year, step=1)

        filtered_df = filter_data(df, options, start_year, end_year)

        # Plot
        fig = go.Figure()

        if plot_type == 'Line Plot':
            for col in options:
                fig.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df[col], mode='lines+markers', name=col))
        elif plot_type == 'Bar Plot':
            for col in options:
                fig.add_trace(go.Bar(x=filtered_df.index, y=filtered_df[col], name=col))

        fig.update_layout(
            title="Population Plot",
            xaxis_title="Years",
            yaxis_title="Values",
            legend_title="Legend",
            hovermode='x unified',  # Show hover information for all traces
        )

        st.plotly_chart(fig)

        st.header('Growth rate')
        selected_loan_options = st.multiselect('Select Data',
                                               ['Population growth (annual %)',
                                                'Life expectancy at birth, total (years)'])
        plot_type_trade = st.selectbox('Select Plot Type ', ['Line Plot', 'Bar Plot'], key='loan_plot_type')

        start_year_trade = st.slider('Select Start Year ', min_value=original_start_year,
                                     max_value=original_end_year,kiy
                                     value=original_start_year, step=1, key='loan_start_year')
        end_year_trade = st.slider('Select End Year ', min_value=original_start_year,
                                   max_value=original_end_year,
                                   value=original_end_year, step=1, key='loan_end_year')

        if selected_loan_options:
            filtered_trade_df = filter_data(df, selected_loan_options, start_year_trade, end_year_trade)
            trade_fig = go.Figure()
            for col in selected_loan_options:
                if plot_type_trade == 'Line Plot':
                    trade_fig.add_trace(go.Scatter(x=filtered_trade_df.index, y=filtered_trade_df[col],
                                                   mode='lines+markers', name=col))
                elif plot_type_trade == 'Bar Plot':
                    trade_fig.add_trace(go.Bar(x=filtered_trade_df.index, y=filtered_trade_df[col], name=col))

            trade_fig.update_layout(
                title="Growth Plot",
                xaxis_title="Years",
                yaxis_title="Values",
                legend_title="Legend",
                hovermode='x unified',  # Show hover information for all traces
            )

            st.plotly_chart(trade_fig)
        return

    elif page_name == 'GDP Growth':
        st.header('GDP Growth')
        selected_options = st.multiselect('Select Data',
                                          ['GDP growth (annual %)', 'Inflation, GDP deflator (annual %)'])
        plot_type = st.selectbox('Select Plot Type', ['Line Plot', 'Bar Plot'])

        start_year = st.slider('Select Start Year', min_value=original_start_year, max_value=original_end_year,
                               value=original_start_year, step=1)
        end_year = st.slider('Select End Year', min_value=original_start_year, max_value=original_end_year,
                             value=original_end_year, step=1)

        filtered_df = filter_data(df, selected_options, start_year, end_year)

        # Plot
        fig = go.Figure()

        if plot_type == 'Line Plot':
            for col in selected_options:
                fig.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df[col], mode='lines+markers', name=col))
        elif plot_type == 'Bar Plot':
            for col in selected_options:
                fig.add_trace(go.Bar(x=filtered_df.index, y=filtered_df[col], name=col))

        fig.update_layout(
            title="GDP Growth Plot",
            xaxis_title="Years",
            yaxis_title="Values",
            legend_title="Legend",
            hovermode='x unified',  # Show hover information for all traces
        )

        st.plotly_chart(fig)

        st.header('Imports and Exports (% of GDP)')
        selected_trade_options = st.multiselect('Select  Data',
                                                ['Imports of goods and services (% of GDP)',
                                                 'Exports of goods and services (% of GDP)'])
        plot_type_trade = st.selectbox('Select Plot Type ', ['Line Plot', 'Bar Plot'], key='trade_plot_type')

        start_year_trade = st.slider('Select Start Year ', min_value=original_start_year,
                                     max_value=original_end_year,
                                     value=original_start_year, step=1, key='trade_start_year')
        end_year_trade = st.slider('Select End Year ', min_value=original_start_year,
                                   max_value=original_end_year,
                                   value=original_end_year, step=1, key='trade_end_year')

        if selected_trade_options:
            filtered_trade_df = filter_data(df, selected_trade_options, start_year_trade, end_year_trade)
            trade_fig = go.Figure()
            for col in selected_trade_options:
                if plot_type_trade == 'Line Plot':
                    trade_fig.add_trace(go.Scatter(x=filtered_trade_df.index, y=filtered_trade_df[col],
                                                   mode='lines+markers', name=col))
                elif plot_type_trade == 'Bar Plot':
                    trade_fig.add_trace(go.Bar(x=filtered_trade_df.index, y=filtered_trade_df[col], name=col))

            trade_fig.update_layout(
                title="Trade Plot",
                xaxis_title="Years",
                yaxis_title="Values",
                legend_title="Legend",
                hovermode='x unified',  # Show hover information for all traces
            )

            st.plotly_chart(trade_fig)
        return

    elif page_name == 'Government Expenditure':
        st.header('Government Expenditure')
        options = ['General government total expenditure(% of GDP)', 'Military expenditure (% of GDP)',
                   'Government expenditure on education, total (% of GDP)', 'Current health expenditure (% of GDP)', 'Total Investment']
        selected_options = st.multiselect('Select Expenditure Data', options)
        plot_type = st.selectbox('Select Plot Type', ['Line Plot', 'Bar Plot'])

        start_year = st.slider('Select Start Year', min_value=original_start_year, max_value=original_end_year,
                               value=original_start_year, step=1)
        end_year = st.slider('Select End Year', min_value=original_start_year, max_value=original_end_year,
                             value=original_end_year, step=1)

        filtered_df = filter_data(df, selected_options, start_year, end_year)

        # Plot
        fig = go.Figure()

        if plot_type == 'Line Plot':
            for col in selected_options:
                fig.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df[col], mode='lines+markers', name=col))
        elif plot_type == 'Bar Plot':
            for col in selected_options:
                fig.add_trace(go.Bar(x=filtered_df.index, y=filtered_df[col], name=col))

        fig.update_layout(
            title="Government Expenditure Plot",
            xaxis_title="Years",
            yaxis_title="Values",
            legend_title="Legend",
            hovermode='x unified',  # Show hover information for all traces
        )

        st.plotly_chart(fig)

    elif page_name == 'Tax and Debt':
        st.header('Revenue and Remittance')
        options = ['Tax revenue (% of GDP)', 'Revenue, excluding grants (% of GDP)', 'Personal remittances, received (% of GDP)']
        selected_options = st.multiselect('Select Data', options)
        plot_type = st.selectbox('Select Plot Type', ['Line Plot', 'Bar Plot'])

        start_year = st.slider('Select Start Year', min_value=original_start_year, max_value=original_end_year,
                               value=original_start_year, step=1)
        end_year = st.slider('Select End Year', min_value=original_start_year, max_value=original_end_year,
                             value=original_end_year, step=1)

        filtered_df = filter_data(df, selected_options, start_year, end_year)

        # Plot
        fig = go.Figure()

        if plot_type == 'Line Plot':
            for col in selected_options:
                fig.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df[col], mode='lines+markers', name=col))
        elif plot_type == 'Bar Plot':
            for col in selected_options:
                fig.add_trace(go.Bar(x=filtered_df.index, y=filtered_df[col], name=col))

        fig.update_layout(
            title="Tax and remittance Plot",
            xaxis_title="Years",
            yaxis_title="Values",
            legend_title="Legend",
            hovermode='x unified',  # Show hover information for all traces
        )

        st.plotly_chart(fig)

        st.header('Debt')
        selected_loan_options = st.multiselect('Select Data',
                                                ['External debt stocks, total (DOD, current US$)', 'Total Disbursements'])
        plot_type_trade = st.selectbox('Select Plot Type ', ['Line Plot', 'Bar Plot'], key='loan_plot_type')

        start_year_trade = st.slider('Select Start Year ', min_value=original_start_year,
                                     max_value=original_end_year,
                                     value=original_start_year, step=1, key='loan_start_year')
        end_year_trade = st.slider('Select End Year ', min_value=original_start_year,
                                   max_value=original_end_year,
                                   value=original_end_year, step=1, key='loan_end_year')

        if selected_loan_options:
            filtered_trade_df = filter_data(df, selected_loan_options, start_year_trade, end_year_trade)
            trade_fig = go.Figure()
            for col in selected_loan_options:
                if plot_type_trade == 'Line Plot':
                    trade_fig.add_trace(go.Scatter(x=filtered_trade_df.index, y=filtered_trade_df[col],
                                                   mode='lines+markers', name=col))
                elif plot_type_trade == 'Bar Plot':
                    trade_fig.add_trace(go.Bar(x=filtered_trade_df.index, y=filtered_trade_df[col], name=col))

            trade_fig.update_layout(
                title="Debt Plot",
                xaxis_title="Years",
                yaxis_title="Values",
                legend_title="Legend",
                hovermode='x unified',  # Show hover information for all traces
            )

            st.plotly_chart(trade_fig)
        return


    elif page_name == 'Internet and Electricity':
        st.header('Internet and Electricity')
        options = ['Individuals using the Internet (% of population)','People using at least basic drinking water services (% of population)', 'Access to electricity (% of population)', 'Electricity production from oil, gas and coal sources (% of total)']
        selected_options = st.multiselect('Select Data', options)
        plot_type = st.selectbox('Select Plot Type', ['Line Plot', 'Bar Plot'])

        start_year = st.slider('Select Start Year', min_value=original_start_year, max_value=original_end_year,
                               value=original_start_year, step=1)
        end_year = st.slider('Select End Year', min_value=original_start_year, max_value=original_end_year,
                             value=original_end_year, step=1)

        filtered_df = filter_data(df, selected_options, start_year, end_year)

        # Plot
        fig = go.Figure()

        if plot_type == 'Line Plot':
            for col in selected_options:
                fig.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df[col], mode='lines+markers', name=col))
        elif plot_type == 'Bar Plot':
            for col in selected_options:
                fig.add_trace(go.Bar(x=filtered_df.index, y=filtered_df[col], name=col))

        fig.update_layout(
            title="Internet and Electricity Plot",
            xaxis_title="Years",
            yaxis_title="Values",
            legend_title="Legend",
            hovermode='x unified',  # Show hover information for all traces
        )

        st.plotly_chart(fig)

        st.header('Unemployment')
        selected_loan_options = st.multiselect('Select Data',
                                               [
                                                'Unemployment, total (% of total labor force)'])
        plot_type_trade = st.selectbox('Select Plot Type ', ['Line Plot', 'Bar Plot'], key='loan_plot_type')

        start_year_trade = st.slider('Select Start Year ', min_value=original_start_year,
                                     max_value=original_end_year,
                                     value=original_start_year, step=1, key='loan_start_year')
        end_year_trade = st.slider('Select End Year ', min_value=original_start_year,
                                   max_value=original_end_year,
                                   value=original_end_year, step=1, key='loan_end_year')

        if selected_loan_options:
            filtered_trade_df = filter_data(df, selected_loan_options, start_year_trade, end_year_trade)
            trade_fig = go.Figure()
            for col in selected_loan_options:
                if plot_type_trade == 'Line Plot':
                    trade_fig.add_trace(go.Scatter(x=filtered_trade_df.index, y=filtered_trade_df[col],
                                                   mode='lines+markers', name=col))
                elif plot_type_trade == 'Bar Plot':
                    trade_fig.add_trace(go.Bar(x=filtered_trade_df.index, y=filtered_trade_df[col], name=col))

            trade_fig.update_layout(
                title="Unemployment Plot",
                xaxis_title="Years",
                yaxis_title="Values",
                legend_title="Legend",
                hovermode='x unified',  # Show hover information for all traces
            )

            st.plotly_chart(trade_fig)

        return

    elif page_name == 'Resources':
        st.header('Agriculture and Industry')
        options = ['Agriculture, forestry, and fishing, value added (% of GDP)',
                   'Industry, value added (% of GDP)']
        selected_options = st.multiselect('Select Data', options)
        plot_type = st.selectbox('Select Plot Type', ['Line Plot', 'Bar Plot'])

        start_year = st.slider('Select Start Year', min_value=original_start_year, max_value=original_end_year,
                               value=original_start_year, step=1)
        end_year = st.slider('Select End Year', min_value=original_start_year, max_value=original_end_year,
                             value=original_end_year, step=1)

        filtered_df = filter_data(df, selected_options, start_year, end_year)

        # Plot
        fig = go.Figure()

        if plot_type == 'Line Plot':
            for col in selected_options:
                fig.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df[col], mode='lines+markers', name=col))
        elif plot_type == 'Bar Plot':
            for col in selected_options:
                fig.add_trace(go.Bar(x=filtered_df.index, y=filtered_df[col], name=col))

        fig.update_layout(
            title="Agriculture and Industry Plot",
            xaxis_title="Years",
            yaxis_title="Values",
            legend_title="Legend",
            hovermode='x unified',  # Show hover information for all traces
        )

        st.plotly_chart(fig)

        st.header('Land')
        selected_trade_options = st.multiselect('Select Data',
                                                [
                                                    'Forest area (% of land area)',
                                                    'Agricultural land (% of land area)'])
        plot_type_trade = st.selectbox('Select Plot Type ', ['Line Plot', 'Bar Plot'],
                                       key='trade_plot_type')

        start_year_trade = st.slider('Select Start Year ', min_value=original_start_year,
                                     max_value=original_end_year,
                                     value=original_start_year, step=1, key='trade_start_year')
        end_year_trade = st.slider('Select End Year ', min_value=original_start_year,
                                   max_value=original_end_year,
                                   value=original_end_year, step=1, key='trade_end_year')

        if selected_trade_options:
            filtered_trade_df = filter_data(df, selected_trade_options, start_year_trade, end_year_trade)
            trade_fig = go.Figure()
            for col in selected_trade_options:
                if plot_type_trade == 'Line Plot':
                    trade_fig.add_trace(go.Scatter(x=filtered_trade_df.index, y=filtered_trade_df[col],
                                                   mode='lines+markers', name=col))
                elif plot_type_trade == 'Bar Plot':
                    trade_fig.add_trace(go.Bar(x=filtered_trade_df.index, y=filtered_trade_df[col], name=col))

            trade_fig.update_layout(
                title="Land Plot",
                xaxis_title="Years",
                yaxis_title="Values",
                legend_title="Legend",
                hovermode='x unified',  # Show hover information for all traces
            )

            st.plotly_chart(trade_fig)

        return

    else:
        st.write("Invalid Page")
        return

# Sidebar navigation
st.sidebar.title('Next Page')
page = st.sidebar.radio('Go to:', ['Population', 'GDP Growth', 'Government Expenditure', 'Tax and Debt', 'Internet and Electricity', 'Resources'])

# Render selected page
render_page(page)
