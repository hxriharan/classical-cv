# Classical Computer Vision
This repository is meant for people who are trying to get into Classical computer vision, it will contain code implementation to some of the most famous classical computer vision algorithms and techniques, research papers and videos, all in one repository to learn and get familiarised with classical computer vision.

The end goal/future idea is to make a UI where one can upload images and click on the algorithm he/she wants to try on the images he/she chooses and can view the result!

## There are the below topics and the respective files, each folder has a seperate README.md which explains what each file contains and the explaination.

1> Image Fundamentals
- Pixel intensity and bit-depth
- Color spaces: RGB, HSV, YCbCr, Lab
- Image formats & representations (grayscale, binary, etc.)
- Sampling & quantization
- Image histograms

2> Image Preprocessing
- Noise types (salt & pepper, Gaussian, Poisson)
- Filtering:
    - Mean, Median
    - Gaussian blur
    - Bilateral filter
- Sharpening & high-pass filters
- Histogram equalization & contrast enhancement
- Gamma correction

3> Edge, Gradient & Feature Detection
- Gradient operators: Sobel, Prewitt, Scharr
- Canny edge detector
- Laplacian of Gaussian (LoG)
- Harris & Shi-Tomasi corner detection
- Hough Transform (lines, circles)
- DoG (Difference of Gaussians)

4> Feature Descriptors & Matching
- SIFT (Scale-Invariant Feature Transform)
- SURF (Speeded-Up Robust Features)
- ORB (Oriented FAST and Rotated BRIEF)
- BRIEF, FREAK, AKAZE
- Descriptor matching (Brute Force, FLANN)
- RANSAC (for robust estimation)

5> Image Segmentation
- Thresholding: global, adaptive, Otsu’s
- Morphological operations: erosion, dilation, opening, closing
- Connected components
- Watershed segmentation
- Graph-based segmentation (Felzenszwalb)
- Region growing & splitting/merging
- Superpixels (SLIC)

6> Object Detection & Recognition
- Template matching
- Haar cascades
- HOG (Histogram of Oriented Gradients)
- Sliding window methods
- Contour analysis
- Shape descriptors (Hu moments, Zernike moments)

7> Motion & Optical Flow
- Frame differencing
- Background subtraction (MOG, KNN)
- Optical flow:
    - Lucas-Kanade
    - Horn-Schunck
- Block matching
- Tracking:
    - Kalman filter
    - Particle filter
    - Meanshift / Camshift

8> Camera Geometry & Calibration
- Pinhole camera model
- Intrinsic and extrinsic parameters
- Camera calibration (Zhang's method)
- Lens distortion (radial, tangential)
- Homographies
- Fundamental & essential matrices
- Epipolar geometry

9> Stereo Vision & Depth Estimation
- Stereo matching (block matching, semi-global matching)
- Disparity maps
- Triangulation
- Rectification
- Depth from stereo

10> Structure from Motion (SfM) & 3D Vision
- Feature tracking across frames
- Bundle adjustment
- Point cloud generation
- Multi-view geometry
- Visual Odometry

11> Image Registration & Stitching
- Image alignment
- Feature-based or intensity-based registration
- Panorama stitching
- Homography estimation
- Blending techniques

12> SLAM (Simultaneous Localization and Mapping) (bridges into robotics)
- Feature-based SLAM (ORB-SLAM)
- Visual-Inertial SLAM
- Loop closure & graph optimization
- EKF-based SLAM

13> Image Classification & Scene Understanding (Traditional)
- Bag of visual words (BoVW)
- Spatial pyramids
- k-NN, SVM, PCA for classification

14> Mathematical Foundations
- Linear algebra (eigenvalues, SVD, PCA)
- Optimization (gradient descent, RANSAC)
- Projective geometry
- Convolution & correlation
- Fourier Transform & frequency analysis
- Graph theory (for segmentation and matching)

