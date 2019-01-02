#!/usr/bin/python3
# 編譯 Telegram Bot Framework 全平台的 Python 程式
# author: pan93412, 2019.

import os
import sys

support_platform = {
    "darwin": {
        "amd64"
    }, # macOS
    "linux": {
        "amd64",
        "386" # 32-bit
    }
}

def build(source, target, prefix, system, arch):
    '''
    編譯 Go 程式的指令，預設是編譯 source 底下的所有以
    .go 做結尾的來源檔。
    
    source: 編譯來源目錄
    target: 編譯目標目錄
    prefix: 檔名前置詞
    system: 要編譯的系統 (GOOS)
    arch:   要編譯的平台 (GOARCH)
    '''
    # {0}=system {1}=arch {2}=source {3}=prefix {4}=target
    os.system("GOOS={0} GOARCH={1} go build -o {4}/{3}_{0}_{1}.out {2}/*.go".format(system, arch, source, prefix, target))

def build_all(prefix, source, target):
    '''
    編譯整個 TGBotFramework，讀取 support_platform
    字典的內容。
    '''
    print("開始編譯程序。")
    for GOOS in support_platform:
        for GOARCH in support_platform[GOOS]:
            print("正在編譯 {0} {1}……".format(GOOS, GOARCH), end="", flush=True)
            build(source, target, prefix, GOOS, GOARCH)
            print("\r編譯 {0} {1} 完成。檔名：{2}_{0}_{1}.out   ".format(GOOS, GOARCH, prefix), flush=True) # 後面空白是為洗掉上行文字
    print("全部編譯完成。")

def main():
    if len(sys.argv) != 3:
        print("使用方法：python3 {filename} (go 檔案存放之目錄) (編譯檔存放目錄)".format(filename = sys.argv[0]))
        exit(1)
    else:
        build_all("TGBF", sys.argv[1], sys.argv[2])
        exit(0)

if __name__ == "__main__":
    main()
