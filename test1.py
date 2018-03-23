from pyAudioAnalysis import audioSegmentation as aS
[flagsInd, classesAll, acc, CM] = aS.mtFileClassification("data/s.wav", "data/svmSM", "svm", True, 'data/scottish.segments')
