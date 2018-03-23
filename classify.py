from pyAudioAnalysis import audioTrainTest as aT
aT.featureAndTrain(["classifierData/snake","classifierData/Cheetah","classifierData/frog","classifierData/Fox","classifierData/seal","classifierData/panther","classifierData/tiger"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
aT.fileClassification("rattlesnake.wav", "svmSMtemp","svm")