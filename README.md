# Risk-data-comparison-tool


This project is a Python-based tool designed to help analysts compare two datasets, identify discrepancies, and visualize differences using Seaborn and Matplotlib.

## Features
- Load two CSV datasets for comparison.
- Identify discrepancies based on a key column.
- Visualize the differences using bar plots.

## Requirements
To use this tool, install the required Python packages:

```bash
pip install pandas matplotlib seaborn
```

## Usage
1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/risk-data-comparison-tool.git
    ```

2. Navigate to the project directory:
    ```bash
    cd risk-data-comparison-tool
    ```

3. Run the script:
    ```bash
    python main.py
    ```

4. Enter the paths to your CSV files and the column name for comparison when prompted.

## Example
Given two datasets `data1.csv` and `data2.csv`:
```csv
data1.csv:
ID,Value
1,100
2,200
3,300

data2.csv:
ID,Value
2,200
3,350
4,400
```

Running the tool may output:
```
Differences between datasets:
   ID  Value_x  Value_y    _merge
0   1    100.0      NaN   left_only
1   3    300.0    350.0   both
2   4      NaN    400.0   right_only
```

## Visualization
The tool will generate a plot visualizing the differences between the datasets.

## Contributions
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

