# Computer vison note 

## OpenCv install with anaconda on Mac OS

Create anaconda env 

```
conda create --name opencv # repleace opencv with your option
```


Download opencv 

```bash 
cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0.zip
```

Build opencv
```bash
export CONDA_HOME=~/opt/anaconda3 # if user. For global, /anaconda3
export CPLUS_INCLUDE_PATH=$CONDA_HOME/envs/cv/lib/python3.7
export CPATH="/usr/local/Cellar/tesseract/4.1.1/include"

cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
-D PYTHON3_LIBRARY=$CONDA_HOME/envs/opencv/lib/libpython3.7m.dylib \
-D PYTHON3_INCLUDE_DIR=$CONDA_HOME/envs/opencv/include/python3.7m \
-D PYTHON3_EXECUTABLE=$CONDA_HOME/envs/opencv/bin/python \
-D PYTHON3_PACKAGES_PATH=$CONDA_HOME/envs/opencv/lib/python3.7/site-packages \
-D PYTHON3_NUMPY_INCLUDE_DIRS=$CONDA_HOME/envs/opencv/lib/python3.7/site-packages/numpy/core/include \
-D BUILD_opencv_python2=OFF \
-D BUILD_opencv_python3=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D OPENCV_ENABLE_NONFREE=ON \
-D BUILD_EXAMPLES=ON ..
```

Create link cv2 to python env
```
# rename cv2
cd /usr/local/python/cv2/python-3.7
sudo mv cv2.cpython-37m-darwin.so cv2.so

cd ~/opt/anaconda3/envs/opencv/lib/python3.7/site-packages/
ln -s /usr/local/python/cv2/python-3.7/cv2.so cv2.so
```

## Use jupyter with conda env 

Install ipykernel 
conda install -c anaconda ipykernel

Install kernel 

python -m ipykernel install --user --name=<env name>

## Refer 

[Install OpenCV 4.0.1 from Source on MacOS with Anaconda Python 3.7 to Use SIFT and SURF](https://medium.com/repro-repo/install-opencv-4-0-1-from-source-on-macos-with-anaconda-python-3-7-to-use-sift-and-surf-9d4287d6228b)

[Install OpenCV 4 on macOS](https://www.pyimagesearch.com/2018/08/17/install-opencv-4-on-macos/)

