import json
import csv   
    
def JSONify(dictionary):
    json_object = json.dumps(dictionary)
    print(json.dumps(json.loads(json_object), indent = 4, sort_keys = True))
    return json_object

def JSONtoCSV(dictionary):
    dictionary = json.loads(dictionary)
    f = csv.writer(open("offers.csv", "wb+"))
    f.writerow(["Discount", "Description", "Promocode", "Site", "Title", "Tags"])
    for item in dictionary:
	try:
	    row = [item['Discount'], item['Description'], item['Promocode'], item['Site'], item['Title']]
	    for tag in item['Tags']:
		row.append(tag) 
	    f.writerow(row)
	except:
	    pass
