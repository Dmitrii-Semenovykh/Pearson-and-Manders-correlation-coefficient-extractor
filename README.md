# Automated Extraction of Colocalization Coefficients

The aim of this script is to extract fluorescence colocalization measurements (Pearson's correlation coefficient and Manders' colocalization coefficients) from multiple text files and compile the results into a single Excel spreadsheet.

### Features

- **Batch processing:** Reads all “.txt” files from a specified directory.
- **Automated data extraction:** Uses regular expressions to identify and extract Pearson's coefficient and Manders' M1/M2 values.
- **Threshold comparison:** Separately retrieves original and thresholded Manders' coefficients.
- **Data organization:** Combines measurements from individual files into a structured Pandas DataFrame.
- **Excel export:** Saves all extracted measurements into a single “.xlsx” file.
- **Basic error checking:** A  warning is raised when one or more expected values cannot be found in a source file.

### Output structure

The resulting Excel spreadsheet contains the following columns:

| Column | Description |
|---|---|
| File | Original text filename |
| Pearson | Pearson's correlation coefficient |
| M1_original | Original Manders' M1 coefficient |
| M2_original | Original Manders' M2 coefficient |
| M1_threshold | Thresholded Manders' M1 coefficient |
| M2_threshold | Thresholded Manders' M2 coefficient |

### Requirements

- Python 3
- pandas
- openpyxl (for Excel export)


### Usage

1. Set “FOLDER” to your directory containing the microscopy analysis “.txt” files.
2. Run the Python script.
3. The script processes all matching files and creates “coefficients.xlsx” in the same directory.
4. Check the terminal output for warnings about missing measurements.


### Application

Designed for batch processing of fluorescence colocalization analysis results. It reduces repetitive manual data collection and provides a consistent format for subsequent statistical analysis and visualization.
