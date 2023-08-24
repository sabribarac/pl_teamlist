from bs4 import BeautifulSoup
import requests
import streamlit as st

def main():
    st.title("Premier League Table")

    url = "https://www.bbc.com/sport/football/premier-league/table"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'html.parser')
    team_name_elements = soup.find_all('a', class_='ssrcss-13tfrt4-TeamName e1uquauq3')
    team_names = [element.get_text() for element in team_name_elements]

    team_table = "\n".join([f"{idx}. {team_name}" for idx, team_name in enumerate(team_names, start=1)])
    
    team_list = st.text_area("Team List", team_table, height=500)

if __name__ == '__main__':
    main()
