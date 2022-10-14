class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res_lst = []

        def make_comb(candidates, target, make_arr):
            if sum(make_arr) == target:
                make_arr.sort()
                if make_arr not in res_lst:
                    res_lst.append(make_arr)
                return
            if sum(make_arr) > target:
                return
            for i in candidates:
                tmp = make_arr[:]
                tmp.append(i)
                make_comb(candidates, target, tmp)
        make_comb(candidates, target, [])
        return res_lst
