"""
@Author: Phani
@Version 1.0
Module to create the pdf report format for reportlab
"""

# for pdf
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd
from os import getcwd
from PIL import Image as Im
# !/usr/local/bin/python
# to PDF report

# global variables
# TODO: Get this line right instead of just copying it from the docs
style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('SIZE', (0, 0), (-1, -1), 5),
                    ('TEXTCOLOR', (0, 0), (-1, -1), colors.crimson),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ('TEXTCOLOR', (0, 0), (-1, -1), colors.blue),
                    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                    ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                    ])

# Configure style and word wrap
s = getSampleStyleSheet()
s = s["h6"]
s.wordWrap = 'CJK'


styles = getSampleStyleSheet()


def create_doc(ori='l', file=''):
    """
    Creates document element for reportlab usage
    :param file: pdf file name (with .pdf extenstion)
    :param ori: orientation 'l' indicates landscape(default) if portrait specify p size is A4
    :return: document object where we can add elements and build it to create pdf.
    """
    if '\\' in file or '/' in file:

        doc = SimpleDocTemplate(file,
                            pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
    else:
        doc = SimpleDocTemplate(getcwd() + '\\' + str(file),
                                pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
    if ori == 'l':
        doc.pagesize = landscape(A4)
    else:
        doc.pagesize = A4
    return doc


def add_element_to_pdf(txt='Sample', df=pd.DataFrame(), type='body', img ='', ori='l'):
    """ Add elements to pdf element list.
    Usage: add_element_to_pdf(txt='Sample', df=dataframe object, type ='body,title,footer,image
    :returns: element that can be added as reportlab pdf element to enable build """
    elem = ''
    if type == 'title':
        elem = Paragraph(txt, styles['Title'])
    elif type == 'footer':
        elem = Paragraph(txt, styles['bu'])
    elif type == 'stitle':
        elem = Paragraph(txt, styles['h4'])
    elif type == 'image':
        # img = "week.png"
        # We really want to scale the image to fit in a box and keep proportions.
        with Im.open(img) as im:
            w,h = im.size
        # print w,h
        if ori == 'l':
            if w > 700:
                h = (h * 700 / w)/2
                w =  (700)/2
            if h > 500:
                h = 500/2
                w = (w * 500/h)/2
        else:
            w,h = w-(w * 0.6),h-(h * 0.6)
        im = Image(img, width=w, height=h)
        elem = im
    elif type == 'body':
        elem = Paragraph(txt, styles['h6'])
    elif not df.empty:
        # try:
            # print data
            # print data
            data = conv_to_str(df)
            # data = [data.columns[:, ].values.astype('unicode').tolist()] + data.values.astype('unicode').tolist()
            data = [data.columns[:, ].values.tolist()] + data.values.tolist()
            data2 = [[Paragraph(cell, s) for cell in row] for row in data]
            # print data2
            # print s
            # print style

            t = Table(data2)
            t.setStyle(style)
            elem = t
            # print t
        # except UnicodeDecodeError:
        #     print 'parsing error'
        # except UnicodeEncodeError:
        #     print 'parsing enc error'
    return elem




def str_col(x):
    if type(x) == str or type(x) == unicode:
        x = x.encode('utf-8')
    else:
        x = str(x)
    return x


def conv_to_str(df):
    """
    Convert given dataframe columns to string
    """
    for col in df.columns:
        try:
            if df[col].dtype == 'O':
                df[col] = df[col].apply(lambda x: str_col(x))
            else:
                df[col] = df[col].apply(lambda x: str_col(x))
        except UnicodeDecodeError:
            continue
        except UnicodeEncodeError:
            continue

    return df

def build_pdf(doc,elem):
    """
    Build and create pdf
    :param elem: element list generated from add_add_element_to_pdf method
    :return: generates pdf of given doc
    """
    doc.build(elem)

# def add_data_to_elem(area):
#     data = final_df(wk_data, area)
#     data['Recent Occurance'] = data['Recent Occurance'].apply(lambda x: str(x))
#     data['Closure notes'] = data['Closure notes'].apply(lambda x: str(x)[1:500])
#     data['Num Of Errors'] = data['Num Of Errors'].apply(lambda x: str(x))
#     data = [data.columns[:, ].values.astype(str).tolist()] + data.values.astype(str).tolist()
#     data2 = [[Paragraph(cell, s) for cell in row] for row in data]
#     t = Table(data2)
#     t.setStyle(style)
#
#     # append
#     elements.append(t)
#
#
# styles = getSampleStyleSheet()
# doc = SimpleDocTemplate(
#     r"I:\Dat\34BKALL\CRSM\Capacity Mgmt in CRSM\Reports\Source\Output\wk\CRSM_batch_%s.pdf" % wk_file.split('.')[0],
#     pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
# doc.pagesize = landscape(A4)
# elements = []
#
# elements.append(Paragraph("BBIT - CRSM, Weekly batch Issues - %s" % wk_file, styles['Title']))
#
# # TODO: Get this line right instead of just copying it from the docs
# style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                     ('TEXTCOLOR', (0, 0), (-1, 0), colors.crimson),
#                     ('VALIGN', (0, 0), (-1, -1), 'TOP'),
#                     ('TEXTCOLOR', (0, 0), (-1, -1), colors.blue),
#                     #                        ('ALIGN',(0,-1),(-1,-1),'CENTER'),
#                     #                        ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
#                     #                        ('TEXTCOLOR',(1,-1),(-1,-1),colors.green),
#                     ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#                     ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
#                     ])
#
# # Configure style and word wrap
# s = getSampleStyleSheet()
# s = s["BodyText"]
# s.wordWrap = 'CJK'
#
# # Job errors per area plot
# elements.append(Paragraph("Last week Failures per Area ", styles['h4']))
#
# img = "week.png"
# # We really want to scale the image to fit in a box and keep proportions.
# im = Image(img, 6 * inch, 2 * inch)
# elements.append(im)
#
# elements.append(Paragraph("Failures for each area", styles['h4']))
#
# for sy in wk_data.SYS.unique():
#     elements.append(Paragraph(sy.upper(), styles['h4']))
#     add_data_to_elem(sy)
#
# elements.append(Paragraph("End Of Report", styles['bu']));
# elements.append(Paragraph("Created by - PHSI", styles['bu']));
# elements.append(Paragraph("Generated On :" + str(dt.datetime.now()), styles['bu']));
# doc.build(elements)