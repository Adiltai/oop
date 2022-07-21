import json
from register import User

class Product():
    FILE='jsondb/data.json'
    id=0
    def __init__(self,title,description,price, quantity,owner) -> None:
        self.title=title
        self.description=description
        self.price=price
        self.qty=quantity
        self.owner=owner
        self.send_product_to_json()

    @classmethod
    def get_id(cls):
        cls.id+=1
        return cls.id

    @classmethod
    def get_data(cls):
        with open(cls.FILE, 'r') as file:
            return json.load(file)
    

    @staticmethod
    def get_one_product(data, id):
        product= list(filter(lambda x: x['id']==id, data))
        if not product:
            return 'Нет такого продукта'
        return product[0]
    
    @classmethod
    def send_data_to_json(cls, data):
        with open(cls.FILE, 'w') as file:
            json.dump(data, file)
    


    def send_product_to_json(self):
        data=Product.get_data()
        product={
            'id':Product.get_id(),
            'title': self.title,
            'description':self.description,
            'price': self.price,
            'quantity':self.qty,
            'owner':self.owner
        }
        data.append(product)
        with open(Product.FILE, 'w') as file:
            json.dump(data, file)
        return {'status': '201', 'msg': product}


    @classmethod
    def retrieve_data(cls, id):
        data = cls.get_data()
        product=cls.get_one_product(data,id)
        return product

    @classmethod
    def update_data(cls, id, **kwargs):
        data=cls.get_data()
        product=cls.get_one_product(data, id)
        if type(product)!= dict:
            return product
        index = data.index(product)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return{'status': '200 ','msg': 'updated'}

    @classmethod
    def delete_product(cls, id):
        data=cls.get_data()
        product=cls.get_one_product(data, id)
        if type(product)!= dict:
            return product

        index=data.index(product)
        data.pop(index)
        cls.send_data_to_json(data)
        return {'status': '204', 'msg': 'deleted'}

        
with open(Product.FILE, 'w') as file:
    json.dump([], file)

user=User().login('JohnSnow', 'john1234')
print(user)
username=user['user']['username']

obj1=Product('Samsung Galaxy S22', 'Cool Phone!', 1000, 10 , 'John Snow')
obj2=Product('Iphone 14', 'Mega Cool Phone!', 1300, 5 , 'John Berg')
obj3=Product('Nokia 3110', 'Retro Cool Phone!', 100, 100 , 'John Jones')

print('All products:\n', Product.get_data())
print(Product.retrieve_data(3))
print(Product.update_data(3, title='Nokia 3110 Super'))
print(Product.retrieve_data(3))
print(Product.delete_product(3))
print('All products:\n', Product.get_data())
