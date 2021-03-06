import sys, os
sys.path.insert(0, os.path.dirname('..'))
from extrmlnet import ExtrmlNet
import numpy as np
from pylab import plot,show,subplot,title,scatter

if __name__ == '__main__':
    x = np.linspace(-1.0,5.0,15)
    y = np.cos(x)+(np.random.rand(15)-.5)*.7 # training points with noise

    subplot(1,3,1)
    net = ExtrmlNet(18)
    net.fit(x,y)
    yy = net.predict(x)
    plot(x,yy,'-r') # red line is the output of the network
    plot(x,np.cos(x),'-g') # the green line is the function we want to approximate
    scatter(x,y, facecolors='none', edgecolors='b') # blue points are samples that we use for the training
    title('no regularization')
    subplot(1,3,2)
    net = ExtrmlNet(18,gamma=0.0001)
    net.fit(x,y)
    yy = net.predict(x)
    plot(x,yy,'-r')
    plot(x,np.cos(x),'-g')
    scatter(x,y, facecolors='none', edgecolors='b')
    title('$\gamma=0.0001$')
    subplot(1,3,3)
    net = ExtrmlNet(18,gamma=1.0)
    net.fit(x,y)
    yy = net.predict(x)
    plot(x,yy,'-r')
    plot(x,np.cos(x),'-g')
    scatter(x,y, facecolors='none', edgecolors='b')
    title('$\gamma=1$')
    show()
