from pyAudioAnalysis import audioTrainTest as aT
aT.featureAndTrain(["classifierData/snake","classifierData/tiger"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
aT.fileClassification("snakehit.wav", "svmSMtemp","svm")