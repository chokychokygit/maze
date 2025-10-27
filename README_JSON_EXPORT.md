# JSON Coordinate Export for Maze Visualization

## Overview
Added JSON coordinate saving functionality to the `new_pro` file to enable automatic maze visualization with the `maze_visualizer (1).py` script.

## Features Added

### 1. JSON Export Functions
- `convert_to_json_serializable()`: Converts numpy types and other non-serializable types to JSON-compatible formats
- `export_maze_data_to_json()`: Main export function that creates comprehensive maze data in JSON format
- `print_node_detailed_info()`: Helper function for detailed node information logging

### 2. Automatic Export Integration
- JSON export is automatically called at the end of exploration in `generate_exploration_report_absolute()`
- Creates `maze_data.json` file compatible with `maze_visualizer (1).py`
- Automatically attempts to create PNG visualization (no GIF animations as requested)

### 3. Data Structure
The exported JSON includes:
```json
{
  "metadata": {
    "export_timestamp": "ISO timestamp",
    "total_nodes_explored": "number of nodes",
    "boundaries": {
      "min_x": -1, "max_x": 1, "min_y": -1, "max_y": 1,
      "width": 3, "height": 3
    },
    "robot_start_position": [0, 0],
    "wall_threshold_cm": 50
  },
  "nodes": {
    "node_id": {
      "position": [x, y],
      "walls": {"north": bool, "south": bool, "east": bool, "west": bool},
      "visited": bool,
      "visit_count": int,
      "is_dead_end": bool,
      "neighbors": {...},
      "unexplored_exits": [...],
      "explored_directions": [...]
    }
  },
  "robot_path": [[x1, y1], [x2, y2], ...],
  "walls": {
    "x,y,direction": {
      "position": [x, y],
      "direction": "north|south|east|west",
      "wall_type": "detected"
    }
  },
  "grid_representation": {...},
  "node_analysis": {...}
}
```

## Usage

### 1. Run Exploration
```bash
python3 new_pro
```

### 2. Files Generated
- `maze_data.json`: Raw maze data for visualization
- `maze_visualization_auto.png`: Automatic PNG visualization (if maze_visualizer is available)

### 3. Manual Visualization
If automatic visualization fails, run manually:
```bash
python3 "maze_visualizer (1).py"
```

## Configuration

### Map Boundaries
The code is configured with a 3x3 grid (-1 to 1 in both X and Y):
```python
graph_mapper = GraphMapper(min_x=-1, min_y=-1, max_x=1, max_y=1)
```

### Output Format
- **PNG only**: No GIF animations as requested
- **High resolution**: 300 DPI output
- **Comprehensive data**: Includes walls, paths, visit counts, dead ends

## Key Improvements

1. **Compatibility**: JSON format matches exactly what `maze_visualizer (1).py` expects
2. **Automatic**: No manual intervention needed for basic visualization
3. **Robust**: Handles numpy types, missing attributes, and edge cases
4. **Informative**: Detailed logging of export process and statistics
5. **No GIF**: Only PNG output as requested, avoiding unnecessary time import requirements

## Requirements Maintained
- All existing robot control functionality preserved
- `import time` retained for essential `time.sleep()` calls in robot control
- JSON and OS imports added for file operations
- Boundary configuration added for controlled exploration area

## Visualization Features
When used with `maze_visualizer (1).py`, creates:
- Grid-based maze layout
- Wall visualization (thick dark lines)
- Robot path (red line with arrows)
- Start position marker (green circle)
- Dead end markers (orange triangles)
- Visit count indicators
- Legend and statistics