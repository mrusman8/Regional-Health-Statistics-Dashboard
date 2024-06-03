from utility_functions import *

st.set_page_config(
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded")
st.title('Regional General Health Statistics')
selected_cols = ['Pakistan']

datasets = {'population_stats': {'Population Size in Thousands': 'total_pop.csv',
                                 'Urban Population by Percentage': 'urban_pop.csv',
                                 'Population Growth Percentage': 'pop_growth.csv',
                                 'Life Expectancy at birth': 'life_exp.csv',
                                 'Fertility Rate': 'fertility_rate.csv'},
            'childbirth_stats': {'Low Birth weight': 'LBW.csv',
                                 'Under 5 who are stunted': 'under_5_stunted.csv',
                                 'Under 5 who are wasted': 'under_5_wasted.csv',
                                 'Under 5 who are overweight': 'under_5_overweight.csv',
                                 'Under 5 who are obese': 'under_5_obese.csv'},
            'general risk factors': {'Tobacco use (13-15 years)': 'tobacco_use(13-15yr) .csv',
                                     'Tobacco use (15+ years)': 'tobacco use 15yr plus.csv',
                                     'Insufficient physical activity (13-18 years)': 'Insufficient physical activity ('
                                                                                     '13-18 years).csv',
                                     'Insufficient physical activity (18+ years)': 'Insufficient physical activity (18+ '
                                                                                   'years).csv',
                                     'Mortality rate due to traffic injuries-per 100000 population':'Mortality due to '
                                                                                                    'traffic injuries-per 100000.csv'},
            'health workforce & expenditure':
                {'Current Health Expenditure (CHE) per Capita in US$': '(CHE) per Capita in US$.csv',
                 'Personnel per 10000 population-Physicians': 'Personnel per 10 000 population-Physicians.csv',
                 'Personnel per 10000 population-Nursing and midwifery':
                     'Personnel per 10 000 population-Nursing and midwifery.csv',
                 'Personnel per 10000 population-Dentists.csv': 'Personnel per 10 000 population-Dentists.csv',
                 'Personnel per 10000 population-Pharmacists': 'Personnel per 10 000 population-Pharmacists.csv'
                 },
            'medical graduates density':{
                'Physician Graduates per 100000 population':'Physician Graduates per 100 000 population.csv',
                'Nursing and midwifery Graduates per 100 000 population':'Nursing and midwifery Graduates per 100 000 population.csv',
                'Dentist Graduates per 100000 population':'Dentist Graduates per 100 000 population.csv',
                'Pharmacists Graduates per 100 000 population':'Pharmacists Graduates per 100 000 population.csv'
            }

            }


def population():
    st.header('Population')
    driver_function(datasets['population_stats'], selected)


def child_birth():
    st.header('Child Birth Statistics')
    driver_function(datasets['childbirth_stats'], selected)

def risk_factors():
    st.header('General Risk Factors')
    driver_function(datasets['general risk factors'], selected)


def workforce():
    st.header('Workforce & Expenditure')
    driver_function(datasets['health workforce & expenditure'], selected)


def medical_graduates():
    st.header('Child Birth Statistics')
    driver_function(datasets['medical graduates density'], selected)


# Sidebar navigation
st.sidebar.title('Next Page')
selected = st.sidebar.multiselect('Select Data',
                                  ['Pakistan', 'Afghanistan', 'Bahrain', 'Djibouti', 'Egypt', 'Iran',
                                   'Iraq', 'Jordan', 'Kuwait', 'Lebanon', 'Libya', 'Morocco',
                                   'Occupied Palestinian territory', 'Oman', 'Qatar', 'Saudi Arabia', 'Somalia',
                                   'Sudan', 'Syrian Arab Republic', 'Tunisia', 'United Arab Emirates', 'Yemen'],

                                  default=['Pakistan', 'Afghanistan', 'Iran', 'Qatar', 'Saudi Arabia',
                                           'United Arab Emirates'])


page = st.sidebar.radio('Go to:', ['Population', 'Child Birth Stats', 'General Risk Factors',
                                   'Workforce & Expenditure', 'Medical Graduates'])

if page == 'Population':
    population()
elif page == 'Child Birth Stats':
    child_birth()
elif page == 'General Risk Factors':
    risk_factors()
elif page == 'Workforce & Expenditure':
    workforce()
elif page == 'Medical Graduates':
    medical_graduates()
