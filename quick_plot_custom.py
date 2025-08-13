#!/usr/bin/env python3
"""
🎯 Quick Plot with Custom File Path
แก้ไขชื่อไฟล์ในตัวแปรด้านล่างแล้วรัน
"""

from maze_visualizer import quick_visualize
import os

# ======================================
# 📝 แก้ไขชื่อไฟล์ตรงนี้
# ======================================
INPUT_FILE = "maze_data.json"          # <- เปลี่ยนชื่อไฟล์ตรงนี้
OUTPUT_NAME = None                     # <- หรือระบุชื่อไฟล์ output (None = auto)

# ======================================

def main():
    print("🎯 Quick Plot with Custom File")
    print(f"📂 Input file: {INPUT_FILE}")
    
    if not os.path.exists(INPUT_FILE):
        print(f"❌ ไม่พบไฟล์: {INPUT_FILE}")
        print("📝 แก้ไขชื่อไฟล์ในตัวแปร INPUT_FILE ด้านบน")
        return
    
    print("🎨 กำลังสร้างรูป...")
    output_file = quick_visualize(INPUT_FILE, output_name=OUTPUT_NAME)
    
    if output_file:
        print(f"\n✅ สำเร็จ! ไฟล์รูปที่สร้าง:")
        print(f"📁 {os.path.abspath(output_file)}")
    else:
        print("❌ ไม่สามารถสร้างรูปได้")

if __name__ == '__main__':
    main()