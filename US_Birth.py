#Introducing US Birth Data Set

f = open("US_births_1994-2003_CDC_NCHS.csv","r").read()
split_file = f.split("\n")
print(split_file[0:5])

#Create List of Lists using Functions:
def read_csv(data):
    string_list=[]
    final_list=[]
    
    f= open(data,"r").read()
    string_list=f.split("\n")[1:]
    
    
    for row in string_list:
        int_fields=[]
        string_fields= row.split(",")
        for i in string_fields:
            int_fields.append(int(i))
        final_list.append(int_fields)
    
    return final_list

cdc_list= read_csv("US_births_1994-2003_CDC_NCHS.csv")
print(cdc_list[0:5])

# Calculate Number of Births per Month:

def month_births(data):
    births_per_month={}
    
    for row in data:
        months = row[1]
        births = row[4]
        
        births_per_month[months]= births_per_month.get(months,0)+births
    return births_per_month

cdc_month_births = month_births(cdc_list)

# Calculate Number of Births per Day of Week (DOW):
def dow_births(data):
    births_per_dow={}
    
    for row in data:
        day_of_week = row[3]
        births= row[4]
        
        births_per_dow[day_of_week]= births_per_dow.get(day_of_week,0)+births
    return births_per_dow
cdc_day_births = dow_births(cdc_list)

print(cdc_day_births)

#Create a Generic Function to encapsulate all column calculations

def cal_counts(data,column):
    final_dic ={}
    
    for row in data:
        col = row[column]
        births = row[4]
        
        final_dic[col]= final_dic.get(col,0)+births
    return final_dic

cdc_year_births = cal_counts(cdc_list,0)
cdc_month_births= cal_counts(cdc_list,1)
cdc_dom_births =  cal_counts(cdc_list,2)
cdc_dow_births = cal_counts(cdc_list,3)

print(cdc_dow_births)


print(cdc_month_births)
        