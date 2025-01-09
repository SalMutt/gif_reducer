# GIF Size Reducer

Python script for reducing GIF file sizes while maintaining animation.

## Features

- Reduces GIF file size to specified target
- Supports animated GIFs
- Preserves animation timing
- Configurable target size

## Requirements

- Python 3.x
- Pillow library

## Installation

```bash
pip install Pillow
```

## Usage

```bash
python gif_reducer.py input.gif output.gif target_size_kb
```

Parameters:
- `input.gif`: Source GIF file
- `output.gif`: Output file name
- `target_size_kb`: Desired size in KB (optional, defaults to 128)

## Example

```bash
python gif_reducer.py large.gif small.gif 256
```

## Process

1. Scales image dimensions
2. Reduces color palette
3. Adjusts quality settings

## Limitations

- Quality reduction increases with smaller target sizes
- Minimum achievable size varies by input
- Processing time increases with animation frames

- Progress indicator implementation
- GUI interface
- Enhanced error reporting
- Backup functionality
