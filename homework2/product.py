product_id=0
class Product:
    def __init__(self,_name,_category,_firm,):
        global product_id
        product_id+=1
        self.id=product_id
        self.productName=_name
        self.productCategory=_category
        self.productFirm=_firm