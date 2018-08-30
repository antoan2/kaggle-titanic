#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn import metrics

from data_loader import DataLoader
from trainer import Trainer


class Experiment:
    def __init__(self):
        self.data_loader = DataLoader('/data')
        self.trainer = Trainer()

    def run(self):
        train_data, train_labels = self.data_loader.load_set('train')

        test_data, test_labels = self.data_loader.load_set('test')

        train_data = self.data_loader.clean_data(train_data)
        test_data = self.data_loader.clean_data(test_data)

        self.trainer.train(train_data, train_labels)

        train_predictions = self.trainer.predict(train_data)
        test_predictions = self.trainer.predict(test_data)

        print('Train accuracy: ',
              self.compute_score(train_labels, train_predictions))
        print('Test accuracy: ',
              self.compute_score(test_labels, test_predictions))

    def compute_score(self, labels, predictions):
        return metrics.accuracy_score(labels, predictions)
