import streamlit as st
from offense_calculator import get_all_offensive_multipliers
from defense_calculator import defense_calculator

st.title("Pokemon Showdown Battle Assistant")
st.write("Analyze type matchups for strategic Pokemon battles!")

# Input for types
col1, col2 = st.columns(2)
with col1:
    type1 = st.selectbox("Opponent's First Type", [""] + ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"])
with col2:
    type2 = st.selectbox("Opponent's Second Type (optional)", ["none"] + ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"])

if st.button("Analyze"):
    if type1 == "":
        st.error("Please select the first type.")
    else:
        # Get data
        offensive_mults = get_all_offensive_multipliers(type1, type2)
        defensive_mults = defense_calculator(type1, type2)
        
        # Prepare tables
        def create_table(mults_dict, title):
            grouped = {}
            for t, mult in mults_dict.items():
                if mult not in grouped:
                    grouped[mult] = []
                grouped[mult].append(t)
            table_data = []
            for mult in sorted(grouped.keys(), reverse=True):
                if mult != 1:
                    types_str = ", ".join(grouped[mult])
                    table_data.append([f"{mult}x", types_str])
            return table_data
        
        offensive_table = create_table(offensive_mults, "Offensive")
        defensive_table = create_table(defensive_mults, "Defensive")
        
        # Display
        st.subheader("Defensive Analysis")
        st.write("Damage multipliers the opponent takes:")
        st.table(defensive_table)
        
        st.subheader("Offensive Analysis")
        st.write("Damage multipliers the opponent deals:")
        st.table(offensive_table)
