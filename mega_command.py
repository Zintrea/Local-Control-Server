import pyautogui
import os
import subprocess
import time
import webbrowser

# 1. เปิด Notepad และพิมพ์ข้อความ
subprocess.Popen('notepad.exe')
time.sleep(1)
pyautogui.write('AI Mega Command is executing 5 tasks at once! ⚡\n', interval=0.05)

# 2. เปิดเครื่องคิดเลข
subprocess.Popen('calc.exe')

# 3. เปิด Chrome ไป YouTube
webbrowser.open('https://www.youtube.com')

# 4. ปลดล็อกเสียงและเพิ่มเสียง
pyautogui.press('volumemute') # สลับเป็นเปิดเสียง
for _ in range(10): pyautogui.press('volumeup')

# 5. ถ่ายภาพหน้าจอ
time.sleep(2)
save_path = r'C:\Host\03 Projects\LocalControlServer\mega_action.png'
screenshot = pyautogui.screenshot()
screenshot.save(save_path)

print('SUCCESS')
