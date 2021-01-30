from flask import Flask,render_template,redirect,url_for,request,send_file
from PIL import Image
import os
from fpdf import FPDF



app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.htm')
from src import * 
@app.route('/upload',methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f1 = request.files['file']
        f2 = Image.open(f1)
        f2_format = f2.format
        print(f2_format)
        f2.save(r'static/input/test.png')
        # if f2_format == 'PNG':
        #     return 'PNG'
        # elif f2_format == 'JPG':
        #     return 'JPG'
        # elif f2_format == 'JPEG':
        #     return 'JPEG'
        # else:
        #     return 'unsupported file format'
        # file.save('test.')
        # exec(open('src/main_file.py').read)
        
        # main_file.main()
        return render_template('preview.htm')

@app.route('/extract',methods = ['POST', 'GET'])
def extract():
    if request.method == 'POST':
        os.system('python src/main_file.py')
        file2 = open("testfile.txt", "r")
        # return render_template('extracted.htm')
        with open ('testfile.txt','r') as file:
            output_var = file.read()
        print("Hello")
        print (output_var)
        os.remove('static/input/test.png')
        return render_template('extracted.htm', value = output_var)

@app.route('/pdf', methods=['POST'])
def pdf():
    for_pdf = request.form['corrected']
    # save FPDF() class into a  
    # variable pdf 
    pdf = FPDF() 
  
    # Add a page 
    pdf.add_page() 
  
    # set style and size of font  
    # that you want in the pdf 
    pdf.set_font("Arial", size = 15) 
  
    # create a cell 
    pdf.cell(200, 10, txt = for_pdf,  ln = 1, align = 'C') 
    # save the pdf with name .pdf 
    pdf.output("pdffile.pdf")  
    return send_file('pdffile.pdf', attachment_filename='recognized.pdf')
    # return 'You entered: {}'.format(request.form['corrected'])


if __name__ == '__main__':
    app.run(debug=True)



