# sequence：これまでに出力したFibonacci数列を保持するリスト
# オブジェクトメソッド： 
# __init__：引数 first, secondをとり，sequence を [first, second] にする。
# next：次のFibonacci 数を出力する
# reset：sequence を 初期化する。引数として整数 first, second を与え sequence を 
# [first, second] にする。デフォルトの値は first=0, second=1

class Fibonacci(object):
    def __init__(self, first = 0, second = 1) -> None:
        self.sequence = [first, second]

    def next(self) -> int:
        next = sum(self.sequence)
        self.sequence[0] = self.sequence[1]
        self.sequence[1] = next 
        # self.sequence[0] <- self.sequence[1] <- temp
        return next
    
    def reset(self) -> None:
        self.sequence = [0, 1]

def main():    
    fib = Fibonacci(1, 1)   #[1, 1]
    print(fib.next())       #[1, 2]
    print(fib.next())       #[2, 3]
    print(fib.next())       #[3, 5]
    print(fib.next())       #[5, 8]
    print(fib.next())       #[8, 13]
    print(fib.next())       #[13, 21]
    print(fib.next())       #[21, 34]
    fib.reset()             #[0, 1]
    print(fib.next())       #[1, 1]
    print(fib.next())       #[1, 2]
    

if __name__ == '__main__':
    main()