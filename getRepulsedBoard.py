def getAttractedBoard(boardInfo, ourId, newCell):
    def getRepulsablePos(newCell):
        n = newCell[0]
        m= newCell[1]
        result ={}
        result['repulsablePos'] = []
        result['resultantPos'] = []
        possiblePos = [[n-1,m-1], [n-1,m], [n-1,m+1], [n,m-1], [n,m+1], [n+1,m-1], [n+1,m], [n+1,m+1]]
        resultantPossiblePos = [[n-2,m-2], [n-2,m], [n-2,m+2], [n,m-2], [n,m+2], [n+2,m+2], [n+2,m], [n+2,m+2]]
        i=0
        for pos in possiblePos:
            i+= 1
            if(pos[0] <0 or pos[0]>9 or pos[1] <0 or pos[1] >9):
                continue
            else:
                result['repulsablePos'].append(pos)
                result['resultantPos'].append(resultantPossiblePos[i-1])
        return result

    def getRepulsableCells(result, boardInfo, ourId):
        repulsableCells = []
        for pos in result['repulsablePos']:
            if(boardInfo[pos[0]][pos[1]] == ourId):
                repulsableCells.append(pos)
        return repulsableCells
    
    def getOutputCellPos(repulsableCells, result, newCell, boardInfo):
        repulseList ={}
        repulseList['existingPos'] = []
        repulseList['resultantPos'] = []
        for cell in repulsableCells:
            posIndex = result['repulsablePos'].index(cell)
            resPos = result['resultantPos'][posIndex]
            if ((not resPos in repulseList['resultantPos']) and boardInfo[resPos[0]][resPos[1]] == 0):
                repulseList['existingPos'].append(cell)
                repulseList['resultantPos'].append(resPos)
        return repulseList
    
    def getFinalBoardAfterAttraction (repulseList, boardInfo, ourID):
        for pos in repulseList['existingPos']:
            boardInfo[pos[0]][pos[1]] = 0
        for pos in repulseList['resultantPos']:
            boardInfo[pos[0]][pos[1]] = ourID
        return boardInfo

    attrPos = getRepulsablePos(newCell)
    attrCells = getRepulsableCells(attrPos, boardInfo, ourId)
    attrList = getOutputCellPos(attrCells, attrPos, newCell, boardInfo)
    resBoard = getFinalBoardAfterAttraction(attrList, boardInfo, ourId)
    return resBoard
