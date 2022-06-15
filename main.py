from fileinput import filename
from PyPDF2 import PdfFileReader, PdfFileWriter



filename = "System+Center+Configuration+Manager+Overview.pdf"
reader = PdfFileReader(filename)

with open('2.txt', 'w') as f:
    
    for page_num in range(reader.numPages):
        # print('Page: {0}'.format(page_num))
        pageObj = reader.getPage(page_num)

        try: 
            txt = pageObj.extractText()
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num+1))
            f.write(''.center(100, '-'))
            f.write(txt)
    f.close()