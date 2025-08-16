# รายงานการทำงานของฟังก์ชัน "Save Node for Plotting"

## ภาพรวม (Overview)

ฟังก์ชัน `export_maze_data_to_json()` ในไฟล์ `please.py` เป็นส่วนสำคัญที่ทำหน้าที่บันทึกข้อมูลการสำรวจเขาวงกตทั้งหมดเพื่อใช้ในการสร้างภาพวาด (visualization) และการวิเคราะห์ข้อมูล

## วัตถุประสงค์ (Purpose)

1. **บันทึกข้อมูลการสำรวจ**: เก็บข้อมูลทุกโหนดที่หุ่นยนต์ได้สำรวจ
2. **สร้างไฟล์ JSON**: เพื่อใช้ในการสร้างภาพวาดและวิเคราะห์ข้อมูล
3. **ติดตามเส้นทาง**: บันทึกเส้นทางการเคลื่อนที่ของหุ่นยนต์
4. **เก็บข้อมูล Marker**: บันทึกข้อมูล marker ที่พบระหว่างการสำรวจ

## โครงสร้างข้อมูลที่บันทึก (Data Structure)

### 1. Metadata (ข้อมูลพื้นฐาน)
```json
{
  "metadata": {
    "export_timestamp": "เวลาที่บันทึก",
    "total_nodes_explored": "จำนวนโหนดทั้งหมด",
    "boundaries": {
      "min_x": "ขอบเขตต่ำสุดแกน X",
      "max_x": "ขอบเขตสูงสุดแกน X", 
      "min_y": "ขอบเขตต่ำสุดแกน Y",
      "max_y": "ขอบเขตสูงสุดแกน Y",
      "width": "ความกว้างแผนที่",
      "height": "ความสูงแผนที่"
    },
    "robot_start_position": [0, 0],
    "wall_threshold_cm": "ค่า threshold การตรวจจับกำแพง"
  }
}
```

### 2. Node Data (ข้อมูลโหนด)
สำหรับแต่ละโหนด จะบันทึกข้อมูลดังนี้:

```json
{
  "position": [x, y],
  "walls": {
    "north": true/false,
    "south": true/false, 
    "east": true/false,
    "west": true/false
  },
  "visited": true/false,
  "visit_count": "จำนวนครั้งที่เยี่ยมชม",
  "is_dead_end": true/false,
  "fully_scanned": true/false,
  "last_visited": "เวลาที่เยี่ยมชมล่าสุด",
  "neighbors": {
    "north": [x, y] หรือ null,
    "south": [x, y] หรือ null,
    "east": [x, y] หรือ null, 
    "west": [x, y] หรือ null
  },
  "unexplored_exits": ["ทิศทางที่ยังไม่ได้สำรวจ"],
  "explored_directions": ["ทิศทางที่สำรวจแล้ว"],
  "out_of_bounds_exits": ["ทิศทางที่อยู่นอกขอบเขต"],
  "out_of_bounds_count": "จำนวนทิศทางที่อยู่นอกขอบเขต"
}
```

### 3. Marker Data (ข้อมูล Marker)
```json
{
  "markers_found": {
    "front": ["marker_id1", "marker_id2"],
    "left": ["marker_id3"],
    "right": ["marker_id4"]
  },
  "marker_scan_results": {
    "front": {
      "marker_ids": ["marker_id1"],
      "distance": 25.5,
      "direction_name": "front",
      "angle": 0,
      "compass_direction": "เหนือ (N)",
      "timestamp": "2024-01-01T12:00:00",
      "found_red": true
    }
  },
  "has_markers": true/false
}
```

### 4. Robot Path (เส้นทางหุ่นยนต์)
```json
{
  "robot_path": [
    [0, 0],
    [1, 0], 
    [1, 1],
    [0, 1]
  ]
}
```

### 5. Walls Data (ข้อมูลกำแพง)
```json
{
  "walls": {
    "1,0,north": {
      "position": [1, 0],
      "direction": "north",
      "wall_type": "detected"
    }
  }
}
```

### 6. Grid Representation (การแสดงผลแบบตาราง)
```json
{
  "grid_representation": {
    "0,0": {
      "explored": true,
      "walls": {"north": false, "south": true, "east": false, "west": true},
      "visit_count": 2,
      "is_dead_end": false,
      "has_markers": true
    }
  }
}
```

## ขั้นตอนการทำงาน (Process Flow)

### 1. การเตรียมข้อมูล (Data Preparation)
```python
# คำนวณขอบเขตแผนที่
positions = [node.position for node in graph_mapper.nodes.values()]
min_x = min(pos[0] for pos in positions)
max_x = max(pos[0] for pos in positions)
min_y = min(pos[1] for pos in positions)
max_y = max(pos[1] for pos in positions)
```

