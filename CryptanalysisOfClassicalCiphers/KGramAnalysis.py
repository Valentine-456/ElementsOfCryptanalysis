import re
import math

class KGramAnalysis:
    def __init__(self, textToAnalize: str,  k: int = 2):
        self._k = k
        self._textToAnalize = re.sub(r'[^a-z]', '', textToAnalize.lower())
    
    def getUniqueKGramsCounted(self) -> dict[str, int]:
        kGramCountTable = {}
        numberOfKGrams = len(self._textToAnalize) - self._k + 1
        
        for i in range(numberOfKGrams):
            kGram = self._textToAnalize[i:i+self._k]
            if kGram in kGramCountTable.keys():
                kGramCountTable[kGram] += 1
            else:
                kGramCountTable[kGram] = 1
        
        return kGramCountTable
    
    def getFrequencyTableKGrams(self) -> dict[str, float]:
        frequencyTable = self.getUniqueKGramsCounted()
        numberOfKGrams = len(self._textToAnalize) - self._k + 1

        for key, value in frequencyTable.items():
            frequencyTable[key] = (value/numberOfKGrams)*1.0

        return frequencyTable
    
    def getFrequencyTableSorted(self, frequencyTableKGrams) -> list[(str, float)]:
        frequenciesListSorted = list(frequencyTableKGrams.items())
        frequenciesListSorted.sort(key = lambda x: x[1], reverse = True)
        return frequenciesListSorted
        
    def calculateLogarithmicFitnessTable(self) -> tuple[dict[str, float], float]:
        fitnessTable = self.getFrequencyTableKGrams()
        numberOfKGrams = len(self._textToAnalize) - self._k + 1
        
        for key in fitnessTable.keys():
            fitnessTable[key] = math.log(fitnessTable[key], 10)
        floor = math.log(0.01/numberOfKGrams ,10)
        return fitnessTable, floor
    
    def fitnessMeasure(self, sample: str, fitnessTable: dict[str, float], floor: float) -> float:
        sampleText = re.sub(r'[^a-z]', '', sample.lower())
        score = 0
        for i in range(len(sampleText) - self._k + 1):
            d = sampleText[i:i+self._k]
            if d in fitnessTable.keys():
                score += fitnessTable[d]
            else:
                score += floor
        return score