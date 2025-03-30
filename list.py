

"""
    延伸例題：
📌 題目描述
給定一個 nums 陣列，其中 除了某個數字以外，其他數字都出現兩次。請找出這個 唯一只出現一次的數字。

範例：
# 輸入：
nums = [4, 1, 2, 1, 2]
# 輸出：
4

"""
def single_number(nums: list[int]) -> int:
    count = {}  # 用來儲存每個數字出現的次數

    # 記錄數字出現次數
    for num in nums:
        count[num] = count.get(num, 0) + 1

    # 找到出現一次的數字
    for key, value in count.items():
        if value == 1:
            return key

# 測試範例
nums1 = [4, 1, 2, 1, 2]
nums2 = [2, 2, 3, 3, 7]
nums3 = [0, 1, 0, 1, 99]

print(single_number(nums1))  # 輸出: 4
print(single_number(nums2))  # 輸出: 7
print(single_number(nums3))  # 輸出: 99





