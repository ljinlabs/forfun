# First place all of the diuscussion pdfs
# and simply run the python file using the discussion number
#
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def check_content(path="."):
    for filename in os.listdir(path):
        if not filename.endswith(".pdf"):
            return False

def go_through(path=None,discussion_number=None):
    '''
    Build 1: assuming I do everything perfectly
    '''
    output_name = "Group6_Discussion" + discussion_number + " _Haylee_Jake_J.pdf" if discussion_number else "test.pdf"
    if path:
        my_dir = os.path.join("C:","Users","ljin0","Documents","School","UIUC","2020(Summer)","Phys211","Discussion",path)
    else:
        my_dir = os.getcwd()
    
    writer = PdfFileWriter()
    for filename in os.listdir(my_dir):
        reader = PdfFileReader(filename)
        for page in range(reader.getNumPages()):
            ## add each page to the writer object
            writer.addPage(reader.getPage(page))
    
    with open(output_name,'wb') as w:
        writer.write(w)
    print(f'''
    File {output_name} created at {my_dir}
    ''')
if __name__ == "__main__":
    go_through()
    print(check_content())
