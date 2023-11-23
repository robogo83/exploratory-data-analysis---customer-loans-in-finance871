# Loan Payments EDA Project

This project demonstrates how to extract and save a dataset from AWS database and load it as pandas dataframe for Exploratary Data Analysis.
The dataset is extracted using RDSDatabaseConnector class in db_utils.py using secret credentials. The dataset is part of the repository and can be used for further manipulation and exploratory data analysis (EDA).

## Instalation Instruction

To run the project locally you can clone the project using git. Copy and paste the following command, making sure you navigate to a desired place in your computer where you want to clone the project.

```
git clone https://github.com/robogo83/exploratory-data-analysis---customer-loans-in-finance871.git
```

## Usage Instruction

Once you clone the project, open it in your prefered IDE, i.e. VS Code, PyCharm etc.

There's no need to run the db_utils.py file since AWS credentials are needed. The db_utils.py file only demonstrates how 
the download of the dataset has been executed. The loan_payments.csv dataset has been downloaded and is available in this repository.

## Project Structure

Apart from the db_utils.py the project consists of the following two python scripts:

1. **data_info.py** - This is a module that consists of the classes that provide the user with an option to get the pandas dataframe info, transform the dataframe columns and plot the dataframe. This file demonstrates ability to create classes with methods to make the code clearer. 
2. **eda.ipynb** - This is the main file using jupyter notebook. Using jupyter notebook helps to use markdowns for explaining the approach of the EDA steps and it also provides the outputs without necessity to run python file scripts in the console. More information about how to restart kernels and run the code in jupyter notebook can be found [here](https://docs.jupyter.org/en/latest/).

## License

This is an open-source repository available to download and manipulate. It demonstrates my ability to use python as a programing language with its data analysis libraries for EDA. 
The libraries used in the repository are open-source libraries:
- [Pandas](https://pandas.pydata.org)
- [Matplotlib](https://matplotlib.org)
- [SciPy](https://scipy.org)
- [statsmodels](https://www.statsmodels.org/stable/index.html)
- [missingno](https://github.com/ResidentMario/missingno)

