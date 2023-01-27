import pandas as pd

file1 = "Sheet1.xlsx"
file2 = "Sheet2.xlsx"
file3 = "Sheet3.xlsx"

sheet1 = pd.read_excel(file1)
sheet2 = pd.read_excel(file2)
sheet3 = pd.read_excel(file3)
# print(sheet1.head())
# print(sheet2.head())                              #............Question Number One                         
# print(sheet3.head())clscls

sheet4 = sheet1.copy()

#keystoadd = list(sheet2.keys())
#keystoadd.remove("id")

#print(keystoadd)

# for key in keystoadd:  
#     sheet4[key] = [None]*len(sheet4['id'])
# print(sheet4.head())
# print(sheet2['id'])
# print(sheet2['dept'])
# print(zip(sheet2['id'],sheet2['dept']))

dept = [None]*len(sheet4['id'])

for i,j in zip(sheet2['id'],sheet2['dept']):
    for idx,k in enumerate(sheet4['id']):
        if k == i:
            dept[idx] = j

sheet4['dept'] = dept

desg = [None]*len(sheet4['id'])

for i,j in zip(sheet3['id'],sheet3['desg']):
    for idx,k in enumerate(sheet4['id']):
        if k == i:
            desg[idx] = j

sheet4['desg'] = desg
sheet4.to_excel("sheet4.xlsx")

print(sheet4.head())                                