#!/usr/bin/env python3
"""
ตัวอย่างการใช้งานระบบ Maze Visualization
Example usage of the Maze Visualization System
"""

import os
import subprocess
from maze_visualizer import MazeVisualizer

def main():
    print("🗺️ Maze Visualization System - Example Usage")
    print("=" * 50)
    
    # ตรวจสอบว่ามีไฟล์ข้อมูลหรือไม่
    test_file = "test_maze_data.json"
    output_file = "example_output.png"
    
    if not os.path.exists(test_file):
        print(f"❌ ไม่พบไฟล์ทดสอบ: {test_file}")
        print("กรุณารันโปรแกรมสำรวจเขาวงกตก่อน หรือใช้ไฟล์ test_maze_data.json")
        return
    
    try:
        # สร้าง visualizer
        print(f"📖 กำลังโหลดข้อมูลจาก: {test_file}")
        visualizer = MazeVisualizer(test_file)
        
        # สร้างภาพแสดงผล
        print("🎨 กำลังสร้างภาพแสดงผล...")
        visualizer.create_visualization(
            save_file=output_file,
            show_path=True,
            show_visit_counts=True,
            show_dead_ends=True
        )
        
        print("✅ เสร็จสิ้น!")
        print(f"📁 ไฟล์ภาพ: {output_file}")
        
        # แสดงข้อมูลสถิติ
        metadata = visualizer.maze_data['metadata']
        print("\n📊 สถิติการสำรวจ:")
        print(f"   🏃 จำนวนจุดที่สำรวจ: {metadata['total_nodes_explored']}")
        print(f"   🗺️ ขนาด grid: {metadata['boundaries']['width']}×{metadata['boundaries']['height']}")
        print(f"   🧱 กำแพงที่พบ: {len(visualizer.maze_data['walls'])}")
        print(f"   🛤️ ความยาวเส้นทาง: {len(visualizer.maze_data['robot_path'])} จุด")
        
        # คำแนะนำการใช้งาน
        print("\n💡 การใช้งานอื่นๆ:")
        print("   python3 maze_visualizer.py test_maze_data.json --save output.png")
        print("   python3 maze_visualizer.py test_maze_data.json --no-path")
        print("   python3 maze_visualizer.py test_maze_data.json --no-visits")
        print("   python3 maze_visualizer.py maze_data.json  # หลังจากรันหุ่นยนต์จริง")
        
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()