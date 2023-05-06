import re
from KGramAnalysis import KGramAnalysis

def lclear(text):
    return re.sub(r'[^a-z]', '', text.lower())

def getFrequencyTable(text: str, alphabet: list[str]) -> dict[str, float]:
    frequencyTable = {}
    for letter in alphabet:
        frequencyTable[letter] = 0
    
    preprocessedText = re.sub(r'[^a-z]', '', text.lower())
    totalLength = len(preprocessedText)
    for i in preprocessedText:
        frequencyTable[i] = frequencyTable[i] + 1
    for key, value in frequencyTable.items():
        frequencyTable[key] = (value/totalLength)
     
    return frequencyTable
