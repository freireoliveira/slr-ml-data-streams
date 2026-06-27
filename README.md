# Supplementary Material: A Systematic Literature Review on Multi-label Data Stream Classification

This repository contains the supplementary dataset, quality assessment scores, and exploratory analysis scripts for the systematic literature review (SLR) titled **"A Systematic Literature Review on Multi-label Data Stream Classification"**. 

## 📂 Repository Structure

The repository consists of the following core files:

*   **`data_extraction.xls`**: The comprehensive data extraction sheet. It contains the raw and categorized data extracted from the 61 primary studies selected for the review.
*   **`quality_assessment.xlsx`**: The selection process. It details the Quality Assessment (QA) scores for the 65 papers evaluated during the final full-text reading phase, explicitly showing the criteria used to approve the final 61 studies.
*   **`exploratory_analysis.py`**: The Python script used to parse the extraction sheet, clean the data, and generate the visualizations presented in the manuscript. 

## 🚀 How to Run the Analysis

If you wish to reproduce the figures and exploratory data analysis from the paper, you can run the provided Python script.

### Prerequisites
The script requires Python 3.x and the following libraries:
* `pandas`
* `matplotlib`
* `seaborn`

### Execution
Run the script in your terminal or preferred IDE ensuring that the Excel files are located in the same directory:

```bash
python exploratory_analysis.py
```

Note: The script will automatically generate and save high-resolution .png files of the charts in the root directory.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
