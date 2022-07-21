def search_object(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        id = args[1]
        for object_ in self.objects:
            if object_.get('id') == id:
                kwargs.update(object_ = object_)
                return func(*args, **kwargs)
    return wrapper



class CRUDMixin:
    def _get_or_set_objects_and_id(self):
        try:
            if(self.objects or not self.objects) and (self.id or not self.id):
                pass
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0
    
    def create(self, **kwargs):
        self._get_or_set_objects_and_id()
        self.id += 1
        object_ = dict(
            id = self.id, **kwargs
        )
        self.objects.append(object_)
        return {'status' :  201, 'msg' : object_}

    @search_object
    def retrieve(self, id, **kwargs):
        return kwargs['object_']
   
    @search_object
    def update(self, id, **kwargs):
        object_ = kwargs.pop('object_')
        object_.update(**kwargs)
        return {'status' : 200, 'msg' : 'Successfully updated'}
    
    @search_object
    def delete(self, id, **kwargs):
        delete_index = self.objects.index(kwargs['object_'])
        self.objects.pop(delete_index)
        return {'status' : 204, 'msg' : 'Successfully removed'}

smartphones = CRUDMixin()
smartphones.create(title = 'Redmi Note 10', body = 'The best for own price', qty = 10, price = 200)
smartphones.create(title = 'Redmi Note 20', body = 'The best', qty = 3, price = 400)
smartphones.create(title = 'Iphone 14 Pro Max', body = 'New Iphone', qty = 15, price = 1000)
smartphones.create(title = 'Samsung Galaxy S22', body = 'Cool nd expensive phone', qty = 5, price = 1200)
# print(smartphones.objects)
# print(smartphones.retrieve(4))
print(smartphones.update(2, title = 'Redmi Note 100', body = 'Made in China'))
print(smartphones.retrieve(2))
print(smartphones.delete(2))
print(smartphones.objects)

