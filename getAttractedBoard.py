def getAttractedBoard(boardInfo, oppId, newCell):
    def getAttractablePos(newCell):
        n = newCell[0]
        m= newCell[1]
        result ={}
        result['attractablePos'] = []
        result['resultantPos'] = []
        possiblePos = [[n-2,m-2], [n-2,m-1], [n-2,m], [n-2,m+1], [n-2,m+2], [n-1,m-2], [n-1,m+2], [n,m-2], [n,m+2], [n+1,m-2], [n+1, m+2], [n+2,m-2], [n+2,m-1], [n+2,m], [n+2,m+1], [n+2,m+2]]
        resultantPossiblePos = [[n-1,m-1], [n-1,m], [n-1,m], [n-1,m], [n-1,m+1], [n,m-1], [n,m+1], [n,m-1], [n,m+1], [n,m-1], [n, m+1], [n+1,m-1], [n+1,m], [n+1,m], [n+1,m], [n+1,m+1]]
        i=0
        for pos in possiblePos:
            i+= 1
            if(pos[0] <0 or pos[0]>9 or pos[1] <0 or pos[1] >9):
                continue
            else:
                result['attractablePos'].append(pos)
                result['resultantPos'].append(resultantPossiblePos[i-1])
        return result

    def getAttractableCells(result, boardInfo, oppId):
        attractableCells = []
        for pos in result['attractablePos']:
            if(boardInfo[pos[0]][pos[1]] == oppId):
                attractableCells.append(pos)
        return attractableCells
    
    def getOutputCellPos(attractableCells, result, newCell, boardInfo):
        attractList ={}
        attractList['existingPos'] = []
        attractList['resultantPos'] = []
        for cell in attractableCells:
            posIndex = result['attractablePos'].index(cell)
            resPos = result['resultantPos'][posIndex]
            if ((not resPos in attractList['resultantPos']) and boardInfo[resPos[0]][resPos[1]] == 0):
                attractList['existingPos'].append(cell)
                attractList['resultantPos'].append(resPos)
        return attractList
    
    def getFinalBoardAfterAttraction (attractList, boardInfo, oppId):
        for pos in attractList['existingPos']:
            boardInfo[pos[0]][pos[1]] = 0
        for pos in attractList['resultantPos']:
            boardInfo[pos[0]][pos[1]] = oppId
        return boardInfo

    attrPos = getAttractablePos(newCell)
    attrCells = getAttractableCells(attrPos, boardInfo, oppId)
    attrList = getOutputCellPos(attrCells, attrPos, newCell, boardInfo)
    resBoard = getFinalBoardAfterAttraction(attrList, boardInfo, oppId)
    return resBoard
