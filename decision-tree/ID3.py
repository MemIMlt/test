from math import log
import operator
import tree_plotter


def CreatDataSet():
    '''创建样本数据'''
    # 色泽： 0 青绿   1 乌黑   2 浅白
    # 根蒂： 0 蜷缩   1 稍蜷   2 硬挺
    # 敲声： 0 浊响   1 沉闷   2 清脆
    # 纹理： 0 清晰   1 稍糊   2 模糊
    # 脐部： 0 凹陷   1 稍凹   2 平坦
    # 触感： 0 硬滑   1 软沾
    dataset = [[0, 0, 0, 0, 0, 0, 'yes'],
               [1, 0, 1, 0, 0, 0, 'yes'],
               [1, 0, 0, 0, 0, 0, 'yes'],
               [0, 0, 1, 0, 0, 0, 'yes'],
               [2, 0, 0, 0, 0, 0, 'yes'],
               [0, 1, 0, 0, 1, 1, 'yes'],
               [1, 1, 0, 1, 1, 1, 'yes'],
               [1, 1, 0, 0, 1, 0, 'yes'],
               [1, 1, 1, 1, 1, 0, 'no'],
               [0, 2, 2, 0, 2, 1, 'no'],
               [2, 2, 2, 2, 2, 0, 'no'],
               [2, 0, 0, 2, 2, 1, 'no'],
               [0, 1, 0, 1, 0, 0, 'no'],
               [2, 1, 1, 1, 0, 0, 'no'],
               [1, 1, 0, 0, 1, 1, 'no'],
               [2, 0, 0, 2, 2, 0, 'no'],
               [0, 0, 1, 1, 1, 0, 'no']]
    label = ['seze', 'gendi', 'qiaoshen', 'wenli', 'qibu', 'chugan']
    return dataset, label


def majorityCnt(classlist):
    '''统计每种类别出现的次数，并返回出现次数最多的类别'''
    classcount = {}
    for num in classlist:
        if num not in classcount.keys():
            classcount[num] = 0
        classcount[num] += 1
    # 对值排序,排序之后变成了列表
    sort_classcount = sorted(classcount.items(), key=operator.itemgetter(1), reverse=True)
    return sort_classcount[0][0]


def SplitDataSet(dataset, axis, value):
    '''将训练集和按获得的最优属性进行划分'''
    newdataset = []
    for temp in dataset:
        if temp[axis] == value:
            newfeat = temp[:axis]
            newfeat.extend(temp[axis + 1:])
            newdataset.append(newfeat)
    return newdataset


def GetEntropy(dataset):
    '''获取某个属性的熵值'''
    sumentries = len(dataset)
    labcount = {}
    for temp in dataset:
        nowlab = temp[-1]
        if nowlab not in labcount.keys():
            labcount[nowlab] = 0
        labcount[nowlab] += 1
    # 计算熵
    ent = 0.0
    for key in labcount:
        prob = float(labcount[key]) / sumentries
        ent -= prob * log(prob, 2)
    return ent


def GetBestFeat(dataset):
    '''获取最优属性编号'''
    entropy = GetEntropy(dataset)
    numfeat = len(dataset[0]) - 1
    bestinf = 0.0  # 最大信息增益
    bestfeat = 0  # 最优属性编号

    for i in range(0, numfeat):
        featlist = [example[i] for example in dataset]
        uniqueval = set(featlist)
        tempentropy = 0.0
        for value in uniqueval:
            subdataset = SplitDataSet(dataset, i, value)
            subentropy = len(subdataset) / float(len(dataset))
            tempentropy += subentropy * GetEntropy(subdataset)
        infotemp = entropy - tempentropy
        if (infotemp > bestinf):
            bestinf = infotemp
            bestfeat = i
    return bestfeat


def CreatTree(dataset, label):
    '''创建决策树'''
    # 类别列表 ['yes','no'......]
    class_list = [sample[-1] for sample in dataset]
    # 类别相同直接返回
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    # 属性集为空，直接返回最多的类
    if len(dataset[0]) == 1:
        return majorityCnt(class_list)
    # 开始按照熵值选择最优划分属性
    bestfeat = GetBestFeat(dataset)  # 获取属性编号
    bestfeatlabel = label[bestfeat]  # 记录该属性
    del (label[bestfeat])  # 删除该属性，不会再以它进行划分
    my_tree = {bestfeatlabel: {}}
    # 根据最优属性建树
    featvalue = [example[bestfeat] for example in dataset]
    uniqueval = set(featvalue)  # set没有重复值
    """   但是下面的for循环只能获得该属性在当前子集中存在的值(意思是在总集中存在，但子集中没有)，
       不存在的属性值就不会新建分支，没有相关的子树或者叶子节点，泛化能力极差   """

    '''   要想解决这个问题只能通过在获得测试集的时候对它进行一次遍历，将每个属性存在的值种类记录下来   '''

    '''   现在有一种新想法，我们建立决策树的最终目的是为了让它能够判别西瓜的好坏，包括我们在样本中从来没有
        出现过的情况，也就是所谓的泛化能力。于是，我们可以在每个节点根据属性值划分的分支中加上一个“其它”属
        性值的叶子节点，它所属的瓜的种类标记为其父节点中种类最多的那一种   '''

    '''   上述的方法其实并未改变ID3算法泛化能力差的本质，但其思想可以运用在其它更优的算法当中'''
    for value in uniqueval:
        # 构建子集，递归
        sublabel = label[:]
        subdataset = SplitDataSet(dataset, bestfeat, value)
        my_tree[bestfeatlabel][value] = CreatTree(subdataset, sublabel)

    return my_tree


def classify(tree, label, testvec):
    '''测试代码'''
    rootfeat = list(tree.keys())[0]
    nexttree = tree[rootfeat]
    featid = label.index(rootfeat)
    for key in nexttree.keys():
        if testvec[featid] == key:
            if type(nexttree[key]).__name__ == 'dict':
                classlabel = classify(nexttree[key], label, testvec)
            else:
                classlabel = nexttree[key]
    return classlabel


def main():
    dataset, label = CreatDataSet()
    label_temp = label[:]
    decision_tree = CreatTree(dataset, label_temp)
    testvec = [2, 2, 1, 0, 0, 1]
    print(classify(decision_tree, label, testvec))
    tree_plotter.create_plot(decision_tree)


if __name__ == '__main__':
    main()
