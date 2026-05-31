class TripleInOne:

    def __init__(self, stackSize: int):
        self.stack_size = stackSize
        self.array = [0] * (stackSize * 3)
        self.sizes = [0, 0, 0]

    def push(self, stackNum: int, value: int) -> str:
        # 如果当前栈满了，拒绝压入，返回友好提示
        if self.sizes[stackNum] == self.stack_size:
            msg = f"❌ 【エラー】{stackNum}号スタックは満杯です！値 [{value}] を追加できません。"
            print(msg)
            return msg
        
        # 计算绝对索引并存入
        abs_index = stackNum * self.stack_size + self.sizes[stackNum]
        self.array[abs_index] = value
        self.sizes[stackNum] += 1
        
        msg = f"📥 【Push成功】{stackNum}号スタックに値 [{value}] をプッシュしました。"
        print(msg)
        return msg

    def pop(self, stackNum: int) -> str:
        # 如果栈已经是空的，返回你指定的提示
        if self.sizes[stackNum] == 0:
            msg = f"⚠️ 【警告】{stackNum}号スタックは既に空です！ポップできません。"
            print(msg)
            return msg
        
        # 计数器减 1 并取出值
        self.sizes[stackNum] -= 1
        abs_index = stackNum * self.stack_size + self.sizes[stackNum]
        value = self.array[abs_index]
        
        msg = f"📤 【Pop成功】{stackNum}号スタックから要素 [{value}] を取り出しました。"
        print(msg)
        return msg

    def peek(self, stackNum: int) -> str:
        if self.sizes[stackNum] == 0:
            msg = f"👀 【Peek】{stackNum}号スタックは空なので、覗き見できる要素はありません。"
            print(msg)
            return msg
        
        abs_index = stackNum * self.stack_size + (self.sizes[stackNum] - 1)
        value = self.array[abs_index]
        
        msg = f"👀 【Peek】{stackNum}号スタックの先頭にある要素は [{value}] です。"
        print(msg)
        return msg

    def isEmpty(self, stackNum: int) -> str:
        if self.sizes[stackNum] == 0:
            msg = f"❓ 【状態確認】{stackNum}号スタックは「空」です。"
        else:
            msg = f"❓ 【状態確認】{stackNum}号スタックには現在 [{self.sizes[stackNum]}] 個の要素が入っています。"
        print(msg)
        return msg

if __name__ == "__main__":
    print("--- 🌟 三合一栈 交互日志开始 🌟 ---\n")
    
    # 1. 创建一个大小为 1 的三合一栈
    # 对应：["TripleInOne"] -> [[1]]
    obj = TripleInOne(1) 
    
    # 2. 往 0 号栈压入 1 -> 对应：["push"] -> [[0, 1]]
    obj.push(0, 1)
    
    # 3. 试图往 0 号栈再压入 2（应该失败，因为大小只有 1） -> 对应：["push"] -> [[0, 2]]
    obj.push(0, 2)
    
    # 4. 从 0 号栈弹出元素 -> 对应：["pop"] -> [[0]]
    obj.pop(0)
    
    # 5. 再次尝试从 0 号栈弹出元素（应该警告已空） -> 对应：["pop"] -> [[0]]
    obj.pop(0)
    
    # 6. 第三次尝试从 0 号栈弹出元素 -> 对应：["pop"] -> [[0]]
    obj.pop(0)
    
    # 7. 检查 0 号栈此时是不是空的 -> 对应：["isEmpty"] -> [[0]]
    obj.isEmpty(0)
    
    print("\n--- 🌟 运行结束，全流程可视化 🌟 ---")