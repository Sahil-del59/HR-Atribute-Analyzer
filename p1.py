import numpy as np
import pandas as pd
df_emp=pd.DataFrame({
    "id":[101,102,103,104,105,106,107,108,109,110],
    "age":[34,56,45,35,47,56,45,35,25,23],
    "department":["IT","HR","HR","IT","Finance","Finance","Marketing","Marketing","IT","IT"],
    "monthly_salary":[75000,50000,np.nan,56000,36000,np.nan,80000,np.nan,120000,140000],
    "attrition_status":[1,0,0,0,1,1,0,1,1,0]
})
df_work=pd.DataFrame({
    "id":[101,102,103,104,105,106,107,108,109,110],
    "overtime":[1,2,3,0,0,6,4,4,0,3],
    "stock_options":[0,0,0,0,1,2,0,1,3,3],
    "performance_rating":[5,3,4,4,5,2,4,4,5,5]
})
df_company=pd.merge(df_emp,df_work,on="id",how="inner")
df_company["monthly_salary"]=df_company["monthly_salary"].fillna(df_company.groupby("department")["monthly_salary"].transform("mean"))
df_company["productivity_per_dept"]=df_company.groupby("department")["performance_rating"].transform("mean")
print(df_company)
high_perf_no_stock_leaving=df_company[(df_company["performance_rating"]>=4)
                                      &(df_company["attrition_status"]==1)
                                      &(df_company["stock_options"]==0)]
print(high_perf_no_stock_leaving)




