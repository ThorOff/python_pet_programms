from gtts import gTTS
import pdfplumber
from art import tprint
from pathlib import Path


def pdf_to_mp3(file_path='test.pdf', language = 'en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'[+]   file{file_path} granted, wait...')
        #return 'File exist and have pdf format!'
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')
        my_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        return f'[+]   {file_name}.mp3 saved succsessfully!\n Have a good day!--'

    else:
        return str('File not exist or not in PDF format, check the file!').isupper()


def main():
    tprint('PDF_TO_MP3', font='bulbhead')
    file_path = input("Input file path, please!\n---")
    language = input('Input language! For eng - en, for rus - ru)\n---')
    print(pdf_to_mp3(file_path=file_path, language=language))

if __name__ == '__main__':
    main()