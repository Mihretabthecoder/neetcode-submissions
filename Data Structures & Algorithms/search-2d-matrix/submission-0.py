class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r:
            m = int((r+l)/2)
            if matrix[m][0] > target:
                r = m-1
            elif matrix[m][-1] < target:
                l = m+1
            else:
                ll, rr = 0, len(matrix[m])-1
                while ll <= rr:
                    mm = int((ll + rr)/2)
                    if matrix[m][mm] > target:
                        rr = mm-1
                    elif matrix[m][mm] < target:
                        ll = mm+1
                    else:
                        return True
                return False
        return False