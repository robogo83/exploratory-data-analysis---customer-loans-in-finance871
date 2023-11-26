import pandas as pd
from scipy.stats import normaltest, yeojohnson
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
import missingno
from sklearn.preprocessing import LabelEncoder


class DataFrameInfo:
    '''
    Class for displaying basic statistical information about 
    A new object of the class needs to be initialised with a pandas dataframe.
    All methods provide basic statistial information about the pandas dataframe. If the pandas dataframe changes
    the object has to be initialised again with the updated pandas dataframe in order to provide updated 
    resuts of the methods.
    '''

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def describe(self):
        '''       
        Method that returns statistical information about the dataframe
        '''
        return self.dataframe.describe()

    def median(self, column_name=None):
        '''
        Method that returns median of a numeric column.
        If a column name is not provided, it returns median of the whole dataframe
        for all numeric columns.
        '''
        try:
            if column_name != None:
                print(self.dataframe[column_name].median(numeric_only=True))
            else:
                print(self.dataframe.median())
        except TypeError:
            print('The column has to be one of the numeric dtypes')

    def mean(self, column_name=None):
        '''
        Method that returns mean of a numeric column
        If a column name is not provided, it returns mean of the whole dataframe
        for all numeric columns.
        '''
        try:
            if column_name != None:
                print(self.dataframe[column_name].mean(numeric_only=True))
            else:
                print(self.dataframe.mean(numeric_only=True))
        except TypeError:
            print('The column has to be one of the numeric dtypes')

    def std(self, column_name=None):
        '''
        Method that returns standard deviation of a numeric column
        If a column name is not provided, it returns standard deviation of the whole dataframe
        for all numeric columns.
        '''
        try:
            if column_name != None:
                return self.dataframe[column_name].std(numeric_only=True)
            else:
                return self.dataframe.std(numeric_only=True)
        except TypeError:
            print('The column has to be one of the numeric dtypes')

    def distinct_categories_count(self, column_name):
        '''
        Method that returns count of distinct values of a categorical columns
        '''
        try:
            if self.dataframe[column_name].dtype == 'category':
                return self.dataframe[column_name].value_counts()
            else:
                print('The column is not a category dtype. Please convert first')
        except TypeError:
            print('The column is not a categorical column')

    def shape(self):
        '''
        Method that returns shape of the dataframe
        '''
        return self.dataframe.shape

    def null_values_count(self):
        '''
        Method that prints number and percentage of NaN values in the pandas dataframe
        '''
        for column in self.dataframe.columns:
            percentage = round((self.dataframe[column].isna().sum() /
                                len(self.dataframe[column])) * 100, 2)
            null_count = self.dataframe[column].isna().sum()
            print(f'{column}: {null_count} missing values, {percentage}%')

    def dagostino_test(self, column_name):
        '''
        Method to perform D'Agostino's K^2 test. The test provide the 
        probability that null hypothesis is false, given the data sample provided.
        The probability estimate - p-value close to 0 means data are normally distributed.
        '''
        data = self.dataframe[column_name]
        stat, p = normaltest(data, nan_policy='omit')
        print('Statistics = %.3f, p=%.3f' % (stat, p))

    def skewness(self):
        '''
        Method that prints skew value of the pandas dataframe
        '''
        print(self.dataframe.skew(numeric_only=False))


