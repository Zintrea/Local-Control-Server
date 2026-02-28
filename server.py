import os
import subprocess
import pyautogui
from mcp.server.fastapi import Context
from mcp.server import Server
from fastapi import FastAPI
import uvicorn

# สร้าง MCP Server
app = FastAPI()
mcp_server = Server("LocalControlServer")

@mcp_server.tool()
async def open_app(name: str) -> str:
    """เปิดโปรแกรมในเครื่อง Windows ตามชื่อที่ระบุ"""
    try:
        # พยายามเปิดผ่านคำสั่ง start
        subprocess.Popen(f"start {name}", shell=True)
        return f"✅ สั่งเปิด {name} เรียบร้อยแล้ว"
    except Exception as e:
        return f"❌ เกิดข้อผิดพลาด: {str(e)}"

@mcp_server.tool()
async def type_text(text: str) -> str:
    """พิมพ์ข้อความลงในตำแหน่งที่เคอร์เซอร์อยู่"""
    try:
        pyautogui.write(text, interval=0.1)
        return f"✅ พิมพ์ข้อความ '{text}' เรียบร้อยแล้ว"
    except Exception as e:
        return f"❌ เกิดข้อผิดพลาด: {str(e)}"

@mcp_server.tool()
async def take_screenshot() -> str:
    """ถ่ายภาพหน้าจอและบันทึกไว้ในเครื่อง"""
    try:
        save_path = r"C:\Host\03 Projects\LocalControlServer\screenshot.png"
        screenshot = pyautogui.screenshot()
        screenshot.save(save_path)
        return f"✅ ถ่ายภาพหน้าจอและบันทึกไว้ที่ {save_path}"
    except Exception as e:
        return f"❌ เกิดข้อผิดพลาด: {str(e)}"

@mcp_server.tool()
async def system_control(action: str) -> str:
    """ควบคุมระบบ: 'mute', 'vol_up', 'vol_down'"""
    try:
        if action == "vol_up":
            pyautogui.press("volumeup")
        elif action == "vol_down":
            pyautogui.press("volumedown")
        elif action == "mute":
            pyautogui.press("volumemute")
        return f"✅ ดำเนินการ {action} เรียบร้อยแล้ว"
    except Exception as e:
        return f"❌ เกิดข้อผิดพลาด: {str(e)}"

# ติดตั้ง MCP บน FastAPI
mcp_server.install(app)

if __name__ == "__main__":
    print("🚀 MCP Local Control Server is RUNNING on http://localhost:8001")
    uvicorn.run(app, host="0.0.0.0", port=8001)
