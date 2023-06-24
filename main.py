import PyPDF3
import pyttsx3
import pdfplumber
from langdetect import detect

file = "cv-Anselme.pdf"
book = open(file, "rb")
pdfReader = PyPDF3.PdfFileReader(book)
print(pdfReader.getDocumentInfo())
pages = pdfReader.numPages
finalText = ""

with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text

lang = detect(finalText)
finalText = finalText.replace("_", "").replace("•", "").replace("|", "")

if lang == "en":
    lang = "EN-US"
else:
    lang = "FR-FR"

def convert():
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    for voice in voices:
        if lang in voice.id:
            engine.setProperty('voice', voice.id)
            break

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + 8)

    engine.save_to_file(finalText, file.split(".")[0] + ".mp3")
    engine.runAndWait()


convert()
