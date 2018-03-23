from pyAudioAnalysis import audioTrainTest as aT
aT.featureAndTrain(["data/tiger","data/snake"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", True)
aT.fileClassification("test.wav", "svmSMtemp","svm")
