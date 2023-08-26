from bs4 import BeautifulSoup
import requests
import streamlit as st

def main():
    st.title("Premier League Table")

    url = "https://www.premierleague.com/tables"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        team_name_elements = soup.find_all("span", class_="long")
        team_names = [element.get_text(strip=True) for element in team_name_elements[:20]]
        
        team_table = "\n".join([f"{idx}. {team_name}" for idx, team_name in enumerate(team_names, start=1)])
    else:
        print("Failed to fetch the webpage.")

    
    
    team_list = st.text_area("Team List", team_table, height=500)

if __name__ == '__main__':
    main()
