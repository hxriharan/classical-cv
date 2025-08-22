# Classical Computer Vision

A comprehensive repository containing implementations of classical computer vision algorithms, research papers, and an interactive web interface for testing these algorithms on custom images.

## Overview

This project serves as both a learning resource and a practical toolkit for classical computer vision. It includes:

- **Algorithm Implementations**: Complete implementations of fundamental CV algorithms
- **Interactive Web Interface**: Gradio-based UI for testing algorithms on uploaded images
- **Research Papers**: Collection of seminal papers in computer vision
- **Educational Content**: Organized tutorials covering all major CV topics

## Quick Start

### Prerequisites

- Python 3.8+
- OpenCV 4.8+
- Gradio 4.0+

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Classical-Computer-Vision-Opensource.git
   cd Classical-Computer-Vision-Opensource/classical-cv
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the web interface**
   ```bash
   python gradio_app.py
   ```

The application will be available at the URL shown in the terminal output (typically `http://localhost:7860` or similar)

## Features

### Interactive Web Interface

Upload images and test various computer vision algorithms through an intuitive web interface:

- **Image Processing**: Gaussian blur, median filter, bilateral filter, sharpening, histogram equalization, gamma correction
- **Edge Detection**: Sobel, Canny, Harris corner detection, Hough transforms
- **Feature Detection**: SIFT, SURF, ORB, BRIEF
- **Segmentation**: Thresholding, watershed, SLIC superpixels
- **Object Detection**: HOG, Haar cascades, template matching

### Algorithm Categories

#### 1. Image Fundamentals
- Pixel intensity and bit-depth
- Color spaces (RGB, HSV, YCbCr, Lab)
- Image formats and representations
- Sampling and quantization
- Image histograms

#### 2. Image Preprocessing
- Noise types and filtering
- Mean, median, Gaussian, and bilateral filters
- Sharpening and high-pass filters
- Histogram equalization and contrast enhancement
- Gamma correction

#### 3. Edge and Feature Detection
- Gradient operators (Sobel, Prewitt, Scharr)
- Canny edge detector
- Laplacian of Gaussian
- Harris and Shi-Tomasi corner detection
- Hough transforms for lines and circles
- Difference of Gaussians

#### 4. Feature Descriptors and Matching
- SIFT (Scale-Invariant Feature Transform)
- SURF (Speeded-Up Robust Features)
- ORB (Oriented FAST and Rotated BRIEF)
- BRIEF, FREAK, AKAZE
- Descriptor matching algorithms
- RANSAC for robust estimation

#### 5. Image Segmentation
- Thresholding (global, adaptive, Otsu's)
- Morphological operations
- Connected components analysis
- Watershed segmentation
- Graph-based segmentation
- Region growing and splitting/merging
- Superpixel algorithms (SLIC)

#### 6. Object Detection and Recognition
- Template matching
- Haar cascades
- HOG (Histogram of Oriented Gradients)
- Sliding window methods
- Contour analysis
- Shape descriptors

#### 7. Motion and Optical Flow
- Frame differencing
- Background subtraction
- Optical flow algorithms
- Block matching
- Tracking algorithms (Kalman filter, particle filter, meanshift)

#### 8. Camera Geometry and Calibration
- Pinhole camera model
- Intrinsic and extrinsic parameters
- Camera calibration
- Lens distortion correction
- Homographies and epipolar geometry

#### 9. Stereo Vision and Depth Estimation
- Stereo matching algorithms
- Disparity map computation
- Triangulation
- Stereo rectification
- Depth estimation

#### 10. Structure from Motion and 3D Vision
- Feature tracking across frames
- Bundle adjustment
- Point cloud generation
- Multi-view geometry
- Visual odometry

#### 11. Image Registration and Stitching
- Image alignment
- Feature-based registration
- Panorama stitching
- Homography estimation
- Blending techniques

## Project Structure

```
classical-cv/
├── gradio_app.py              # Main Gradio web application
├── test_app.py                # Testing script for dependencies
├── requirements.txt           # Python dependencies
├── algorithms/               # Algorithm implementations
│   ├── __init__.py
│   ├── image_processing.py   # Image processing algorithms
│   ├── edge_detection.py     # Edge detection algorithms
│   ├── feature_detection.py  # Feature detection algorithms
│   ├── segmentation.py       # Segmentation algorithms
│   └── object_detection.py   # Object detection algorithms
├── 1_Image_basics/          # Image fundamentals tutorials
├── 2_Image_processing/      # Image processing tutorials
├── 3_edge_detection/        # Edge detection tutorials
├── 4_feature_detection/     # Feature detection tutorials
├── 5_segmentation/          # Segmentation tutorials
├── 6_object_detection/      # Object detection tutorials
├── 7_motion_optical_flow/   # Motion analysis tutorials
├── 8_camera_geometry/       # Camera geometry tutorials
├── 9_stereo_vision/         # Stereo vision tutorials
├── 10_sfm_and_3D_Vision/    # 3D vision tutorials
├── 11_Image_Stitching/      # Image stitching tutorials
├── books/                   # Reference books and materials
└── papers/                  # Research papers collection
```

## Usage

### Web Interface

1. Start the application: `python gradio_app.py`
2. Open your browser to the URL shown in the terminal output
3. Upload an image using the interface
4. Select an algorithm category and specific algorithm
5. Click "Process Image" to see the results

### Programmatic Usage

```python
from algorithms.image_processing import apply_gaussian_blur
from algorithms.edge_detection import apply_canny
import cv2

# Load image
image = cv2.imread('image.jpg')

# Apply algorithms
blurred = apply_gaussian_blur(image)
edges = apply_canny(image)
```

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests if applicable
4. Commit your changes: `git commit -m 'Add feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

### Adding New Algorithms

1. Add your algorithm function to the appropriate file in `algorithms/`
2. Import it in `gradio_app.py`
3. Add it to the corresponding processing function
4. Update the dropdown choices in the interface

## Testing

Run the test suite to verify your installation:

```bash
python test_app.py
```

This will check all dependencies and basic algorithm functionality.

## Dependencies

- **OpenCV**: Computer vision algorithms
- **NumPy**: Numerical computing
- **PIL/Pillow**: Image processing
- **Matplotlib**: Visualization
- **Scikit-image**: Additional image processing
- **Gradio**: Web interface

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenCV community for the excellent computer vision library
- Gradio team for the web interface framework
- All contributors and researchers whose work is referenced in this repository

## Citation

If you use this repository in your research or projects, please cite:

```bibtex
@misc{classical_cv_opensource,
  title={Classical Computer Vision Open Source},
  author={Hariharan Sureshkumar},
  year={2025},
  url={https://github.com/hxriharan/classical-cv}
}
```

