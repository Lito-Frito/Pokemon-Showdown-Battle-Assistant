import streamlit as st
import pandas as pd
from offense_calculator import get_all_offensive_multipliers, get_opponent_offensive_mults
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
                    if mult >= 2:
                        label = "Super Effective"
                    elif mult < 1 and mult > 0:
                        label = "Not Very Effective"
                    elif mult == 0:
                        label = "Immune (No Damage)"
                    else:
                        label = f"{mult}x"
                    types_str = ", ".join(grouped[mult])
                    table_data.append([label, f"{mult}x", types_str])
            return table_data
        
        defensive_table = create_table(defensive_mults, "Defensive")
        
        # Display
        st.subheader("Defensive Analysis")
        st.write("Damage multipliers the opponent takes:")
        if defensive_table:
            df_def = pd.DataFrame(defensive_table, columns=["Effectiveness", "Multiplier", "Types"])
            st.dataframe(df_def, hide_index=True, use_container_width=True)
        else:
            st.write("No data available.")
        
        st.subheader("Offensive Analysis")
        st.write("Damage multipliers the opponent deals:")
        
        # Offensive for type1
        offensive_mults1 = get_opponent_offensive_mults(type1, "none")
        offensive_table1 = create_table(offensive_mults1, "Offensive")
        st.write(f"**{type1.capitalize()} moves:**")
        if offensive_table1:
            df_off1 = pd.DataFrame(offensive_table1, columns=["Effectiveness", "Multiplier", "Types"])
            st.dataframe(df_off1, hide_index=True, use_container_width=True)
        else:
            st.write("No data available.")
        
        # Offensive for type2 if present
        if type2 != "none":
            offensive_mults2 = get_opponent_offensive_mults(type2, "none")
            offensive_table2 = create_table(offensive_mults2, "Offensive")
            st.write(f"**{type2.capitalize()} moves:**")
            if offensive_table2:
                df_off2 = pd.DataFrame(offensive_table2, columns=["Effectiveness", "Multiplier", "Types"])
                st.dataframe(df_off2, hide_index=True, use_container_width=True)
            else:
                st.write("No data available.")
