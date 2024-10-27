import streamlit as st
import pandas as pd

# Streamlit app title and description
st.title("LC/HRMS Web App")
st.write("Upload your LC-HRMS data and configure your analysis settings.")

# Upload file section
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv", "xlsx"])

# Display sample data if uploaded
if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(data.head())
    except Exception as e:
        st.error("Error loading file. Please check the format.")
        st.write(e)

# Analysis settings section
st.header("Analysis Settings")

# pH input
ph_value = st.number_input("pH", min_value=0.0, max_value=14.0, value=2.7, step=0.1)

# Solvents input
st.subheader("Solvents")
solvent_a = st.selectbox("Solvent A", ["Formic acid", "Water", "Methanol"])
solvent_b = st.selectbox("Solvent B", ["Acetonitrile", "Methanol", "None"])

# Gradient program section
st.subheader("Gradient Program")
gradient_data = []

# Add a new row for gradient
with st.form("gradient_form"):
    t_min = st.number_input("Time (min)", min_value=0.0, step=0.1, key="time")
    solvent_a_percent = st.number_input("Solvent A %", min_value=0.0, max_value=100.0, step=0.1, key="solvent_a")
    solvent_b_percent = st.number_input("Solvent B %", min_value=0.0, max_value=100.0, step=0.1, key="solvent_b")
    add_row_button = st.form_submit_button("Add Row")

    # Add row to gradient data if 'Add Row' is clicked
    if add_row_button:
        gradient_data.append({"Time (min)": t_min, "Solvent A %": solvent_a_percent, "Solvent B %": solvent_b_percent})
        st.write("Gradient Program Updated")

# Ensure gradient_df is defined even if there are no rows
if gradient_data:
    gradient_df = pd.DataFrame(gradient_data)
else:
    gradient_df = pd.DataFrame(columns=["Time (min)", "Solvent A %", "Solvent B %"])

# Display gradient program table
st.write("Gradient Program:")
st.dataframe(gradient_df)

# Submit button for final query
if st.button("Submit Query"):
    st.success("Query submitted with the following settings:")
    st.write("pH:", ph_value)
    st.write("Solvent A:", solvent_a)
    st.write("Solvent B:", solvent_b)
    st.write("Gradient Program:")
    st.dataframe(gradient_df)

# Download template CSV file
st.markdown("### Download Sample CSV File")
st.write("You can use this sample file as a template for your input.")
st.markdown("[Download Sample CSV](https://example.com/sample.csv)")

# Optional: Link to user manual
st.markdown("For detailed guidance, refer to the [Quantem User Manual](https://app.quantem.co/user_manual).")
