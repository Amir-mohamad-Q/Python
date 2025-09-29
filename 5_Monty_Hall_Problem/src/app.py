import streamlit as st
import time
from main import simulate_game


st.title('Monty Hall Problem')

num_games = st.number_input("Enter number of games to simulate",
                min_value=1,max_value=10000,
                value=100)

col1, col2 = st.columns(2)
col1.subheader("Win Percentage Without Switching")
col2.subheader("Win Percentage With Switching")

chart1 = col1.line_chart(x=None,y=None,height=400)
chart2 = col2.line_chart(x=None,y=None,height=400)

wins_no_switch = 0
wins_switch = 0
for i in range(num_games): 
    num_of_wins_without_switching, num_of_wins_with_switching = simulate_game(1)
    wins_no_switch += num_of_wins_without_switching
    wins_switch += num_of_wins_with_switching

    chart1.add_rows([wins_no_switch / (i + 1)])
    chart2.add_rows([wins_switch / (i + 1)])
    time.sleep(0.03)