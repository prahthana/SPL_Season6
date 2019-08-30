import numpy
from copy import deepcopy

def getMaxSeq(boardInfo, id):
    def getRowSeq(boardInfo, id):
        eachPosLen = deepcopy(boardInfo)
        eachPosSeq = []
        i = 0
        j = 0
        for row in boardInfo:
            eachPosSeq.append([])
            j = 0
            for col in row:
                eachPosSeq[i].append([])
                if(not boardInfo[i][j] == id):
                    eachPosLen[i][j] = 0
                else:
                    eachPosLen[i][j] =1
                    if(j<9 and boardInfo[i][j+1] == id):
                        eachPosLen[i][j] = 2
                        eachPosSeq[i][j] = [[i,j],[i,j+1]]
                        if(j<8 and boardInfo[i][j+2] == id):
                            eachPosLen[i][j] = 3
                            eachPosSeq[i][j] = [[i,j],[i,j+1],[i,j+2]]
                            if(j<7 and boardInfo[i][j+3] == id):
                                eachPosLen[i][j] = 4
                                eachPosSeq[i][j] = [[i,j],[i,j+1],[i,j+2],[i,j+3]]
                j+=1
            i+=1
        maxLen = numpy.amax(eachPosLen)
        seqs =[]
        i=0
        for row in eachPosLen:
            j=0
            for col in row:
                if eachPosLen[i][j] == maxLen:
                    seqs.append(eachPosSeq[i][j])
                j+=1
            i+=1
        return maxLen, seqs

    def getForDiagSeq(boardInfo, id):
        eachPosLen = boardInfo.copy()
        eachPosSeq = []
        i = 0
        j = 0
        for row in boardInfo:
            eachPosSeq.append([])
            j = 0
            for col in row:
                eachPosSeq[i].append([])
                if(not boardInfo[i][j] == id):
                    eachPosLen[i][j] = 0
                else:
                    eachPosLen[i][j] =1
                    if(i<9 and j<9 and boardInfo[i+1][j+1] == id):
                        eachPosLen[i][j] = 2
                        eachPosSeq[i][j] = [[i,j],[i+1,j+1]]
                        if(i<8 and j<8 and boardInfo[i+2][j+2] == id):
                            eachPosLen[i][j] = 3
                            eachPosSeq[i][j] = [[i,j],[i+1,j+1],[i+2,j+2]]
                            if(i<7 and j<7 and boardInfo[i+3][j+3] == id):
                                eachPosLen[i][j] = 4
                                eachPosSeq[i][j] = [[i,j],[i+1,j+1],[i+2,j+2],[i+3,j+3]]
                j+=1
            i+=1
        maxLen = numpy.amax(eachPosLen)
        seqs =[]
        i=0
        for row in eachPosLen:
            j=0
            for col in row:
                if eachPosLen[i][j] == maxLen:
                    seqs.append(eachPosSeq[i][j])
                j+=1
            i+=1
        return maxLen, seqs

    def getBackDiagSeq(boardInfo, id):
        eachPosLen = boardInfo.copy()
        eachPosSeq = []
        i = 0
        j = 0
        for row in boardInfo:
            eachPosSeq.append([])
            j = 0
            for col in row:
                eachPosSeq[i].append([])
                if(not boardInfo[i][j] == id):
                    eachPosLen[i][j] = 0
                else:
                    eachPosLen[i][j] =1
                    if(i<9 and j>0 and boardInfo[i+1][j-1] == id):
                        eachPosLen[i][j] = 2
                        eachPosSeq[i][j] = [[i,j],[i+1,j-1]]
                        if(i<8 and j>1 and boardInfo[i+2][j-2] == id):
                            eachPosLen[i][j] = 3
                            eachPosSeq[i][j] = [[i,j],[i+1,j-1],[i+2,j-2]]
                            if(i<7 and j>2 and boardInfo[i+3][j-3] == id):
                                eachPosLen[i][j] = 4
                                eachPosSeq[i][j] = [[i,j],[i+1,j-1],[i+2,j-2],[i+3,j-3]]
                j+=1
            i+=1
        maxLen = numpy.amax(eachPosLen)
        seqs =[]
        i=0
        for row in eachPosLen:
            j=0
            for col in row:
                if eachPosLen[i][j] == maxLen:
                    seqs.append(eachPosSeq[i][j])
                j+=1
            i+=1
        return maxLen, seqs

    def getColSeq(boardInfo, id):
        eachPosLen = deepcopy(boardInfo)
        eachPosSeq = []
        i = 0
        j = 0
        for row in boardInfo:
            eachPosSeq.append([])
            j = 0
            for col in row:
                eachPosSeq[i].append([])
                if(not boardInfo[i][j] == id):
                    eachPosLen[i][j] = 0
                else:
                    eachPosLen[i][j] =1
                    if(i<9 and boardInfo[i+1][j] == id):
                        eachPosLen[i][j] = 2
                        eachPosSeq[i][j] = [[i,j],[i+1,j]]
                        if(i<8 and boardInfo[i+2][j] == id):
                            eachPosLen[i][j] = 3
                            eachPosSeq[i][j] = [[i,j],[i+1,j],[i+2,j]]
                            if(i<7 and boardInfo[i+3][j] == id):
                                eachPosLen[i][j] = 4
                                eachPosSeq[i][j] = [[i,j],[i,j+1],[i,j+2],[i,j+3]]
                j+=1
            i+=1
        maxLen = numpy.amax(eachPosLen)
        seqs =[]
        i=0
        for row in eachPosLen:
            j=0
            for col in row:
                if eachPosLen[i][j] == maxLen:
                    seqs.append(eachPosSeq[i][j])
                j+=1
            i+=1
        return maxLen, seqs
    max1,seq1 = getRowSeq(boardInfo, id)
    max2,seq2 = getColSeq(boardInfo, id)
    max3,seq3 = getForDiagSeq(boardInfo, id)
    max4,seq4 = getBackDiagSeq(boardInfo, id)
    maxVal = max(max1,max2,max3,max4)
    seqList = []
    if(max1 == maxVal):
        seqList.append(seq1)
    if(max2 == maxVal):
        seqList.append(seq2)
    if(max3 == maxVal):
        seqList.append(seq3)
    if(max4 == maxVal):
        seqList.append(seq4)
    return maxVal, seqList




