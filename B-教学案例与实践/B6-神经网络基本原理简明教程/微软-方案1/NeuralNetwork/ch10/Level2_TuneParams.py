# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import math

from LossFunction import * 
from Parameters import *
from Level0_TwoLayerNet import *
from DataReader import * 

x_data_name = "CurveX.dat"
y_data_name = "CurveY.dat"

def train(ne, batch, eta):
    dataReader = DataReader(x_data_name, y_data_name)
    XData,YData = dataReader.ReadData()
    X = dataReader.NormalizeX(passthrough=True)
    Y = dataReader.NormalizeY()
    
    n_input, n_hidden, n_output = 1, 4, 1
    eta, batch_size, max_epoch = 0.1, 10, 30000
    eps = 0.001

    params = CParameters(n_input, n_hidden, n_output,
                         eta, max_epoch, batch_size, eps, 
                         InitialMethod.Xavier,
                         OptimizerName.SGD)

    loss_history = CLossHistory()
    net = TwoLayerNet(NetType.Fitting)
    net.train(dataReader, params, loss_history)

    trace = loss_history.GetMinimalLossData()
    print(trace.toString())
    title = loss_history.ShowLossHistory(params)
    ShowResult(net, X, YData, title, trace.wb1, trace.wb2)


if __name__ == '__main__':

    ne, batch, eta = 4, 10, 0.1
    train(ne, batch, eta)
    ne, batch, eta = 4, 10, 0.3
    train(ne, batch, eta)
    ne, batch, eta = 4, 10, 0.5
    train(ne, batch, eta)
    ne, batch, eta = 4, 10, 0.7
    train(ne, batch, eta)

    ne, batch, eta = 4, 1, 0.5
    train(ne, batch, eta)
    ne, batch, eta = 4, 5, 0.5
    train(ne, batch, eta)
    ne, batch, eta = 4, 10, 0.5
    train(ne, batch, eta)
    ne, batch, eta = 4, 20, 0.5
    train(ne, batch, eta)

    ne, batch, eta = 2, 10, 0.5
    train(ne, batch, eta)
    ne, batch, eta = 4, 10, 0.5
    train(ne, batch, eta)
    ne, batch, eta = 8, 10, 0.5
    train(ne, batch, eta)
    ne, batch, eta = 16, 10, 0.5
    train(ne, batch, eta)


