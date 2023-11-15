# Loan Payments EDA Project

This project demonstrates how to extract and save a dataset from AWS database and load it as pandas dataframe for Exploratary Data Analysis.

## Instalation Instruction

To run the project locally you can clone the project using git. Copy and paste the following command, making sure you navigate to a desired place in your computer where you want to clone the project.

```
git clone https://github.com/robogo83/exploratory-data-analysis---customer-loans-in-finance871.git
```
## Usage Instruction

Once you have the project clone open it in your prefered IDE, i.e. VS Code, PyCharm etc.

First run the db_utils.py file to extract and save the dataset in CSV format into your computer. You can run the file using the following command:
```
python -m db_utils
```
This will save loan_payments.csv file into your project folder.

***Note: Please be aware to successfully download the file, you need to have the AWS credentials of the database where the dataset is stored.***

After downloading the file you can head to the jupyter notebook *dataframe_func.ipynb* file where you can run the cells one by one.

