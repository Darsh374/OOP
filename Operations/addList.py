class AddList:
    @staticmethod
    def sumList(augend, addend=None):
        if isinstance(augend, list):
            return AddList.sumList(augend)
        return augend + addend

    @staticmethod
    def sumLists(valueList):
        result = 0
        for value in valueList:
            result = AddList.sumList(result, value)

        return result
