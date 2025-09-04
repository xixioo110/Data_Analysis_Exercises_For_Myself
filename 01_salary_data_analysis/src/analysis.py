import pandas as pd

def load_data(file_path):
    """Load salary data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def analyze_salary_data(data):
    """Perform analysis on the salary data."""
    summary = {
        'mean_salary': data['salary'].mean(),
        'median_salary': data['salary'].median(),
        'max_salary': data['salary'].max(),
        'min_salary': data['salary'].min(),
        'salary_count': data['salary'].count()
    }
    return summary

def main():
    """Main function to execute the analysis."""
    file_path = '../data/salary_data.csv'
    salary_data = load_data(file_path)
    analysis_results = analyze_salary_data(salary_data)
    print(analysis_results)

if __name__ == "__main__":
    main()