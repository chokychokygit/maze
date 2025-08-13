# Maze Exploration and Visualization System

## Overview
ระบบสำรวจและแสดงผลเขาวงกตสำหรับหุ่นยนต์ RoboMaster EP ที่สามารถบันทึกเส้นทางการเดิน กำแพง และข้อมูลการสำรวจแล้วนำมาแสดงผลเป็น grid visualization

## Files

### 1. `maze_plot` 
ไฟล์หลักของระบบสำรวจเขาวงกต:
- ควบคุมการเคลื่อนไหวของหุ่นยนต์
- สแกนหากำแพงโดยใช้ ToF sensor
- บันทึกข้อมูลเส้นทางและกำแพงในรูปแบบ graph
- **เพิ่มฟังก์ชัน `export_maze_data_to_json()`** เพื่อส่งออกข้อมูลเป็น JSON file

### 2. `maze_visualizer.py`
ไฟล์หลักสำหรับแสดงผลข้อมูลเขาวงกต:
- อ่านข้อมูลจาก JSON file
- สร้าง grid visualization แสดงเขาวงกต
- แสดงกำแพง เส้นทางหุ่นยนต์ จุดเริ่มต้น และจุดตัน
- **เซฟรูปอัตโนมัติ** ไม่ต้องระบุชื่อไฟล์

### 3. `plot_maze.py` 
สคริปต์ง่ายๆ สำหรับพลอตรูปทันที:
- รันคำสั่งเดียว พลอตและเซฟรูปเลย
- Auto-detect ไฟล์ข้อมูลเขาวงกต
- ใช้งานง่ายที่สุด

### 4. `test_maze_data.json`
ตัวอย่างข้อมูลเขาวงกตสำหรับทดสอบระบบ

## การใช้งาน

### 1. รันการสำรวจเขาวงกต
```bash
python3 maze_plot
```
- หุ่นยนต์จะสำรวจเขาวงกตอัตโนมัติ
- เมื่อเสร็จสิ้น ข้อมูลจะถูกบันทึกเป็น `maze_data.json`

### 2. แสดงผลเขาวงกต

#### 🚀 วิธีง่ายที่สุด - พลอตและเซฟทันที:
```bash
# รันเลยไม่ต้องใส่อะไร - จะ auto-detect ไฟล์และเซฟรูปทันที
python3 plot_maze.py

# หรือ
python3 maze_visualizer.py

# หรือ quick mode
python3 maze_visualizer.py --quick
```

#### 🎯 วิธีแบบละเอียด:
```bash
# ระบุไฟล์เฉพาะ
python3 maze_visualizer.py maze_data.json

# บันทึกเป็นไฟล์รูปภาพชื่อที่ต้องการ
python3 maze_visualizer.py maze_data.json --save my_maze.png

# ซ่อนเส้นทางหุ่นยนต์
python3 maze_visualizer.py maze_data.json --no-path

# ซ่อนจำนวนครั้งที่เยี่ยมชม
python3 maze_visualizer.py maze_data.json --no-visits

# ซ่อนจุดตัน
python3 maze_visualizer.py maze_data.json --no-dead-ends
```

### 3. ทดสอบด้วยข้อมูลตัวอย่าง
```bash
python3 maze_visualizer.py test_maze_data.json --save test_output.png
```

## ข้อมูลที่บันทึก

### JSON Structure
```json
{
  "metadata": {
    "export_timestamp": "...",
    "total_nodes_explored": 6,
    "boundaries": {...},
    "robot_start_position": [0, 0],
    "wall_threshold_cm": 25
  },
  "nodes": {
    "0,0": {
      "position": [0, 0],
      "walls": {"north": false, "south": false, "east": true, "west": false},
      "visited": true,
      "visit_count": 3,
      "is_dead_end": false,
      ...
    }
  },
  "robot_path": [[0,0], [0,1], [0,0], ...],
  "walls": {...},
  "grid_representation": {...}
}
```

### ข้อมูลที่แสดง
- **พื้นที่สำรวจแล้ว**: สีฟ้าอ่อน
- **พื้นที่ยังไม่สำรวจ**: สีเทาอ่อน  
- **กำแพง**: เส้นสีน้ำเงินเข้ม
- **เส้นทางหุ่นยนต์**: เส้นสีแดงพร้อมลูกศร
- **จุดเริ่มต้น**: วงกลมสีเขียว
- **จุดตัน**: สามเหลี่ยมสีส้ม
- **จำนวนครั้งที่เยี่ยมชม**: ตัวเลขในวงกลมขาว

## Dependencies
```bash
sudo apt install python3-matplotlib python3-numpy
```

## Features
- ✅ บันทึกข้อมูลเส้นทางและกำแพงเป็น JSON
- ✅ แสดงผล grid visualization แบบสวยงาม
- ✅ แสดงเส้นทางการเดินของหุ่นยนต์
- ✅ ระบุจุดตันและพื้นที่ที่เยี่ยมชมหลายครั้ง
- ✅ Command line interface ที่ใช้งานง่าย
- ✅ Export รูปภาพความละเอียดสูง
- ✅ **Auto-save รูปภาพโดยอัตโนมัติ**
- ✅ **Quick plot - รันคำสั่งเดียวได้รูปเลย**
- ✅ **Auto-detect ไฟล์ข้อมูล**

## 🚀 Quick Start (ใช้งานทันที)

```bash
# วิธีที่ 1: รันแล้วได้รูปเลย
python3 plot_maze.py

# วิธีที่ 2: ใช้ maze_visualizer
python3 maze_visualizer.py

# วิธีที่ 3: quick mode
python3 maze_visualizer.py --quick
```

**ไม่ต้องระบุไฟล์อะไร - ระบบจะหาให้เองและเซฟรูปให้อัตโนมัติ!** 🎯

## Technical Details
- ใช้ matplotlib สำหรับ visualization
- รองรับ absolute direction mapping (north/south/east/west)
- ข้อมูลกำแพงแยกตามทิศทางและตำแหน่ง
- Grid coordinate system ที่สอดคล้องกับการเคลื่อนไหวของหุ่นยนต์