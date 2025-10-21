# A farmer records rainfall in mm for 6 months, he wants to see how rainfall changes month to month using a line chart. Plot the data and clearly mark which month had the maximum rainfall
# A student wants to understand how his day is spent, plot a pie chart of hours spent and show percentage with one decimal 
# A retailer wants to compare quarerly sales of product A vs product B, plot a grouped bar chart with labels on top of bars
# A small shop records 500 transaction amounts, plot a histogram chart to see the typical spent and mark the mean with a vertical line
# A teacher wants to see if hours studied affects exam marks for 8 students, plot a scatter chart showing hours studied vs marks obtained

import matplotlib.pyplot as plt
import numpy as np

def one():
    # Sample rainfall data (in mm) for 6 months
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    rainfall = [120, 85, 95, 150, 110, 75]
    
    # Create the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(months, rainfall, marker='o', linewidth=2, markersize=8, color='blue')
    
    # Find and mark the maximum rainfall
    max_rainfall = max(rainfall)
    max_month_index = rainfall.index(max_rainfall)
    max_month = months[max_month_index]
    
    # Highlight the maximum point
    plt.plot(max_month, max_rainfall, marker='*', markersize=20, 
             color='red', linestyle='None', label=f'Max: {max_rainfall}mm in {max_month}')
    
    # Add labels and title
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Rainfall (mm)', fontsize=12)
    plt.title('Monthly Rainfall Data', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def two():
    # Sample data for student's daily activities
    activities = ['Sleeping', 'Studying', 'Entertainment', 'Meals', 'Exercise', 'Others']
    hours = [8, 6, 3, 2, 1.5, 3.5]
    
    # Create the pie chart
    plt.figure(figsize=(10, 8))
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc', '#c2c2f0']
    
    plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=90,
            colors=colors)
    
    plt.title("Student's Daily Time Distribution (24 Hours)", 
              fontsize=14, fontweight='bold')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.tight_layout()
    plt.show()

def three():
    # Sample quarterly sales data
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    product_a_sales = [15000, 18000, 22000, 19000]
    product_b_sales = [12000, 16000, 20000, 23000]
    
    # Create the grouped bar chart
    plt.figure(figsize=(10, 6))
    
    # Set the width of bars and positions
    bar_width = 0.35
    x_positions = np.arange(len(quarters))
    
    # Create bars for both products
    bars1 = plt.bar(x_positions - bar_width/2, product_a_sales, bar_width, 
                    label='Product A', color='skyblue', edgecolor='black')
    bars2 = plt.bar(x_positions + bar_width/2, product_b_sales, bar_width, 
                    label='Product B', color='salmon', edgecolor='black')
    
    # Add value labels on top of each bar
    for bar in bars1:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height,
                f'₹{height:,.0f}', ha='center', va='bottom', fontsize=10)
    
    for bar in bars2:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height,
                f'₹{height:,.0f}', ha='center', va='bottom', fontsize=10)
    
    # Add labels and formatting
    plt.xlabel('Quarter', fontsize=12)
    plt.ylabel('Sales (₹)', fontsize=12)
    plt.title('Quarterly Sales Comparison: Product A vs Product B', 
              fontsize=14, fontweight='bold')
    plt.xticks(x_positions, quarters)
    plt.legend()
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()

def four():
    # Generate sample transaction data (500 transactions)
    # Using normal distribution with mean=50 and std=15
    np.random.seed(42)  # For reproducibility
    transactions = np.random.normal(loc=50, scale=15, size=500)
    transactions = np.clip(transactions, 10, 100)  # Keep values between 10-100
    
    # Calculate mean
    mean_transaction = np.mean(transactions)
    
    # Create histogram
    plt.figure(figsize=(10, 6))
    
    # Plot histogram
    plt.hist(transactions, bins=20, color='lightgreen', 
             edgecolor='black', alpha=0.7)
    
    # Add vertical line for mean
    plt.axvline(mean_transaction, color='red', linestyle='--', linewidth=2,
                label=f'Mean: ₹{mean_transaction:.2f}')
    
    # Add labels and formatting
    plt.xlabel('Transaction Amount (₹)', fontsize=12)
    plt.ylabel('Frequency (Number of Transactions)', fontsize=12)
    plt.title('Distribution of Transaction Amounts (500 Transactions)', 
              fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()

def five():
    # Sample data for 8 students
    hours_studied = [2, 3, 4, 5, 6, 7, 8, 9]
    exam_marks = [45, 55, 60, 68, 75, 82, 88, 92]
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    
    # Plot scatter points
    plt.scatter(hours_studied, exam_marks, s=100, color='purple', 
                alpha=0.6, edgecolors='black', linewidth=1.5)
    
    # Add a trend line (optional but helpful to see correlation)
    z = np.polyfit(hours_studied, exam_marks, 1)
    p = np.poly1d(z)
    plt.plot(hours_studied, p(hours_studied), color='red', 
             linestyle='--', linewidth=2, label='Trend Line')
    
    # Add labels and formatting
    plt.xlabel('Hours Studied', fontsize=12)
    plt.ylabel('Exam Marks (%)', fontsize=12)
    plt.title('Relationship Between Study Hours and Exam Performance', 
              fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xlim(1, 10)
    plt.ylim(40, 100)
    plt.tight_layout()
    plt.show()

