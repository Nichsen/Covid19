# Main File!
import src_code.getData as getData
import src_code.analyseData as analyse
import src_code.generateHTML as HTMLgenerator
import os
import subprocess

getData.apiCall()  #Create json file for current day
analyse.renderCurrentDay() # Create calc json file
filePath = HTMLgenerator.genHtmlfile() # creates html file for current day

print(filePath)

