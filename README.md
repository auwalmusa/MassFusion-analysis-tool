# MassFusion: LC-HRMS Analysis Tool

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://massfusion-analysis-tool.streamlit.app/)

MassFusion is a web-based application designed to assist scientists and analysts in configuring and analyzing LC-HRMS (Liquid Chromatography-High Resolution Mass Spectrometry) data. This tool allows users to upload their experimental data, set key parameters like pH and solvents, and configure a gradient program for LC-MS analysis.

## Features

- **File Upload**: Supports uploading LC-HRMS data in CSV or Excel formats for easy viewing and analysis.
- **pH and Solvent Settings**: Lets users input pH and select solvents, ensuring proper analysis conditions.
- **Gradient Program Configuration**: Enables users to configure a time-dependent gradient program with multiple entries, affecting solvent composition over time.
- **Sample Data Download**: Provides a sample CSV file as a template for input format.
- **Direct Access to Quantem User Manual**: Links to the Quantem manual for detailed guidance on analysis settings and file formats.

## How to Use

1. **Upload Your Data**: Click on "Upload a CSV file" to upload your LC-HRMS data. The app supports both CSV and Excel file formats.
2. **Set Analysis Parameters**:
   - Input the desired **pH** value for your analysis.
   - Select **Solvent A** and **Solvent B** from the dropdown menus.
3. **Configure Gradient Program**:
   - Enter the time (in minutes) and percentage composition for Solvent A and Solvent B.
   - Click "Add Row" to add multiple entries to the gradient program.
4. **Submit the Query**: After configuring your settings, click "Submit Query" to finalize your setup. The app will display your settings for verification.
5. **Download Sample CSV**: If you need a template for formatting your input file, download the sample CSV provided in the app.

## Access the App

You can access the app here: [https://massfusion-analysis-tool.streamlit.app/](https://massfusion-analysis-tool.streamlit.app/)

## Sample Data

A sample LC-HRMS dataset for pesticides analysis is available in this repository under `pesticide_sample_data.csv` for testing purposes. You can upload this file to test the functionality of the app.

## Requirements

This app was built with:
- `streamlit`
- `pandas`

These dependencies are specified in `requirements.txt`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

