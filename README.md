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

## Technical Notes

- Uses Pillow for image processing
- Implements progressive optimization
- Maintains animation frame timing
- Temporary files cleaned after processing

## Development

### Setup
1. Clone repository
2. Install requirements
3. Run using Python 3.x

### Testing
Test with various GIF sizes and target parameters.

## Error Handling

- Validates input file existence
- Reports optimization progress
- Notifies if target size unachievable

## Future Development

- Progress indicator implementation
- GUI interface
- Enhanced error reporting
- Backup functionality
