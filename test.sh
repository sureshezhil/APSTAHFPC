#!/bin/sh
python createClassifierModel.py trainData
python record.py
python testclassfier.py output.wav	
