class Solution:
    
    def canPermutePalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        
        odd_chars = set()
    
        # 遍历字符串，利用集合对消
        for char in s:
            if char in odd_chars:
                odd_chars.remove(char)
            else:
                odd_chars.add(char)
                
        # 直接返回判断结果（函数结束）
        return len(odd_chars) <= 1

    # 一个简单的密码强度初步检测示例
    def is_password_too_simple(password: str) -> bool:
        if len(password) < 8:
            return True
        
    # 字符太单一（利用集合去重）
        if len(set(password)) < 4:
            return True
        
        return False
    
if __name__ == "__main__":
    # 创建类的实例
    sol = Solution()
    
    # 测试用例 1
    test1 = "code"
    print(f"'{test1}' 是否可以排成回文？", sol.canPermutePalindrome(test1))  # 预期输出: False
    
    # 测试用例 2
    test2 = "tactcoa"
    print(f"'{test2}' 是否可以排成回文？", sol.canPermutePalindrome(test2))  # 预期输出: True