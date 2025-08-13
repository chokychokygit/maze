#!/usr/bin/env python3
"""
🗺️ Quick Maze Plotter - พลอตรูปเขาวงกตและเซฟลงเครื่องทันที
Quick maze visualization and auto-save script
"""

import os
import sys
from datetime import datetime
from maze_visualizer import quick_visualize, MazeVisualizer

def plot_maze_now(json_file=None):
    """
    พลอตรูปเขาวงกตและเซฟลงเครื่องทันที
    Plot maze and save to computer immediately
    """
    print("🚀 === QUICK MAZE PLOTTER ===")
    print("กำลังสร้างรูปเขาวงกตและเซฟลงเครื่อง...")
    print("Creating maze visualization and saving to computer...")
    
    # ใช้ quick_visualize function
    output_file = quick_visualize(json_file)
    
    if output_file:
        print(f"\n✅ สำเร็จ! ไฟล์รูปถูกเซฟแล้ว:")
        print(f"✅ Success! Image file saved:")
        print(f"📁 {os.path.abspath(output_file)}")
        
        # แสดงขนาดไฟล์
        file_size = os.path.getsize(output_file)
        print(f"📊 File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
        
        return output_file
    else:
        print("❌ ไม่สามารถสร้างรูปได้")
        print("❌ Failed to create visualization")
        return None

def plot_all_available():
    """
    พลอตทุกไฟล์ JSON ที่มี
    Plot all available JSON files
    """
    json_files = []
    
    # หาไฟล์ JSON ทั้งหมด
    for file in os.listdir('.'):
        if file.endswith('.json') and ('maze' in file.lower() or 'data' in file.lower()):
            json_files.append(file)
    
    if not json_files:
        print("❌ ไม่พบไฟล์ข้อมูลเขาวงกต")
        print("❌ No maze data files found")
        return
    
    print(f"📂 พบไฟล์ข้อมูล {len(json_files)} ไฟล์:")
    print(f"📂 Found {len(json_files)} data files:")
    
    results = []
    for json_file in json_files:
        print(f"\n🔄 กำลังประมวลผล: {json_file}")
        print(f"🔄 Processing: {json_file}")
        
        output_file = plot_maze_now(json_file)
        if output_file:
            results.append((json_file, output_file))
    
    print(f"\n🎉 เสร็จสิ้น! สร้างรูป {len(results)} รูป:")
    print(f"🎉 Complete! Created {len(results)} visualizations:")
    for json_file, output_file in results:
        print(f"   📊 {json_file} -> {output_file}")

def main():
    """Main function"""
    if len(sys.argv) > 1:
        # ถ้ามีการระบุไฟล์
        json_file = sys.argv[1]
        plot_maze_now(json_file)
    else:
        # ไม่ระบุไฟล์ - ให้ auto-detect
        print("🔍 Auto-detecting maze data files...")
        
        # ลองหาไฟล์มาตรฐาน
        standard_files = ['maze_data.json', 'test_maze_data.json']
        found_file = None
        
        for file in standard_files:
            if os.path.exists(file):
                found_file = file
                break
        
        if found_file:
            print(f"📂 Found: {found_file}")
            plot_maze_now(found_file)
        else:
            print("🔍 ไม่พบไฟล์มาตรฐาน ลองหาไฟล์อื่น...")
            print("🔍 Standard files not found, looking for other files...")
            plot_all_available()

if __name__ == '__main__':
    main()