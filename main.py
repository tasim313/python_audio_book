import pyttsx3
import PyPDF2
book = open('file:///home/kali/Documents/Antonio Mel Django Example_Build powerful and reliable Python web applications from scratch-Packt Publishing 20Ltd(2020).pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
