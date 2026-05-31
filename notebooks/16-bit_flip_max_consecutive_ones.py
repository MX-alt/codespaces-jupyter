class Solution:
    def reverseBits(self, num: int) -> int:
        num = num & 0xffffffff
        if num == 0xffffffff: return 32
        current,flipped, max_len = 0, 0, 0
        
        for _ in range(32):
            if (num & 1) == 1:
                current += 1
                flipped += 1
            else:
                flipped = current + 1
                current = 0           
            max_len = max(max_len, flipped)
            num >>= 1
        return max_len

if __name__ == "__main__":
    sol = Solution()
    
    print("🚦 开始执行位运算算法硬核全测...")
    
    # -------------------------------------------------------------
    # Case 1: 题目经典正数案例（1775 -> 二进制 ...11011101111）
    # 物理焊接后：3 + 1 + 4 = 8
    assert sol.reverseBits(1775) == 8, "测试失败：1775 应该输出 8"
    
    # Case 2: 题目经典正数案例（7 -> 二进制 ...0111）
    # 物理扩建后：3 + 1 = 4
    assert sol.reverseBits(7) == 4, "测试失败：7 应该输出 4"
    
    # -------------------------------------------------------------
    # Case 3: 极端边界哨兵（-1 -> 32位全1）
    # 物理天花板：直接触发 Guard Clause 吐出 32
    assert sol.reverseBits(-1) == 32, "测试失败：-1 应该输出 32"
    
    # Case 4: 闷骚负数断点（-2 -> 31个1 + 1个0）
    # 物理焊接后：31 + 1 = 32
    assert sol.reverseBits(-2) == 32, "测试失败：-2 应该输出 32"
    
    # Case 5: 刚才发生大震荡的负数（-3 -> 30个1 + 1个0 + 1个1）
    # 物理焊接后：30 + 1 + 1 = 31（座位被挤占，大部队缩水）
    assert sol.reverseBits(-3) == 32, "测试失败：-3 应该输出 32"
    
    # -------------------------------------------------------------
    # Case 6: 纯净零点（0 -> 32位全0）
    # 物理特权：随便把哪个 0 涂成 1，最长也只能拼出长度为 1 的铁轨
    assert sol.reverseBits(0) == 1, "测试失败：0 应该输出 1"
    
    print("✅ 恭喜，所有断言物理通关！代码质量稳如磐石。")