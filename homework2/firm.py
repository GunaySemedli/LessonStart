firm_id=0
class Firm:
    def __init__(self,_name,_category,_product,):
        global firm_id
        firm_id+=1
        self.id=firm_id
        self.firmName=_name
        self.firmCategory=_category
        self.firmProduct=_product