### 2. การประมวลผลโหนด (Node Processing)
```python
for node_id, node in graph_mapper.nodes.items():
    # แปลงข้อมูลเป็น JSON-serializable
    node_data = {
        "position": list(node.position),
        "walls": convert_to_json_serializable(node.walls),
        # ... ข้อมูลอื่นๆ
    }
```

### 3. การสร้างเส้นทางหุ่นยนต์ (Robot Path Creation)
```python
# สร้างเส้นทางตามลำดับการเยี่ยมชม
visited_positions = [[0, 0]]  # เริ่มต้นที่จุด (0,0)
sorted_nodes = sorted(graph_mapper.nodes.values(), 
                     key=lambda n: (n.lastVisited, n.position))
```

### 4. การประมวลผลกำแพง (Wall Processing)
```python
for node in graph_mapper.nodes.values():
    x, y = node.position
    for direction, has_wall in node.walls.items():
        if has_wall:
            wall_key = f"{x},{y},{direction}"
            maze_data["walls"][wall_key] = {
                "position": [int(x), int(y)],
                "direction": str(direction),
                "wall_type": "detected"
            }
```

### 5. การสร้างตาราง (Grid Creation)
```python
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        node_id = f"{x},{y}"
        if node_id in graph_mapper.nodes:
            # โหนดที่สำรวจแล้ว
            grid_data = {
                "explored": True,
                "walls": node.walls,
                "visit_count": node.visitCount,
                "is_dead_end": node.isDeadEnd
            }
        else:
            # โหนดที่ยังไม่ได้สำรวจ
            grid_data = {
                "explored": False,
                "walls": {"north": True, "south": True, "east": True, "west": True},
                "visit_count": 0,
                "is_dead_end": False
            }
```

## การใช้งาน (Usage)

### 1. การเรียกใช้ฟังก์ชัน
```python
# บันทึกข้อมูลหลังจากสำรวจเสร็จ
export_maze_data_to_json(graph_mapper, "maze_data.json")

# บันทึกข้อมูลเมื่อเกิดข้อผิดพลาด
except KeyboardInterrupt:
    export_maze_data_to_json(graph_mapper, "maze_data.json")
```

### 2. ไฟล์ที่ได้
- **ชื่อไฟล์**: `maze_data.json`
- **รูปแบบ**: JSON format
- **ขนาด**: ขึ้นอยู่กับจำนวนโหนดที่สำรวจ

## ข้อดี (Advantages)

1. **ข้อมูลครบถ้วน**: บันทึกข้อมูลทุกด้านของการสำรวจ
2. **รูปแบบมาตรฐาน**: ใช้ JSON format ที่อ่านง่าย
3. **รองรับ Visualization**: สามารถใช้สร้างภาพวาดได้ทันที
4. **ข้อมูล Marker**: บันทึกข้อมูล marker ที่พบ
5. **การวิเคราะห์**: สามารถวิเคราะห์ประสิทธิภาพการสำรวจได้

## การประยุกต์ใช้ (Applications)

### 1. การสร้างภาพวาด (Visualization)
```python
# ใช้ข้อมูลจาก JSON เพื่อสร้างภาพวาด
import json
with open("maze_data.json", "r") as f:
    maze_data = json.load(f)
    
# สร้างภาพวาดจากข้อมูล
create_maze_visualization(maze_data)
```

### 2. การวิเคราะห์ประสิทธิภาพ (Performance Analysis)
```python
# วิเคราะห์ประสิทธิภาพการสำรวจ
total_nodes = maze_data["metadata"]["total_nodes_explored"]
path_length = len(maze_data["robot_path"])
efficiency = total_nodes / path_length
```

### 3. การเปรียบเทียบ (Comparison)
```python
# เปรียบเทียบผลการสำรวจหลายครั้ง
compare_exploration_results(["run1.json", "run2.json", "run3.json"])
```

## สรุป (Summary)

ฟังก์ชัน "Save Node for Plotting" เป็นส่วนสำคัญที่ทำให้ระบบการสำรวจเขาวงกตสมบูรณ์แบบ โดยการบันทึกข้อมูลทั้งหมดในรูปแบบ JSON ที่สามารถนำไปใช้ในการสร้างภาพวาด วิเคราะห์ประสิทธิภาพ และเปรียบเทียบผลการทำงานได้อย่างมีประสิทธิภาพ

ข้อมูลที่บันทึกครอบคลุมทุกด้านของการสำรวจ ตั้งแต่ข้อมูลพื้นฐานของโหนด เส้นทางการเคลื่อนที่ ข้อมูลกำแพง และข้อมูล marker ที่พบ ทำให้สามารถเข้าใจพฤติกรรมการสำรวจของหุ่นยนต์ได้อย่างละเอียด