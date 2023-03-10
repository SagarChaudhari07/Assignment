import pandas as pd

inputFile = "input.xlsx"

sheet1 = pd.read_excel(inputFile,sheet_name= "Sheet1")
sheet2 = pd.read_excel(inputFile,sheet_name= "Sheet2")
sheet3 = pd.read_excel(inputFile,sheet_name= "Sheet3")

print(sheet1.head(10),'\n')

print(sheet2.head(),'\n')

print(sheet3.head(),'\n')

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

dept = ["-"]*len(sheet4['id'])
print('\n', dept, '\n')

for i,j in zip(sheet2['id'],sheet2['dept']):
    for idx,k in enumerate(sheet4['id']):
        if k == i:
            dept[idx] = j

sheet4['dept'] = dept

desg = ["-"]*len(sheet4['id'])

for i,j in zip(sheet3['id'],sheet3['desg']):
    for idx,k in enumerate(sheet4['id']):
        if k == i:
            desg[idx] = j

sheet4['desg'] = desg
sheet4.to_excel("output.xlsx")
print("File saved successfully",'\n')

print(sheet4.head(10),'\n')                                