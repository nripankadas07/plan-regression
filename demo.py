import json
from plan_regression import compare
old={'Node Type':'Seq Scan','Relation Name':'orders','Total Cost':100,'Plan Rows':1000}
new={**old,'Total Cost':160,'Plan Rows':1600}
print(json.dumps(compare(old,new),indent=2))
