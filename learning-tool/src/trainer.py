#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn import svm
from sklearn import preprocessing


class Trainer:
    def __init__(self):
        self.preprocessor = preprocessing.StandardScaler()
        self.model = svm.SVC()

    def fit_preprocessor(self, data):
        self.preprocessor = self.preprocessor.fit(data)

    def fit_model(self, data, labels):
        self.model.fit(data, labels)

    def train(self, data, labels):
        self.fit_preprocessor(data)
        data = self.preprocessor.transform(data)
        self.fit_model(data, labels)

    def predict(self, data):
        data = self.preprocessor.transform(data)
        return self.model.predict(data)
