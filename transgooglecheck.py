# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:58:55 2020

@author: intel
"""
import googletrans
from googletrans import Translator
import os

chunk = 14500

list_files = ["Learning PowerPoint 2019 Transcript" ,]

languageList = ['vietnamese',
 'spanish',
 'portuguese',
 'french',
 'japanese',
 'korean',
 'indonesian',
 'thai',
 'russian',
 'filipino',
 'italian',
 'german',
 'turkish',
 'chinese (traditional)',
 'chinese (simplified)',
 'hindi',
 'bengali',
 'polish',
 'greek',
 'arabic',
]

def getLangCode(Lang):
    return googletrans.LANGCODES.get(Lang)

def translate_file(filename):
    for lang in languageList:
        with open(f'{filename}.txt' , 'r') as file:
            totaldata = ''
            leftdata = ''
            while True:
                data = leftdata + file.read(chunk)
                if not data:
                    print('EOF')
                    break
                else:
                    maindata, leftdata = data.rsplit('\n',1)
                    trans = Translator()
                    transdata = trans.translate(maindata, dest = getLangCode(lang))
                    totaldata += transdata.text
                    del trans
            print(totaldata)
        os.chdir(f"{filename}!")
        with open(f'{filename + "-" + lang.title()}.txt' , 'a' , encoding = 'utf-8') as transedfile:
            transedfile.write(totaldata)
        os.chdir('../')

                
no = 1
for file in list_files:
    os.mkdir(f"{file}!")
    translate_file(file)
    

