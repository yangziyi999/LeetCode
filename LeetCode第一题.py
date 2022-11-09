# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
class Solution(object):
    # 第一个方法是暴力解题 时间复杂度为n2，空间复杂度为n1
    #     执行结果：
    # 通过
    # 执行用时：1996 ms, 在所有 Python 提交中击败了29.71% 的用户
    # 内存消耗：13.8 MB, 在所有 Python 提交中击败了55.47% 的用户
    # 通过测试用例：57 / 57
    def twoSum(self, nums:list[int], target:int)->list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    # 第二种方式是使用哈希表，对于每一个输入的x，都会先查询哈希表内是否存在
    # target-x，然后将x插入哈希表,该方法时间复杂度和空间复杂度都为n
    # 执行用时：24 ms, 在所有 Python 提交中击败了76.48% 的用户
    # 内存消耗：13.5 MB, 在所有 Python 提交中击败了90.13% 的用户
    # 通过测试用例：57 / 57
    def twoSum2(self,nums:list[int],target:int)->list[int]:
        hashtable=dict()
        # 枚举，将每个hash表内的值都列出来 
        # 0，2
        # 1，7
        # 。。。
        for i,num in enumerate(nums):
            if target-num in hashtable:
                # 返回哈希表内位置与遍历到枚举的数
                return [hashtable[target-num],i]
            hashtable[nums[i]]=i
        return  []

number = [2,7,11,5]
target = 9
a = Solution()
print(a.twoSum2(number,target))