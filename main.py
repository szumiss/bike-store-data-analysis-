import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_file = 'Sales.csv'
df = pd.read_csv(csv_file)

numeric_columns = df.select_dtypes(include=['number'])
corr_matrix = numeric_columns.corr()


def Heatmap():
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.show()

def AgeToProfit():
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Customer_Age', y='Profit', data=df)
    plt.title('Age vs. Profit')
    plt.xlabel('Customer Age')
    plt.ylabel('Profit')
    plt.show()

def GenderToAgeToProfit3D():
    df['Gender_Num'] = df['Customer_Gender'].map({'M': 1, 'F': 0})

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    gender = df['Gender_Num']
    age = df['Customer_Age']
    profit = df['Profit']

    scatter = ax.scatter(age, gender, profit, c=profit, cmap='coolwarm', s=20)

    ax.set_xlabel('Customer Age')
    ax.set_ylabel('Gender')
    ax.set_zlabel('Profit')
    ax.set_title('Correlation between Gender, Age, and Profit')

    color_bar = plt.colorbar(scatter)
    color_bar.set_label('Profit')
    plt.show()

def NumberOfSalesToCostOfItem():
    ax = df['Unit_Cost'].plot(kind='hist', figsize=(14, 6))
    ax.set_ylabel('Number of Sales')
    ax.set_xlabel('Item price')
    plt.show()

def AgeToNumberOfSales():
    ax = df['Age_Group'].value_counts().plot(kind='bar', figsize=(14, 6))
    ax.set_ylabel('Number of Sales')
    plt.show()

def CategoryToGender():
    plt.figure(figsize=(12, 8))
    df_grouped = df.groupby(['Product_Category', 'Customer_Gender'])['Revenue'].sum().unstack()
    df_grouped.plot(kind='bar', width=0.4)
    plt.title('Sum of Revenue by Product Category and Customer Gender')
    plt.xlabel('Product Category')
    plt.ylabel('Total Revenue')
    plt.legend(title='Customer Gender', loc='upper right', labels=['Female', 'Male'])
    plt.show()

def TotalMoneySpentPerGender():
    plt.figure(figsize=(8, 6))
    df_gender_spending = df.groupby('Customer_Gender')['Revenue'].sum()
    df_gender_spending.plot(kind='bar', color=['blue', 'green'])
    plt.title('Total Money Spent by Gender')
    plt.xlabel('Customer Gender')
    plt.ylabel('Total Money Spent')
    plt.show()

def CategoriesPerCountryBarChart():
    plt.figure(figsize=(12, 8))
    category_country_counts = df.groupby(['Country', 'Product_Category'])['Product'].count().unstack()
    category_country_counts.plot(kind='bar', width=0.8)
    plt.title('Product Categories per Country')
    plt.xlabel('Country')
    plt.ylabel('Count of Product Categories')
    plt.legend(title='Product Category', loc='upper right')
    plt.show()

def ProfitsForTop15ProductsBarChart():
    plt.figure(figsize=(12, 8))
    top_15_products = df['Product'].value_counts().nlargest(15).index
    filtered_df = df[df['Product'].isin(top_15_products)]

    product_profits = filtered_df.groupby('Product')['Profit'].sum()
    product_profits.sort_values(ascending=False).plot(kind='bar', color='skyblue')

    plt.title('Profits for Top 15 Best-Selling Products')
    plt.xlabel('Product')
    plt.ylabel('Total Profit')
    plt.xticks(rotation=45, ha='right')
    plt.show()

def SalesPerCountryPieChart():
    plt.figure(figsize=(10, 10))
    country_sales = df.groupby('Country')['Revenue'].sum()
    plt.pie(country_sales, labels=country_sales.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Sales Distribution per Country')
    plt.show()

def SalesPerCategoryPerAgeGroupBarChart():
    plt.figure(figsize=(12, 8))
    category_age_sales = df.groupby(['Product_Category', 'Age_Group'])['Revenue'].sum().unstack()
    category_age_sales_in_millions = category_age_sales / 1000000

    category_age_sales_in_millions.plot(kind='bar', width=0.8)

    plt.title('Sales per Product Category per Age Group (in Millions)')
    plt.xlabel('Product Category')
    plt.ylabel('Total Sales (Millions)')
    plt.legend(title='Age Group', loc='upper right')
    plt.show()

Heatmap()
AgeToProfit()
GenderToAgeToProfit3D()
NumberOfSalesToCostOfItem()
AgeToNumberOfSales()
CategoryToGender()
TotalMoneySpentPerGender()
CategoriesPerCountryBarChart()
ProfitsForTop15ProductsBarChart()
SalesPerCountryPieChart()
SalesPerCategoryPerAgeGroupBarChart()
