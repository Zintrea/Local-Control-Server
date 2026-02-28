import requests
import json
import time

# URL ของ MCP Server ที่เราเปิดไว้
SERVER_URL = "http://localhost:8001/sse"

def call_tool(name, arguments):
    # เลียนแบบการเรียกผ่าน MCP Protocol
    # ในกรณีทดสอบนี้ เราจะส่ง POST ไปที่ Endpoint โดยตรง (หรือใช้ mcp python client)
    # เพื่อความง่าย ผมจะส่งผ่าน requests ตรงๆ ไปที่ FastAPI
    url = f"http://localhost:8001/LocalControlServer/tools/{name}/call"
    try:
        response = requests.post(url, json=arguments)
        return response.json()
    except Exception as e:
        return f"Error: {e}"

print("🚀 กำลังเริ่มต้น AI Local Controller (Python Client)...")
print("-" * 50)

# 1. สั่งเปิด Notepad
print("📂 กำลังสั่งเปิด Notepad...")
call_tool("open_app", {"name": "notepad"})
time.sleep(2) # รอให้โปรแกรมเปิดขึ้นมา

# 2. สั่งพิมพ์ข้อความ
print("⌨️ กำลังพิมพ์ข้อความทักทาย...")
call_tool("type_text", {"text": "Hello from Zintrea AI Local Controller! This computer is now under my command. 🚀"})

print("-" * 50)
print("✅ ปฏิบัติการเสร็จสมบูรณ์! เชิญดูหน้าจอของคุณได้เลยครับ")
