import yaml
from sqlalchemy import create_engine
import pandas as pd


class RDSDatabaseConnector:

    def __init__(self):
        self.credentials = self.load_credentials()

    def load_credentials(self):
        """
        Method that reads yaml file and returns python dictionary.
        It takes the yaml file as an argument.
        """
        with open('./credentials.yaml', 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials

    def db_engine(self):
        engine = create_engine(
            f"postgresql+psycopg2://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}")
        return engine

    def extract_data(self):
        sql = "select * from loan_payments"
        df = pd.read_sql(sql, con=self.db_engine())
        print('Data Extracted')
        return df

    def save_data(self):
        df = self.extract_data()
        print('Data Saved')
        return df.to_csv('./loan_payments.csv')


if __name__ == '__main__':
    data = RDSDatabaseConnector()
    data.save_data()
