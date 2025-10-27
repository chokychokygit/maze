# Maze Visualizer with JSON Configuration

This project contains a robot maze exploration script that now supports JSON configuration files for easy customization.

## Files

- `maze_visualizer.py` - Main robot control script with JSON configuration support
- `config.json` - Default configuration file
- `test_config.json` - Example alternative configuration
- `test_json_loading.py` - Test script to verify JSON loading functionality

## JSON Configuration Features

### ✅ Fixed: JSON File Loading
The script now properly loads JSON configuration files from the same directory as the script. This includes:

1. **Automatic path resolution** - Always looks for JSON files in the script's directory
2. **Error handling** - Falls back to default configuration if JSON file is missing or invalid
3. **Command line support** - Can specify custom JSON file as command line argument
4. **Data export** - Saves exploration results to JSON files for analysis

### Configuration Structure

```json
{
  "robot_settings": {
    "wall_threshold": 30,        // Distance threshold for wall detection (cm)
    "max_nodes": 49,             // Maximum nodes to explore
    "gimbal_speed": 100,         // Gimbal movement speed
    "movement_speed": 50         // Robot movement speed
  },
  "map_boundaries": {
    "min_x": -1,                 // Minimum X coordinate
    "min_y": -1,                 // Minimum Y coordinate  
    "max_x": 1,                  // Maximum X coordinate
    "max_y": 1                   // Maximum Y coordinate
  },
  "exploration_settings": {
    "priority_order": ["left", "front", "right", "back"],  // Movement priority
    "enable_caching": true,      // Enable sensor data caching
    "scan_delay": 0.3           // Delay between scans (seconds)
  },
  "debug_settings": {
    "verbose_logging": true,     // Enable detailed logging
    "show_boundary_info": true,  // Show boundary information
    "show_sensor_readings": true // Show sensor readings
  }
}
```

## Usage

### Basic Usage (uses config.json)
```bash
python3 maze_visualizer.py
```

### Custom Configuration File
```bash
python3 maze_visualizer.py test_config.json
python3 maze_visualizer.py my_custom_config.json
```

### Test JSON Loading
```bash
python3 test_json_loading.py
python3 test_json_loading.py test_config.json
```

## Features

- 🔧 **Flexible Configuration**: Easy to modify robot behavior without changing code
- 📁 **Same-folder Loading**: JSON files are loaded from the script's directory
- 🛡️ **Error Handling**: Graceful fallback to defaults if JSON is invalid
- 💾 **Data Export**: Exploration results saved to timestamped JSON files
- 🎯 **Command Line Support**: Specify custom config files as arguments
- 🧪 **Testing**: Included test script to verify functionality

## Example Configurations

### Small Map (test_config.json)
- 5x5 grid boundaries
- Faster movement, lower wall threshold
- Different exploration priority (front-first)

### Default Map (config.json)  
- 3x3 grid boundaries
- Standard settings for normal exploration
- Left-first exploration priority

## Data Export

The script automatically saves exploration data to JSON files with timestamps:
- Format: `exploration_data_YYYYMMDD_HHMMSS.json`
- Contains: Node positions, walls, sensor readings, exploration status
- Location: Same directory as the script