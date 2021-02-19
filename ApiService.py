import requests

class ApiService:
    
    def get():
        response = requests.get("https://jsonplaceholder.typicode.com/todos")
        print(len(response.json()))
        for i in response.json():
            print(i['title'])
