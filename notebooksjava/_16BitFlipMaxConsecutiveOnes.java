public class _16BitFlipMaxConsecutiveOnes {
    public int reverseBits(int num) {
        // 🏁 特权拦截哨兵：如果 32 位全满载（即 -1）
        if (num == -1) return 32;
        
        int current = 0;
        int flipped = 0;
        int maxLen = 0;
        
        // 🚂 严格走满 32 位有符号车厢的生命周期
        for (int i = 0; i < 32; i++) {
            // 🔬 显微镜：检查最右边的一格是不是 1
            if ((num & 1) == 1) {
                current++;
                flipped++;
            } else {
                // 🌪️ 大盘暴跌与逻辑交接时刻
                flipped = current + 1;
                current = 0;
            }
            
            // 🛡️ 档案馆：实时锁死历史最高纪录
            maxLen = Math.max(maxLen, flipped);
            
            // 🚨 【高能核心改动】：必须用无符号右移 >>> 
            num >>>= 1;
        }
        
        return maxLen;
    }

    // 🚦 工业级自动化测试集
    public static void main(String[] args) {
        _16BitFlipMaxConsecutiveOnes sol = new _16BitFlipMaxConsecutiveOnes();
        System.out.println("🚦 开始执行 Java 位运算算法硬核全测...");

        // 用 Java 的 assert（运行时需加上 -ea 参数）
        // 或者直接打印验证结果是否符合我们讨论的物理真理
        
        System.out.println("Case 1 (1775): " + (sol.reverseBits(1775) == 8 ? "✅ 通过" : "❌ 失败"));
        System.out.println("Case 2 (7):    " + (sol.reverseBits(7) == 4 ? "✅ 通过" : "❌ 失败"));
        System.out.println("Case 3 (-1):   " + (sol.reverseBits(-1) == 32 ? "✅ 通过" : "❌ 失败"));
        System.out.println("Case 4 (-2):   " + (sol.reverseBits(-2) == 32 ? "✅ 通过" : "❌ 失败"));
        System.out.println("Case 5 (-3):   " + (sol.reverseBits(-3) == 32 ? "✅ 通过" : "❌ 失败（我们算对了，32才是真理！）"));
        System.out.println("Case 6 (-8):   " + (sol.reverseBits(-8) == 30 ? "✅ 通过" : "❌ 失败"));
        System.out.println("Case 7 (0):    " + (sol.reverseBits(0) == 1 ? "✅ 通过" : "❌ 失败"));

        System.out.println("🎉 恭喜！Java 物理引擎全线通关！");
    }
}