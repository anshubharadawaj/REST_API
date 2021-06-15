import requests
import json

# URL="http://127.0.0.1:8000/emp_api_fn/"
# URL="http://127.0.0.1:8000/api_fbv/"
# URL="http://127.0.0.1:8000/student_api/"
URL="http://127.0.0.1:8000/student_api/<int:pk>/"
def get_data(id=None):
    data={}
    headers = {'content-Type': 'application/json'}
    if id is not None:
     data={'id':id}

     json_data = json.dumps(data)
     r=requests.get(url=URL,headers=headers,data=json_data)
     data=r.json()
     print(data)

    else:
        headers={'content-Type':'application/json'}
        json_data= json.dumps(data)
        r=requests.get(url=URL, headers=headers, data=json_data)
        data=r.json()
        print(data)


# get_data(1)
# get_data()

def post_data():
    data={

        'name':'Sohan',
        'roll':104,
        'city':'patna',
    }
    headers={'content-Type': 'application/json'}

    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

# post_data()


def update_data():
    data={
        'id':4,
        'name':'Rinku_new',
        'city':'Mumbai',


    }
    headers = {'content-Type': 'application/json'}
    json_data=json.dumps(data)
    r=requests.put(url=URL,headers=headers, data=json_data)
    data=r.json()
    print(data)

# update_data()

def delete_data():
    data={'id':3}
    headers = {'content-Type': 'application/json'}
    json_data=json.dumps(data)
    r=requests.delete(url=URL, headers=headers,data=json_data)
    data=r.json()
    print(data)

# delete_data()