import pymongo
import json
import pandas as pd

client = pymongo.MongoClient("mongodb+srv://matindra:mongodb123@cluster0.qej6jzl.mongodb.net/?retryWrites=true&w=majority")
db = client.test

DATA_FILE_PATH = "/home/lipu/Jupyter/insurance-premium-prediction-project/dataset/insurance.csv"
database_name = "INSURANCE"
collection_name = "INSURANCE_PROJECT"


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Columns and Rows:{df.shape}")
    
    df.reset_index(drop=True, inplace=True)
    
    json_record = list(json.loads(df.T.to_json()).values()) #Json will load df and then it will transpose the df, export to json and then will extract the values only(from key value pair) and make a list of same
    print(json_record[0])
    
    client[collection_name][collection_name].insert_many(json_record) #Inserting all the transposed json records to database