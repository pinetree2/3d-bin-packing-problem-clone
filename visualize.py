from py3dbp import Packer, Bin, Item
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import matplotlib.pyplot as plt
import random

trucks = [
    #컨테이너 각각의 크기
    [250, 250, 500],
    [500, 500, 500],
    '''
     [500, 500, 400],
    [300, 300, 300],
    [300, 300, 200],
    [300, 300, 100],
    [500, 500, 500]
    '''
]




for t in range(len(trucks)):
    packer = Packer()
    truckX = trucks[t][0]
    truckY = trucks[t][1]
    truckZ = trucks[t][2]
    '''
    #packer.add_bin(Bin('small-envelope', 11.5, 6.125, 0.25, 10))
    #packer.add_bin(Bin('large-envelope', 15.0, 12.0, 0.75, 15))
    #packer.add_bin(Bin('small-box', 8.625, 5.375, 1.625, 70.0))
    #packer.add_bin(Bin('medium-box', 11.0, 8.5, 5.5, 70.0))
    #packer.add_bin(Bin('medium-2-box', 13.625, 11.875, 3.375, 70.0))
    #packer.add_bin(Bin('large-box', 240, 244, 1360, 70.0))
    #packer.add_bin(Bin('large-2-box', 23.6875, 11.75, 3.0, 70.0))
    '''
#Bin( container 이름 , contianer 가로 , container 세로 , container 높이 , 최대 무게) 컨테이너 생성
    packer.add_bin(Bin('LB', truckX, truckY, truckZ, 3000.0))
#Item(item 이름 , 가로 , 세로 , 높이, 무게)적재
    for i in range(5):
        packer.add_item(Item('boxU' + str(i), 200, 100, 50, 1))

    '''
    for i in range(10):
        packer.add_item(Item('boxU'+str(i), 100, 100, 100, 1))

    for i in range(300):
        packer.add_item(Item('boxL'+str(i), 20, 40, 20, 1))

    for i in range(10):
        packer.add_item(Item('boxU'+str(i), 40, 40, 20, 1))
    '''

    #packer.pack()

    packer.pack(bigger_first=False)
    positions = []
    sizes = []
    colors = []


    for b in packer.bins:
        print(":::::::::::", b.string())
        print("FITTED ITEMS 적재가능한 물품 정보 출력:")
        for item in b.items:
            print("====> ", item.string())
            x = float(item.position[0])
            y = float(item.position[1])
            z = float(item.position[2])
            positions.append((x,y,z))
            sizes.append((float(item.get_dimension()[0]), float(item.get_dimension()[1]), float(item.get_dimension()[2])))

        print("UNFITTED ITEMS 적재 불가능한 물품 정보 출력 :")
        for item in b.unfitted_items:
            print("====> ", item.string())
            

        print("***************************************************")
        print("***************************************************")



    def cuboid_data2(o, size=(1,1,1)):
        X = [[[0, 1, 0], [0, 0, 0], [1, 0, 0], [1, 1, 0]],
            [[0, 0, 0], [0, 0, 1], [1, 0, 1], [1, 0, 0]],
            [[1, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]],
            [[0, 0, 1], [0, 0, 0], [0, 1, 0], [0, 1, 1]],
            [[0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0]],
            [[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]]
        X = np.array(X).astype(float)
        for i in range(3):
            X[:,:,i] *= size[i]
        X += np.array(o)
        return X

    def plotCubeAt2(positions,sizes=None,colors=None, **kwargs):
        if not isinstance(colors,(list,np.ndarray)): colors=["C0"]*len(positions)
        if not isinstance(sizes,(list,np.ndarray)): sizes=[(1,1,1)]*len(positions)
        g = []
        for p,s,c in zip(positions,sizes,colors):
            g.append( cuboid_data2(p, size=s) )
        return Poly3DCollection(np.concatenate(g),  
                                facecolors=np.repeat(colors,6), **kwargs)
        

    colorList = ["crimson","limegreen","g","r","c","m","y","k"]

    for i in range(len(b.items)):
        f = random.randint(0,7)
        colors.append(colorList[f])

    print(colors)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #오류발생해서 수정함, gca() 메소드가 키워드 인수 projection 을 받지않음
    ax.set_aspect('auto')

    pc = plotCubeAt2(positions,sizes,colors=colors, edgecolor="k")
    ax.add_collection3d(pc)    

    ax.set_xlim([0,truckX])
    ax.set_ylim([0,truckY])
    ax.set_zlim([0,truckZ])

    plt.show()


