# Workflow to create VR/AR Web experiences from Lidar data 

## Example  pages

This workshop will be a lot like a strenous hike. For 90 minutes you will follow a steep trail of steps carefully, one wrong move and you could tumble back to the start (intense!), but I hope you'll decide once we reach the summit its worth it. To help you realize that lets look at a couple of examples.

* [Finger Rock model in AR on your phone](https://finger-rock-ar.glitch.me/)
  * Open the link and then tap the icon that looks like a cube
  * Point your phone down at a horizontal surface (your floor or desk should  work)  and gently move it so it can identify a platform
  * Once the model appears, move your phone around to view the model from different perspectives
* [Finger Rock model in VR/3D on computer](https://finger-rock-vr.glitch.me/)
  * Click on the link, then wait for the model to load 
  * Once it appears (it might be below you) use the arrow keys to move the camera around the scene, and click drag to change the direction the camera faces


## Steps

## Getting your resources

### Getting the lidar data

* Visit [https://prd-tnm.s3.amazonaws.com/LidarExplorer/index.html#/](https://prd-tnm.s3.amazonaws.com/LidarExplorer/index.html#/) and zoom in on Tucson
* Click the box select tool under the `+ -` and home buttons in the top left corner of the map 
* Click on the map once to start drawing the selection box, and a second point to complete the shape
* in the panel that appears on the right side select `lidar within AOI` 
* Click the folder, and finally select one of the lidar entries to open in a new tab
* On the new page scroll down to section titled `Related External Resources`
* Start your download for the `.laz` resource 

### Getting the orthographic imagery

* Visit [https://libguides.library.arizona.edu/GIS/ImageryandLidar](https://libguides.library.arizona.edu/GIS/ImageryandLidar) and click on the 2017 button under the section *NAIP Imagery*
* This is the tricky step, you must try to find a section of landscape that overlaps significantly with your lidar data, so try to select the same part of arizona 
* Click on that tile, and choose to *Download*


## Installing and running the python code
### Setting up conda for python to help you install existing code 
For this section you will need to install `miniconda` to follow the steps verbatim. If you have your own existing python code setup then I will assume you know what's going on and you'll manage to get the required packages. 

* go to https://docs.conda.io/en/latest/miniconda.html and download the correct installer for your operating system
* Follow the other instructions on the page to complete the installation

### Install Point data abstraction library (PDAL) and laspy

* In a command line run this command `conda install --channel conda-forge pdal`, which should give you a *yes/no* option to install PDAL and its dependencies , go ahead and say *yes*
* Using the standard python installer install `laspy`  with `pip install laspy`

### Getting the code and colorizing our pointcloud

 [pdal file](https://drive.google.com/file/d/1z8L70_xb8KlX6sHx1R_ZiysCTthR4PtM/view?usp=sharing)

* first edit the colorize.json  and make 3 changes
    * change where it says `change_1` to the name of the lidar `.laz` file you downloaded
    * change where it says `change_2` to the orthographic image `.tif` you downloaded
* then using your command line you'll execute the PDAL pipeline command 
    * `pdal pipeline colorize.json` 
    * this will take a while to execute, but in the mean time we will continue with some previously generated results [python code](https://drive.google.com/file/d/16eLoCfCsEl4F2iAzDu_KuQKntbNwWgdd/view?usp=sharing)

* now using this program we will convert our colorized points into a `.txt` file that meshlab can read
* simply run `python python_processing.py` and you will convert the `colorized.laz` into `colorized.txt`




## Processing your Colorized Point Cloud into a textured mesh

* Open Meshlab
* import the `colorized.txt` file [screenshot](./screenshot_from_2020-10-29_14-56-35.png)
 [screenshot](./screenshot_from_2020-10-29_14-57-18.png)

* select correct point format `X Y Z R G B` with separator `,` [screenshot](./screenshot_from_2020-10-29_15-16-22.png)

* (optional) calculate your normals
    * makes for more color accurate visuals while working [screenshot](./screenshot_from_2020-10-29_15-19-11.png)

* Simplify 1 of 2 ways
    * Point Simplification  [screenshot](./screenshot_from_2020-10-29_15-24-38.png)
 [screenshot](./screenshot_from_2020-10-29_15-25-04.png)

* or Poisson disc sampling [screenshot](./screenshot_from_2020-10-29_15-26-30.png)
 [screenshot](./screenshot_from_2020-10-29_15-26-47.png)

* these steps can take some time to complete

* result should look a lot less densely packed, only about 7k points instead of 11 million [screenshot](./screenshot_from_2020-10-29_15-28-55.png)

* calculate the normals of the new simplified point cloud, (make sure you have the new point cloud selected in the list on the right)  [screenshot](./screenshot_from_2020-10-29_15-32-25.png)

* perform a Screened Poisson reconstruction (optional increase the oct tree depth for more detail, but since we are already using the simplified point cloud it won't do that much. ) [screenshot](./screenshot_from_2020-10-29_15-32-46.png)
 [screenshot](./screenshot_from_2020-10-29_15-34-04.png)

* remove zero area faces that sometimes get created by poisson reconstruction [screenshot](./screenshot_from_2020-10-29_15-36-40.png)

* perform a trivial plane parameterization which helps us know where the colors for our mesh should go [screenshot](./screenshot_from_2020-10-29_15-37-06.png)

* Save your project, put in names for each object you've worked on so far [screenshot](./screenshot_from_2020-10-29_15-37-43.png)
 [screenshot](./screenshot_from_2020-10-29_15-38-30.png)

* Transfer the vertex attributes of the original point cloud to the texture of the reconstruction [screenshot](./screenshot_from_2020-10-29_15-39-35.png)

* make sure the  source mesh is the original point cloud with 11 million points
* target mesh is the poisson mesh
* texture width and height are atleast 4096 (higher numbers gives more resolution for final product ) [screenshot](./screenshot_from_2020-10-29_15-41-31.png)

* check that a png has been created [screenshot](./screenshot_from_2020-10-29_15-42-25.png)

* inspect result [screenshot](./screenshot_from_2020-10-29_15-42-50.png)

* export mesh as `.obj` [screenshot](./screenshot_from_2020-10-29_15-43-31.png)
 [screenshot](./screenshot_from_2020-10-29_15-44-40.png)

* uncheck vert color and vert normal because we don't need them and they'll make our file larger [screenshot](./screenshot_from_2020-10-29_15-45-51.png)

## Blender step, exporting as `.glb`
* open blender [screenshot](./screenshot_from_2020-10-29_15-46-55.png)

* import `.obj` (its also an option under the file menu import) [screenshot](./screenshot_from_2020-10-29_15-47-34.png)

* select file from folder where you saved it [screenshot](./screenshot_from_2020-10-29_15-48-57.png)

* turn on material shading so we can tell our model is colored correctly [screenshot](./screenshot_from_2020-10-29_15-49-33.png)

* select model and set geometry to origin (lidar points position usually ) with the right click mouse and `set_origin` option [screenshot](./screenshot_from_2020-10-29_15-51-00.png)

* scale down the model so we can see it, press `s` key and then type `.0001` to make it 1 /10000 th of its current size, and press enter [screenshot](./screenshot_from_2020-10-29_15-52-47.png)

* set X rotation to 0 (might have to press the `n` key first to get the transform window to appear) [screenshot](./screenshot_from_2020-10-29_15-53-26.png)

* Export as gltf option, we will be using the `.glb` that is by default  [screenshot](./screenshot_from_2020-10-29_15-54-00.png)

* name export file something like `poisson_mesh` and the glb will be added on its own [screenshot](./screenshot_from_2020-10-29_15-55-04.png)

## Importing into VR/AR on the WEB!!






