# Camera Geometry & Calibration

This section explores the foundational concepts in camera modeling and multi-view geometry. These are essential for 3D computer vision, robotics, SLAM, AR/VR, and stereo vision.

---

## Topics Covered

1. **Pinhole Camera Model**
2. **Intrinsic & Extrinsic Parameters**
3. **Camera Calibration (Zhang's Method)**
4. **Lens Distortion (Radial, Tangential)**
5. **Homographies**
6. **Fundamental & Essential Matrices**
7. **Epipolar Geometry**

---

## 1. Pinhole Camera Model

The pinhole model is a mathematical model that describes how 3D points in the world project onto a 2D image plane.

### Projection Equation:

\[
s \cdot \mathbf{x} = \mathbf{K} \cdot [\mathbf{R} \,|\, \mathbf{t}] \cdot \mathbf{X}
\]

Where:
- \( \mathbf{X} \) = 3D point in world coordinates (homogeneous)
- \( \mathbf{x} \) = 2D image point (homogeneous)
- \( \mathbf{K} \) = Intrinsic matrix
- \( \mathbf{R}, \mathbf{t} \) = Rotation and translation (extrinsic)

---

## 2. Intrinsic & Extrinsic Parameters

### Intrinsic Parameters:
Describe the camera's internal characteristics.

\[
\mathbf{K} =
\begin{bmatrix}
f_x & 0 & c_x \\
0 & f_y & c_y \\
0 & 0 & 1
\end{bmatrix}
\]

- \( f_x, f_y \) – focal lengths in pixels
- \( c_x, c_y \) – principal point (image center)

### Extrinsic Parameters:
Define the camera's position and orientation in the world.
- \( \mathbf{R} \) – 3×3 rotation matrix
- \( \mathbf{t} \) – 3×1 translation vector

---

## 3. Camera Calibration (Zhang's Method)

Used to estimate intrinsic and extrinsic parameters from images of a known pattern (e.g., chessboard).

### Steps:
1. Capture multiple images of a calibration pattern from different angles.
2. Detect corners (e.g., OpenCV’s `findChessboardCorners`)
3. Estimate camera matrix and distortion using `cv2.calibrateCamera()`

Reference:
- Zhang, Z. "A Flexible New Technique for Camera Calibration", IEEE Transactions on Pattern Analysis and Machine Intelligence, 2000. [[PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr98-71.pdf)]

---

## 4. Lens Distortion

### Radial Distortion:
- Causes straight lines to appear curved
- Modeled using \( k_1, k_2, k_3 \)

### Tangential Distortion:
- Occurs when the lens and the image plane are not parallel
- Modeled using \( p_1, p_2 \)

### Distortion Coefficients:
\[
[k_1, k_2, p_1, p_2, k_3]
\]

---

## 5. Homography

Homography is a transformation between two planes (2D ↔ 2D mapping).

\[
\mathbf{x}' = \mathbf{H} \cdot \mathbf{x}
\]

Used in:
- Image stitching
- Planar object tracking
- Perspective correction

Can be estimated using `cv2.findHomography()` with point correspondences.

---

## 6. Fundamental & Essential Matrices

These encode the geometric relationship between two views.

### Fundamental Matrix \( \mathbf{F} \)
- Maps points from one image to epipolar lines in the other
- Intrinsic-independent

### Essential Matrix \( \mathbf{E} \)
\[
\mathbf{E} = \mathbf{K}^T \cdot \mathbf{F} \cdot \mathbf{K}
\]
- Used when camera intrinsics are known

Estimated using `cv2.findFundamentalMat()` or `cv2.findEssentialMat()`.

---

## 7. Epipolar Geometry

Describes constraints between two camera views.

- **Epipolar lines**: Points in one image lie on lines in the other image
- **Epipoles**: Intersection points of the baseline with the image planes
- **Epipolar constraint**:
\[
\mathbf{x}'^T \cdot \mathbf{F} \cdot \mathbf{x} = 0
\]

Understanding epipolar geometry is critical for:
- Stereo matching
- Structure-from-Motion (SfM)
- Visual Odometry

---

## Further Reading

- Hartley & Zisserman – Multiple View Geometry in Computer Vision*
- Richard Szeliski – Computer Vision: Algorithms and Applications*
- OpenCV Tutorials

