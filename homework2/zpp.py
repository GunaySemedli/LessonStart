from yb import products,firms,categories


def searchCategory(_categoryName):
     for category in categories:
          if category.categoryName==_categoryName:
               print(f"{category.categoryName} - Product : {category.categoryProduct} , Firm : {category.categoryFirm}")
               break
          else:
               print(f"Teessuf ki, bu adda kategoriya movcud deyil")     
ad=input(" Kategoriya adini daxil edin :")     
searchCategory(ad)          
          