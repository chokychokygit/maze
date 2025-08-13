#!/usr/bin/env python3
"""
🔄 Interactive Maze Plotter
โปรแกรมจะถามหาชื่อไฟล์จากผู้ใช้
"""

import os
from maze_visualizer import quick_visualize

def list_json_files():
    """แสดงไฟล์ JSON ที่มีในโฟลเดอร์"""
    json_files = []
    for file in os.listdir('.'):
        if file.endswith('.json'):
            json_files.append(file)
    return json_files

def main():
    print("🔄 Interactive Maze Plotter")
    print("=" * 40)
    
    # แสดงไฟล์ JSON ที่มี
    json_files = list_json_files()
    if json_files:
        print("\n📂 ไฟล์ JSON ที่พบในโฟลเดอร์:")
        for i, file in enumerate(json_files, 1):
            print(f"   {i}. {file}")
    
    # ถามผู้ใช้
    print("\n🎯 เลือกวิธีการ:")
    print("1. พิมพ์ชื่อไฟล์")
    print("2. เลือกจากรายการ (ถ้ามี)")
    print("3. Auto-detect ไฟล์")
    
    choice = input("\nเลือก (1/2/3): ").strip()
    
    input_file = None
    
    if choice == "1":
        input_file = input("💾 ชื่อไฟล์ JSON: ").strip()
        
    elif choice == "2" and json_files:
        try:
            index = int(input(f"เลือกไฟล์ (1-{len(json_files)}): ")) - 1
            if 0 <= index < len(json_files):
                input_file = json_files[index]
            else:
                print("❌ หมายเลขไม่ถูกต้อง")
                return
        except ValueError:
            print("❌ กรุณาใส่หมายเลข")
            return
            
    elif choice == "3":
        print("🔍 กำลัง auto-detect ไฟล์...")
        input_file = None  # จะให้ quick_visualize หาเอง
        
    else:
        print("❌ ตัวเลือกไม่ถูกต้อง")
        return
    
    # สร้างรูป
    print(f"\n🎨 กำลังสร้างรูปจาก: {input_file if input_file else 'auto-detect'}")
    output_file = quick_visualize(input_file)
    
    if output_file:
        print(f"\n✅ สำเร็จ! ไฟล์รูปที่สร้าง:")
        print(f"📁 {os.path.abspath(output_file)}")
        
        # ถามว่าต้องการเปิดโฟลเดอร์ไหม
        open_folder = input("\n📂 เปิดโฟลเดอร์ที่เก็บไฟล์? (y/n): ").strip().lower()
        if open_folder in ['y', 'yes', 'ใช่']:
            try:
                import subprocess
                import platform
                
                folder_path = os.path.dirname(os.path.abspath(output_file))
                
                if platform.system() == "Windows":
                    subprocess.run(["explorer", folder_path])
                elif platform.system() == "Darwin":  # macOS
                    subprocess.run(["open", folder_path])
                else:  # Linux
                    subprocess.run(["xdg-open", folder_path])
                    
                print("📂 เปิดโฟลเดอร์แล้ว")
            except:
                print("❌ ไม่สามารถเปิดโฟลเดอร์ได้")
    else:
        print("❌ ไม่สามารถสร้างรูปได้")

if __name__ == '__main__':
    main()