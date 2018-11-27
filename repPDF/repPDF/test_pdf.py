# Import of Create PDF
import CreatePDF as CP
# Regular Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

# create random data
data = pd.DataFrame(data=[np.linspace(0,5,10),np.linspace(10,50,10)]).transpose()
data.columns=['a','b']

# create plot just for illustration
data.plot()
plt.savefig('sample.jpg')

# move to df
df = data

# create instance of file
doc = CP.create_doc('h', 'Sample.pdf')

# initialize all elements
elem = []

elem.append(CP.add_element_to_pdf(txt = 'Sample PDF Creation', type = 'title'))
elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
elem.append(CP.add_element_to_pdf(txt = 'This Report Contains below information', type = 'body'))

elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
elem.append(CP.add_element_to_pdf(txt = 'subtitle', type = 'stitle'))
if df.empty:
    elem.append(CP.add_element_to_pdf(txt = 'verification of emtpy datafare', type = 'body'))
else:
    elem.append(CP.add_element_to_pdf(txt = '', type = 'image', img='sample.jpg' ))
    elem.append(CP.add_element_to_pdf(txt = 'Top 10 data', type = 'stitle'))
    elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
    elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
    elem.append(CP.add_element_to_pdf(txt = 'Another subtitle', type = 'stitle'))
    elem.append(CP.add_element_to_pdf(txt = '',df=df.head(10), type = ''))
 
# elem.append(CP.add_element_to_pdf(txt = '<link href=link here> + SQL Source - Click here + </link>',type='body'))
elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))

elem.append(CP.add_element_to_pdf(txt = 'Created By : ', type = 'footer'))
elem.append(CP.add_element_to_pdf(txt = 'Created on : ' + str(dt.datetime.now()), type = 'footer'))
doc.build(elem)
