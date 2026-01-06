import time
import subprocess
import os
import sys
from datetime import datetime, timedelta

def run_checkin():
    print(f"[{datetime.now()}] 开始执行签到任务...")
    try:
        # 使用当前 Python 解释器执行主脚本
        result = subprocess.run([sys.executable, "leaflow_checkin.py"], capture_output=False)
        if result.returncode == 0:
            print(f"[{datetime.now()}] 签到任务执行完成")
        else:
            print(f"[{datetime.now()}] 签到任务执行失败，退出码: {result.returncode}")
    except Exception as e:
        print(f"[{datetime.now()}] 执行出错: {e}")

def main():
    print("Leaflow 自动签到调度器已启动")
    
    # 立即执行一次
    run_checkin()
    
    while True:
        # 计算距离下一次运行的时间（这里简单设置为每24小时运行一次）
        # 也可以根据需要修改为固定时间点运行
        interval = 24 * 60 * 60  # 24小时
        print(f"[{datetime.now()}] 进入休眠，{interval}秒后再次执行...")
        time.sleep(interval)
        run_checkin()

if __name__ == "__main__":
    main()
