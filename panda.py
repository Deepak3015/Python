import pandas as pd
 
 
# df = pd.read_csv("New folder/sales_data_sample.csv",encoding= "latin1")


# print(df)

# Creating the data frame 

data ={
    "name": ["alice","bob","Charlie"],
    "age": [30,40,50],
    "city": ["newyork","losangles","lasvegas"]
}
df = pd.DataFrame(data)
print(df)
df.to_csv("First  OUtput")



