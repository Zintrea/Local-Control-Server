import os
import subprocess
import pyautogui
from mcp.server.fastapi import Context
from mcp.server import Server
from fastapi import FastAPI
import uvicorn
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

# สร้าง MCP Server
app = FastAPI()
mcp_server = Server("LocalControlServer")

@mcp_server.tool()
async def open_app(name: str) -> str:
    """เปิดโปรแกรมในเครื่อง Windows ตามชื่อที่ระบุ"""
    try:
        subprocess.Popen(f"start {name}", shell=True)
        return f"✅ สั่งเปิด {name} เรียบร้อยแล้ว"
    except Exception as e:
        return f"❌ เกิดข้อผิดพลาด: {str(e)}"

@mcp_server.tool()
async def set_volume(level: int) -> str:
    """ตั้งค่าระดับเสียงลำโพง (0 - 100)"""
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        
        # ปรับระดับเสียง (0.0 ถึง 1.0)
        volume.SetMasterVolumeLevelScalar(level / 100, None)
        return f"✅ ปรับระดับเสียงเป็น {level}% เรียบร้อยแล้ว"
    except Exception as e:
        return f"❌ เกิดข้อผิดพลาด: {str(e)}"

@mcp_server.tool()
async def type_text(text: str) -> str:
    """พิมพ์ข้อความลงในตำแหน่งที่เคอร์เซอร์อยู่"""
    try:
        pyautogui.write(text, interval=0.1)
        return f"✅ พิมพ์ข้อความเรียบร้อยแล้ว"
    except Exception as e:
        return f"❌ เกิดข้อผิดพลาด: {str(e)}"

@mcp_server.tool()
async def take_screenshot() -> str:
    """ถ่ายภาพหน้าจอ"""
    try:
        save_path = r"C:\Host\03 Projects\LocalControlServer\screenshot.png"
        screenshot = pyautogui.screenshot()
        screenshot.save(save_path)
        return f"✅ ถ่ายภาพหน้าจอแล้ว"
    except Exception as e:
        return f"❌ เกิดข้อผิดพลาด: {str(e)}"

# ติดตั้ง MCP บน FastAPI
mcp_server.install(app)

if __name__ == "__main__":
    print("🚀 MCP Local Control Server (Upgraded) is RUNNING on http://localhost:8001")
    uvicorn.run(app, host="0.0.0.0", port=8001)
