#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset_unix.pkl", "rb") )
features = ["salary", "bonus"]

"""
#Removing TOTAL data_set
bonuses = [x[1] for x in data]
print(max(bonuses))
print(bonuses)
print([key for key in data_dict if data_dict[key]["bonus"]==97343619.0])
"""



data_dict.pop('TOTAL', 0)

data = featureFormat(data_dict, features)
bonuses = np.sort([x[1] for x in data ])[-2:]
print(bonuses)#7000000. 8000000.
salaries = np.sort([x[0] for x in data ])[-3:]
print(salaries)#[1060932. 1072321. 1111258.]
for key in data_dict:
    if data_dict[key]["bonus"] in bonuses.tolist():
        print(key,data_dict[key]["bonus"])

for key in data_dict:
    if data_dict[key]["salary"] in salaries.tolist():
        print(key,data_dict[key]["salary"])

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter( salary, bonus )

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()


