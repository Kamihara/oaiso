#!/usr/bin/python
# coding: utf-8

import numpy as np
from sklearn.svm import LinearSVC
from sklearn.model_selection import KFold

class Classifier():
  """docstring for Classifier"""
  def __init__(self, labeled_shops):
    self.shops = labeled_shops
    self.X = []
    for shop in labeled_shops:
      self.X.append(shop.vector)
    self.X = np.array(self.X)
    #self.X.transpose()

  def fit(self, X, y, cost):
    y = np.array(y)
    n_splits = 4
    clf = LinearSVC(C=cost)
    kf = KFold(n_splits=n_splits)
    kf.get_n_splits(self.X)
    sigma = 0.0
    clfs = []
    p = []
    for train_index, test_index in kf.split(self.X):
      X_train, X_test = self.X[train_index], self.X[test_index]
      y_train, y_test = y[train_index], y[test_index]
      try:
        clf.fit(X_train, y_train)
        clfs.append(clf)
        p.append(clf.score(X_test, y_test))
      except:
        pass
    return clfs, p

  def yes_or_no(self, v, clfs, probabilities):
    if len(clfs) != len(probabilities):
      return None

    yes = 1.0
    no = 1.0
    for i,clf in enumerate(clfs):
      if clf.predict([v])[0]:
        yes *= probabilities[i]
        no *= 1-probabilities[i]
      else:
        yes *= 1-probabilities[i]
        no *= probabilities[i]
    return yes > no

  # evaluation
  def scores(self):
    print('X = {0}\n'.format(self.X.shape))
    print('Class = 0:Others 1:Eats or drinks')
    y = []
    for shop in self.shops:
      y.append(int(shop.priority_food + shop.priority_drink > shop.priority_speed + shop.priority_atmosphere))
    y = np.array(y)
    print('y = {0}'.format(y[y>0].shape))
    C = 2
    print('Cost Parameter = {0}'.format(C))
    clfs, p = self.fit(self.X, y, C)
    p = np.array(p)
    print('Accuracy = {0}\n'.format(p.mean()))

    print('Class = 0:Slow 1:Fast')
    y = []
    for shop in self.shops:
      y.append(int(shop.priority_speed > 1.5))
    y = np.array(y)
    print('y = {0}'.format(y[y>0].shape))
    C = 1.2
    print('Cost Parameter = {0}'.format(C))
    clfs, p = self.fit(self.X, y, C)
    p = np.array(p)
    print('Accuracy = {0}\n'.format(p.mean()))
    
    print('Class = 0:Others 1:Drinks(3)')
    y = []
    for shop in self.shops:
      y.append(int(shop.priority_drink == 3))
    y = np.array(y)
    print('y = {0}'.format(y[y>0].shape))
    C = 1
    print('Cost Parameter = {0}'.format(C))
    clfs, p = self.fit(self.X, y, C)
    p = np.array(p)
    print('Accuracy = {0}\n'.format(p.mean()))
    
    print('Class = 0:Others 1:Atmosphere(>1)')
    y = []
    for shop in self.shops:
      y.append(int(shop.priority_atmosphere > 1))
    y = np.array(y)
    print('y = {0}'.format(y[y>0].shape))
    C = 4
    print('Cost Parameter = {0}'.format(C))
    clfs, p = self.fit(self.X, y, C)
    p = np.array(p)
    print('Accuracy = {0}\n'.format(p.mean()))
    
    print('Class = 0:Not Alone 1:Alone(>0)')
    y = []
    for shop in self.shops:
      y.append(int(shop.can_alone > 0))
    y = np.array(y)
    print('y = {0}'.format(y[y>0].shape))
    C = 4
    print('Cost Parameter = {0}'.format(C))
    clfs, p = self.fit(self.X, y, C)
    p = np.array(p)
    print('Accuracy = {0}\n'.format(p.mean()))
    
  def predict(self, v):
    # check v todo xxx

    # eats + drinks vs others
    y = []
    for shop in self.shops:
      y.append(int(shop.priority_food + shop.priority_drink > shop.priority_speed + shop.priority_atmosphere))
    clfs, p = self.fit(self.X, y, 2)
    is_eats_or_drinks = self.yes_or_no(v, clfs, p)

    # speed
    y = []
    for shop in self.shops:
      y.append(int(shop.priority_speed > 1.5))
    clfs, p = self.fit(self.X, y, 1.2)
    is_speed = self.yes_or_no(v, clfs, p)  

    # drinks
    y = []
    for shop in self.shops:
      #y.append(int(shop.priority_drink == 3))
      y.append(int(shop.priority_drink > 1))
    clfs, p = self.fit(self.X, y, 1)
    is_drinks = self.yes_or_no(v, clfs, p)  

    # atmosphere
    y = []
    for shop in self.shops:
      y.append(int(shop.priority_atmosphere > 1))
    clfs, p = self.fit(self.X, y, 4)
    is_atmosphere = self.yes_or_no(v, clfs, p)  

    # can_alone
    y = []
    for shop in self.shops:
      y.append(int(shop.can_alone > 0))
    clfs, p = self.fit(self.X, y, 4)
    can_alone = self.yes_or_no(v, clfs, p)

    # construct label
    label = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    if is_drinks:
      if is_eats_or_drinks:
        label[3] = 3.0
      else:
        label[4] = 3.0
      if is_atmosphere:
        label[5] = 1.5
      elif is_speed:
        label[6] = 1.5
    else:
      if is_speed:
        label[6] = 3.0
      else:
        label[5] = 3.0
      if is_eats_or_drinks:
        label[4] = 3.0
    if can_alone:
      label[7] = 3.0
    else:
      label[8] = 3.0

#   if is_eats_or_drinks:
#      if is_drinks:
#        label[4] = 3.0
#      else:
#        label[3] = 3.0
#      if is_atmosphere:
#        label[5] = 1.5
#      elif is_speed:
#        label[6] = 1.5
#    else:
#      if is_speed:
#        label[6] = 3.0
#      else:
#        label[5] = 3.0
#      if is_drinks:
#        label[4] = 1.5
#    if can_alone:
#      label[7] = 3.0
#    else:
#      label[8] = 3.0

    return label
