category_id=0
class Category:
    def __init__(self,_name,_product,_firm): 
        global category_id
        category_id+=1
        self.id=category_id
        self.categoryName=_name
        self.categoryProduct=_product
        self.categoryFirm=_firm