doc = CP.create_doc('h', r'<FILENAME>.pdf')
elem = []
elem.append(CP.add_element_to_pdf(txt = 'TILE', type = 'title'))
elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
elem.append(CP.add_element_to_pdf(txt = 'This Report Contains below information', type = 'body'))
e
elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
elem.append(CP.add_element_to_pdf(txt = 'subtitle', type = 'stitle'))
if part_df.empty:
    elem.append(CP.add_element_to_pdf(txt = 'verification of emtpy datafare', type = 'body'))
else:
    elem.append(CP.add_element_to_pdf(txt = '', type = 'image', img='Part_ML.jpg' ))
    elem.append(CP.add_element_to_pdf(txt = 'Top 10 Tables', type = 'stitle'))
    elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
    elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
    elem.append(CP.add_element_to_pdf(txt = 'Another subtitle', type = 'stitle'))
    elem.append(CP.add_element_to_pdf(txt = '',df=pq1.drop('STATSTIME',1).head(10), type = ''))
 
elem.append(CP.add_element_to_pdf(txt = '<link href=link here> + SQL Source - Click here + </link>',type='body'))
elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))
elem.append(CP.add_element_to_pdf(txt = '     ', type = 'body'))

elem.append(CP.add_element_to_pdf(txt = 'Created By : ', type = 'footer'))
elem.append(CP.add_element_to_pdf(txt = 'Created on : ' + str(dt.datetime.now()), type = 'footer'))
doc.build(elem)
