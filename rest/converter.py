import sys
import os
import PyPDF3
import pyttsx3
import pdfplumber
from langdetect import detect
from rest_framework import status
from api import settings


class Convert:
    def __init__(self, origin="cmd"):
        self.origin = origin

    def make_audio(self, file=None, filename=None):
        if self.origin == "cmd":
            if len(sys.argv) < 2:
                sys.exit("Wrong/No parameters given")
            file = sys.argv[1]

        try:
            book = open(file, "rb")
        except (FileNotFoundError, FileExistsError):
            if self.origin == "cmd":
                sys.exit('File ' + file + ' does not exist or found')
            else:
                return status.HTTP_404_NOT_FOUND

        try:
            pdfReader = PyPDF3.PdfFileReader(book)
            # print(pdfReader.getDocumentInfo())
            pages = pdfReader.numPages
            finalText = ""

            with pdfplumber.open(file) as pdf:
                for i in range(0, pages):
                    page = pdf.pages[i]
                    text = page.extract_text()
                    finalText += text

            lang = detect(finalText)
            specific_folder = settings.MEDIA_ROOT + os.sep + "mp3"
            if not os.path.exists(specific_folder):
                os.mkdir(specific_folder)

            finalText = finalText.replace("_", "").replace("•", "").replace("|", "")

            if lang == "en":
                lang = "EN-US"
            else:
                lang = "FR-FR"

            def convert(f_name):
                engine = pyttsx3.init()

                voices = engine.getProperty('voices')
                for voice in voices:
                    if lang in voice.id:
                        engine.setProperty('voice', voice.id)
                        break

                rate = engine.getProperty('rate')
                engine.setProperty('rate', rate + 8)

                if self.origin == "cmd":
                    f_name = specific_folder + os.sep + file.split(".")[0] + ".mp3"
                else:
                    f_name = specific_folder + os.sep + f_name + ".mp3"

                engine.save_to_file(finalText, f_name)
                engine.runAndWait()

            convert(filename)
            return status.HTTP_201_CREATED
        except Exception:
            return status.HTTP_500_INTERNAL_SERVER_ERROR