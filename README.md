# **Cryptocurrency Adoption Analysis: Does Cryptocurrency Have the Potential to Replace Cash?**

## **Project Overview**

This project explores the potential of **cryptocurrency** (BTC, ETH) to replace **traditional cash**. Specifically, it investigates whether the **availability of crypto ATMs** correlates with an **increase in wallet openings** for Bitcoin (BTC) and Ethereum (ETH).

### **Research Question:**
- Can cryptocurrencies, such as **Bitcoin** and **Ethereum**, replace traditional cash?
- Does an **increase in crypto ATM installations** correlate with **higher wallet openings**?

## **Project Goals**
- To analyze the correlation between **crypto ATMs** and the number of **wallet openings** for **BTC** and **ETH** over time.
- To explore the growth trends in **crypto adoption**.
- To visualize and quantify these correlations using **Python** and **data analysis techniques**.

## **Tools & Libraries Used**
- **Python**: For data analysis and visualization.
- **Pandas**: Data manipulation and cleaning.
- **Matplotlib / Seaborn**: Visualization of trends and relationships.
- **SciPy (Pearson Correlation)**: Statistical analysis to measure correlation between variables.
- **Statsmodels**: For any advanced statistical methods (optional, for future work).
- **Excel/CSV**: For initial data collection and cleansing.

## **Data Sources**
- **Cryptocurrency ATMs Data**: Data on the number of crypto ATMs installed across different regions.
- **Wallet Openings Data**: Data on the number of new wallet registrations for **Bitcoin (BTC)** and **Ethereum (ETH)** over time.

## **Data Cleaning and Preprocessing**
1. **Loading the Data**: Data was loaded into Python using `pandas`.
2. **Data Cleansing**: 
   - Removed irrelevant text (e.g., "K", "M") from numeric columns (e.g., ATMs, wallet numbers).
   - Converted columns to appropriate data types (e.g., numeric).
   - Checked for and handled missing values.
3. **Data Grouping**: The data was grouped by month to analyze trends over time.

## **Analysis & Results**
### **Exploratory Data Analysis (EDA)**  
- **Visualizing Trends**: Using **line plots** to display the growth in **crypto ATMs** and **wallet openings** over time.  
- **Correlation Analysis**: Calculated **Pearson correlation** between crypto ATMs and wallet openings for both BTC and ETH to determine if there is a significant relationship.
  - For example, a positive correlation suggests that **more ATMs correlate with more ETH wallet openings**, supporting the idea that **accessibility drives adoption**.

### **Key Findings**
- There is a **positive correlation** between the **number of crypto ATMs** and the **number of wallet openings** for both **BTC and ETH**.
- **Increasing accessibility to crypto ATMs** correlates with **higher adoption** rates for cryptocurrency wallets.
- While there is a relationship, external factors such as **market conditions, regulatory environment**, and **overall public perception** also play a crucial role in adoption.

## **Challenges & Limitations**
- **Correlation does not imply causation**: Just because the number of ATMs increases with wallet openings doesn’t mean one is directly causing the other.
- The dataset was somewhat **limited** to certain regions and could be improved by including more countries or more granular data.
- Further **seasonality adjustments** or **time-series models** could improve the forecasting and accuracy of predictions.

## **Future Work**
- **Advanced Modeling**: Explore **time-series forecasting models** such as **ARIMA** or **Prophet** to account for seasonality in the data.
- **Incorporating Other Variables**: Include other data sources like **market volatility** or **regulations** to improve prediction accuracy.
- **Geographical Data**: Analyze regional variations in the adoption of cryptocurrency and availability of ATMs.

## **How to Run This Project**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cryptocurrency-adoption.git
2. Install required libraries:
```bash
  pip install pandas matplotlib seaborn scipy statsmodels
3. Run the main analysis script:
```bash
  python crypto_adoption_analysis.py

File Structure
crypto_adoption_analysis.py: Main Python script for data analysis and visualization.
ETH_adjusted_2015.csv: Cleaned data file with historical crypto ATM and wallet opening data.
README.md: Project description and instructions (this file).
notebooks/: (Optional) Jupyter notebooks for more detailed analysis and exploration.
Contact
Erdal Beyoglu
GitHub: github.com/yourusername
LinkedIn: linkedin.com/in/erdalbeyoglu