class DataFrameTransform():
    '''
    Class to transform the columns of a pandas dataframe to more.
    A new object of the class needs to be initialised with a pandas dataframe.
    Some of the methods can be used only with loan_payments.csv dataset transformed to a pandas dataframe.
    '''

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def term_column_type(self,  split_word, column_name='term',):
        '''
        Method that transform term variable in a loan_payment.csv into a numeric datatype.
        The method accepts the following arguments:
        column_name: name of the dataframe column. Because this method is specific to the loan_payment.csv
                    dataset, the default value is 'term'.
        split_word: at which word the string needs to be split, i.e. months
        '''
        # remove the right part of the value
        stripped_values = self.dataframe[column_name].astype(
            str).map(lambda x: x.rstrip(split_word))
        # cast it as an int64 type
        numeric_values = pd.to_numeric(
            stripped_values, errors='coerce')
        # assign the transformed column back to the DataFrame
        self.dataframe[column_name] = numeric_values
        return self.dataframe

    def column_to_categorical(self, column_name):
        '''
        Method that converts a pandas dataframe column into a categorical dtype
        and returns an updated dataframe.
        column_name: name of the column to be converted into category dtype.
        '''
        # cast the column as categorical type
        self.dataframe[column_name] = self.dataframe[column_name].astype(
            'category')
        return self.dataframe

    def object_to_datetime(self, column_name, date_format):
        '''
        Method that converts pandas object dtype into a pandas datetime dtype.
        column_name: name of the pandas dataframe column to be converted
        date_format: format of the datetime dtype that the column will be converted into
        '''
        # convert the column into a datetime dtype
        self.dataframe[column_name] = pd.to_datetime(
            self.dataframe[column_name], format=date_format)
        # # change the format of the column back to its original
        # # value and keep the column as datetime dtype
        # self.dataframe[column_name] = self.dataframe[column_name].dt.strftime(
        #     date_format)
        return self.dataframe

    def drop_columns(self, column_name):
        '''
        Method that drops a single or multiple columns
        column_name: either a single column of a pandas dataframe or a list of columns
        '''
        return self.dataframe.drop(column_name, axis=1, inplace=True)

    def data_impute(self, column_name, method):
        '''
        Method that takes in a method imputation as a string.
        column_name: column name of a pandas dataframe
        2 methods can be provided:
        mean
        median
        mode
        '''
        if method == 'mean':
            self.dataframe[column_name].fillna(
                self.dataframe[column_name].mean(), inplace=True)
        elif method == 'median':
            self.dataframe[column_name].fillna(
                self.dataframe[column_name].median(), inplace=True)
        elif method == 'mode':
            self.dataframe[column_name].fillna(
                self.dataframe[column_name].mode().iloc[0], inplace=True)
        else:
            print('Invalid imputation method.')
        return self.dataframe

    def yj_transform(self, column_name):
        '''
        Method to apply Yeo-Johnson method for solving positive skewness 
        '''
        yj_transform = self.dataframe[column_name]
        yj_transform = yeojohnson(yj_transform)
        yj_transform = pd.Series(yj_transform[0])
        self.dataframe[column_name] = yj_transform

    def encode_categorical_columns(self, columns):
        '''
        Method to transfrom categorical values into the numerical values. Using scikit-learn library and
        LabelEncoder method.
        '''
        le = LabelEncoder()

        for col in columns:
            if col in self.dataframe.columns:
                self.dataframe[col] = le.fit_transform(self.dataframe[col])


class Plotter():
    '''
    Class to provide basic visualisation plot methods for EDA.
    A new object of the class needs to be initialised with a pandas dataframe.
    If the pandas dataframe is updated the object has to be re-initialised to provide 
    plots with updated values.
    '''

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def histogram(self, column_name, bins):
        '''
        Histogram that takes two arguments.
        column_name: which is a column name of pandas dataframe
        bins: number of bins the histogram will show of the column
        '''
        plt.hist(self.dataframe[column_name], bins=bins)
        plt.show()

    def qq_plot(self, column_name):
        '''
        qq_plot to display values distribution of the colum.
        column_name: column name of pandas dataframe
        '''
        qq_plot = qqplot(self.dataframe[column_name], scale=1, line='q')
        plt.show()

    def missing_values_bar(self):
        '''
        Bar graph to visualise distribution of values in a dataframe
        '''
        missingno.bar(self.dataframe)

    def boxplot(self, column_name, number_of_var=0):
        '''
        Method for visualising box plot of a pandas dataframe
        If a list of columns is passed, number_of_var in the columns has to be passed 
        to display boxplots for all the var
        If only single column is passed as the argument a single boxplot is displayed.
        '''
        if number_of_var > 0:
            for i in range(number_of_var):
                self.dataframe.boxplot(column_name[i])
                plt.show()
        else:
            self.dataframe.boxplot(column_name)
