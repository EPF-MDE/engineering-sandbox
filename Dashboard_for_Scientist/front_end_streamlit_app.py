import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Dashboard for Scientist")
CSV_data = st.file_uploader("Upload CSV File", type=["csv"])
if CSV_data is None:
    st.info("Please upload a CSV file to continue.")
    st.stop()

Diabetes_df = pd.read_csv(CSV_data)
st.dataframe(Diabetes_df.head())
print(f"Number of Rows: \n{Diabetes_df.shape[0]}")
st.text("Number of Rows:")
st.write(Diabetes_df.shape[0])
st.text("Number of Columns")
st.write(Diabetes_df.shape[1])
st.text("Overall Shape")
st.write(Diabetes_df.shape)
st.text("All Coloumns and their Data Types : ")
st.dataframe(Diabetes_df.dtypes)
st.text("Total NUll Values: ")
st.write(Diabetes_df.isnull().sum().sum())
st.text("Column Wise Null Values Are: ")
st.dataframe(Diabetes_df.isnull().sum())
st.text("Basic Statistics for Numerical Colums: ")
st.dataframe(Diabetes_df.describe())

st.text("Box Plot for Outlier Detection: Enter Column Name")

column_for_outlier_detection = st.text_input("Enter column name")

if column_for_outlier_detection:  # only runs if not empty
    if column_for_outlier_detection in Diabetes_df.columns:
        fig, ax = plt.subplots()
        sns.boxenplot(Diabetes_df[column_for_outlier_detection])
        st.pyplot(fig)
    else:
        st.warning("❌ Column not found. Please enter a valid column name.")
else:
    st.info("👆 Please enter a column name to generate the boxplot.")
st.text("Correlations on Your dataset: ")
st.dataframe(Diabetes_df.corr())
fig2, ax = plt.subplots()
sns.heatmap(Diabetes_df.corr(), cmap="YlGnBu", annot=True)
st.pyplot(fig2)
st.text("Historgam for Distribtution: Enter Column Name")
histogram_Column = st.text_input("Enter Column Name for Histogram Visualization")
if histogram_Column:  # only runs if not empty
    if histogram_Column in Diabetes_df.columns:
        fig3, ax = plt.subplots()
        hist = Diabetes_df[histogram_Column].hist(bins=8)
        st.pyplot(fig3)
    else:
        st.warning("❌ Column not found. Please enter a valid column name.")
else:
    st.info("👆 Please enter a column name to generate the Histogram.")
