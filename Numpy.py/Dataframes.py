'''DataFrames: Datasets in Pandas are usually multi-dimensional tables,called dataframes'''
import pandas as pd
Data={
    'Std1':
    {'Name':'Chinmai',
    'Branch':'Bio-Informatics',
    'ID':1001,
    'Skills':['Python','Dsa','Sql','C++']
    },
    'Std2':
    {'Name':'Ruhi',
    'Branch':'Bio-Tech',
    'ID':1045,
    'Skills':['Python','Dsa','Java','C']
    }
}
Data=pd.DataFrame(Data)
print(Data)
print(type(Data))