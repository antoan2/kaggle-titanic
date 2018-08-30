#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pandas as pd


class DataLoader:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_set(self, dataset):
        print('## Loading data %s' % dataset)
        assert (dataset in ['train', 'test'])

        path_data = self.get_path_set(dataset)
        data = pd.read_csv(path_data)

        if dataset == 'train':
            data, labels = self.get_labels_train(data)
        else:
            data, labels = self.get_labels_test(data)

        self.write_dataframe_name(data, dataset)
        self.write_dataframe_name(labels, dataset)
        return data, labels

    def clean_data(self, data):
        print('## Prepare %s' % data.dataset_name)

        # Mapping female / male to 1 / 0
        d = {'female': 1, 'male': 0}
        data['Sex'] = data['Sex'].map(d)

        # Droping useless datas
        data = data.drop(
            columns=['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked'])

        # Fill Nans
        data['Age'] = data['Age'].fillna(data['Age'].mean())
        data['Fare'] = data['Fare'].fillna(data['Fare'].mean())
        return data

    def write_dataframe_name(self, data, dataset):
        data.dataset_name = 'data %s' % dataset

    def get_path_set(self, dataset):
        return os.path.join(self.data_path, dataset + '.csv')

    def get_labels_train(self, data):
        labels = data['Survived']
        data = data.drop(columns='Survived')
        return data, labels

    def get_labels_test(self, data):
        temp_labels = pd.read_csv(
            os.path.join(self.data_path, 'gender_submission.csv'))
        labels = pd.Series(
            index=temp_labels['PassengerId'],
            data=list(temp_labels['Survived']))
        return data, labels
