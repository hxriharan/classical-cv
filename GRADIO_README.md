# 🖼️ Classical Computer Vision Gradio Webapp

A beautiful web interface for testing classical computer vision algorithms. Upload images and apply various algorithms with just a few clicks!

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Test the Setup
```bash
python test_app.py
```

### 3. Run the Webapp
```bash
python gradio_app.py
```

The app will open in your browser at `http://localhost:7860`

## 🎯 Features

### Image Processing
- **Gaussian Blur**: Smooths image using Gaussian kernel
- **Median Filter**: Removes salt-and-pepper noise
- **Bilateral Filter**: Edge-preserving smoothing
- **Sharpening**: Enhances image details
- **Histogram Equalization**: Improves contrast
- **Gamma Correction**: Adjusts brightness

### Edge Detection
- **Sobel**: Gradient-based edge detection
- **Canny**: Multi-stage edge detection
- **Harris Corner**: Corner detection
- **Hough Lines**: Line detection
- **Hough Circles**: Circle detection

### Feature Detection
- **SIFT**: Scale-invariant feature transform
- **SURF**: Speeded-up robust features (fallback to SIFT if not available)
- **ORB**: Oriented FAST and rotated BRIEF
- **BRIEF**: Binary robust independent elementary features (fallback to ORB if not available)

### Segmentation
- **Thresholding**: Binary segmentation
- **Watershed**: Region-based segmentation
- **SLIC**: Superpixel segmentation

### Object Detection
- **HOG**: Histogram of oriented gradients (pedestrian detection)
- **Haar Cascade**: Viola-Jones detection (face detection)
- **Template Matching**: Pattern matching

## 🎨 How to Use

1. **Upload an Image**: Click the upload area to select an image
2. **Choose Algorithm Category**: Select from Image Processing, Edge Detection, Feature Detection, Segmentation, or Object Detection
3. **Select Algorithm**: Choose the specific algorithm you want to test
4. **Process**: Click the "🚀 Process Image" button
5. **View Results**: See the processed image on the right side

## 📁 Project Structure

```
classical-cv/
├── gradio_app.py              # Main Gradio application
├── test_app.py                # Test script
├── requirements.txt           # Python dependencies
├── algorithms/               # Algorithm implementations
│   ├── __init__.py
│   ├── image_processing.py   # Image processing algorithms
│   ├── edge_detection.py     # Edge detection algorithms
│   ├── feature_detection.py  # Feature detection algorithms
│   ├── segmentation.py       # Segmentation algorithms
│   └── object_detection.py   # Object detection algorithms
└── examples/                 # Sample images (create this folder)
    ├── sample1.jpg
    ├── sample2.jpg
    └── sample3.jpg
```

## 🔧 Customization

### Adding New Algorithms

1. Add your algorithm function to the appropriate file in `algorithms/`
2. Import it in `gradio_app.py`
3. Add it to the corresponding processing function
4. Update the dropdown choices in the interface

### Example:
```python
# In algorithms/image_processing.py
def apply_custom_filter(img):
    # Your algorithm implementation
    return processed_img

# In gradio_app.py
from algorithms.image_processing import apply_custom_filter

# Add to process_image_processing function
elif algorithm == "Custom Filter":
    return apply_custom_filter(img)
```

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **OpenCV Contrib Features**: Some algorithms (SURF, BRIEF) require `opencv-contrib-python`
   ```bash
   pip install opencv-contrib-python
   ```

3. **Memory Issues**: Large images may cause memory problems. Consider resizing images before processing.

4. **Algorithm Not Working**: Check the console for error messages. Some algorithms may not work with all image types.

### Testing

Run the test script to verify everything works:
```bash
python test_app.py
```

## 🌟 Future Enhancements

- [ ] Add parameter sliders for algorithm tuning
- [ ] Support for video processing
- [ ] Batch processing multiple images
- [ ] Save/export processed images
- [ ] Add more advanced algorithms
- [ ] Real-time webcam processing
- [ ] Algorithm comparison side-by-side
- [ ] Performance metrics display

## 📝 License

This project is part of the Classical Computer Vision repository.

## 🤝 Contributing

Feel free to add new algorithms or improve the interface! Just follow the existing code structure and add appropriate tests. 