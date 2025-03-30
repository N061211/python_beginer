s = "hello world"
length = len(s)

assert length == 11

print("✅ Strings 正確！")


"""
📌 題目描述
給定一個 words 陣列，其中 除了某個字串以外，其他字串都出現兩次。
請找出這個 唯一只出現一次的字串，並回傳它。
"""
def single_string(words: list[str]) -> str:
    count = {}  # 建立字典來儲存每個字串的出現次數

    # 記錄每個字串出現的次數
    for word in words:
        count[word] = count.get(word, 0) + 1

    # 找出唯一只出現一次的字串
    for key, value in count.items():
        if value == 1:
            return key

# 測試範例
words1 = ["apple", "banana", "apple", "orange", "banana"]
words2 = ["hello", "world", "python", "hello", "python"]
words3 = ["one", "two", "two", "three", "three", "one", "unique"]

print(single_string(words1))  # 輸出: "orange"
print(single_string(words2))  # 輸出: "world"
print(single_string(words3))  # 輸出: "unique"

    
       