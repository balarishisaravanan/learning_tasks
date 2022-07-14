import yaml



def search_key(d,flag=False):
    if isinstance(d, dict):
        for k, v in d.items():
            flag = search_key(k,flag) or search_key(v,flag)
            if k==search_param:
                return True
    return flag 




stream = open("data.yml","r")
dic = yaml.safe_load(stream)

search_param = input("Enter key to find")
success = search_key(dic)

if success:
    print("The key is found in the file!")
else:
    print("The key is not found, we will add it!")
    new_value = input("Enter the value for this key")
    dic[search_param] = new_value
    with open("data.yml","w") as yamlfile:
        yaml.safe_dump(dic, yamlfile)
    print("New key value pair added!") 
