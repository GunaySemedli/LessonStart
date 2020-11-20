from yb import products,firms

def searchFirm(_firmName):
     for firm in firms:
          if firm.firmName==_firmName:
               print(f"{firm.firmName} {firm.firmCategory}")
               break
          else:
               print(f"Teessuf ki, bu adda firma movcud deyil")     
ad=input(" Firma adini daxil edin :")     
searchFirm(ad)          



