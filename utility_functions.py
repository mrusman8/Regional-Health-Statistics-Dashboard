import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def data_preprocess(df):
    df = df.T
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    df.reset_index(drop=True, inplace=True)
    df.rename(columns={'Country': 'Year','Iran, Islamic Republic of':'Iran'}, inplace=True)
    df['Year'].iloc[0] = '2023'
    df.fillna(method='bfill', inplace=True)
    obj_cols = df.select_dtypes(exclude=['int64', 'float64'])
    for col in obj_cols.columns:
        if ',' in df[col].values.any():
            df[col] = df[col].str.replace(',','').astype(float)
        else:
            df[col] = df[col].astype(float)
    df.to_csv('data.csv', index=False)
    return df


def year_wise_plot(df,selected_cols,start_year,end_year, plot_type,plot_data):
    start_value = st.slider('Select Year Range', min_value=start_year, max_value=end_year,
                            value=(start_year, end_year), step=1)

    start_slider, end_slider = start_value  # Unpack the tuple into separate variables

    filtered_df = df[selected_cols][(df['Year'] >= start_slider) & (df['Year'] <= end_slider)]

    fig = go.Figure()

    if plot_type == 'Line Plot':
        for col in selected_cols:
            fig.add_trace(go.Scatter(x=df['Year'].unique(), y=filtered_df[col], mode='lines+markers', name=col))
    elif plot_type == 'Bar Plot':
        for col in selected_cols:
            fig.add_trace(go.Bar(x=df['Year'].unique(), y=filtered_df[col], name=col))

    fig.update_layout(
        title=plot_data, xaxis_title="Years", yaxis_title="Values",
        legend_title="Legend", bargap = 0.1, hovermode='x unified',  # Show hover information for all traces
    )
    st.plotly_chart(fig)


def recent_statistics(df,selected_cols, plot_type, plot_data, Year = 2023):
    #selected_cols = selected_cols.append('Year')
    filtered_df = df[selected_cols][df['Year'] == Year]

    fig = go.Figure()

    if plot_type == 'Line Plot':
        for col in selected_cols:
            print("cols = ",selected_cols)
            fig.add_trace(
                go.Scatter(x = [Year], y=filtered_df[col], mode='lines+markers', name=col))
    elif plot_type == 'Bar Plot':
        for col in selected_cols:
            fig.add_trace(go.Bar(x =[Year], y=filtered_df[col], name=col))


    fig.update_layout(
        title=plot_data, xaxis_title="Years", yaxis_title="Values",
        legend_title="Legend", bargap= 0.1, hovermode='x unified',  # Show hover information for all traces
    )
    st.plotly_chart(fig)


def driver_function(available_stats,selected):
    with st.container(border=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.container(border=True):
                plot_data = st.selectbox('Select Data',available_stats.keys())
        with col2:
            with st.container(border=True):
                plot_kind = st.selectbox('Select Data', ['Most Recent Statistics','Year Wise Statistics'])
        with col3:
            with st.container(border=True):
                plot_type = st.selectbox('Select Plot Type', ['Bar Plot','Line Plot'])

    # Read the data
    df = pd.read_csv(available_stats[plot_data])
    df_1 = data_preprocess(df)
    start_year = int(df_1['Year'].min())
    end_year = int(df_1['Year'].max())

    if plot_kind == 'Most Recent Statistics':
        recent_statistics(df_1,selected,plot_type, plot_data)
    else:
        year_wise_plot(df_1,selected,start_year,end_year,plot_type, plot_data)
