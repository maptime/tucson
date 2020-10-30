# Testing adding materials to this 

![](https://s3.amazonaws.com/statescoop-media/uploads/GIS-big-data-graphic-getty.jpg?mtime=20170821165732)
## Steps

## Processing your Colorized Point Cloud into a textured mesh

* Open Meshlab
* import the `.txt` file

![](./screenshot_from_2020-10-29_14-56-35.png)


![](./screenshot_from_2020-10-29_14-57-18.png)

* select correct point format `X Y Z R G B` with separator `,`

![](./screenshot_from_2020-10-29_15-16-22.png)

* (optional) invert your normals
    * makes for more color accurate visuals while working

![](./screenshot_from_2020-10-29_15-19-11.png)

* Simplify 1 of 2 ways
    * Point Simplification 

![](./screenshot_from_2020-10-29_15-24-38.png)


![](./screenshot_from_2020-10-29_15-25-04.png)

    * or Poisson disc sampling

![](./screenshot_from_2020-10-29_15-26-30.png)


![](./screenshot_from_2020-10-29_15-26-47.png)

    * these steps can take some time to complete

* result should look a lot less densely packed, only about 7k points instead of 11 million

![](./screenshot_from_2020-10-29_15-28-55.png)

* calculate the normals of the new simplified point cloud, (make sure you have the new point cloud selected in the list on the right) 

![](./screenshot_from_2020-10-29_15-32-25.png)

* perform a Screened Poisson reconstruction (optional increase the oct tree depth for more detail, but since we are already using the simplified point cloud it won't do that much. )

![](./screenshot_from_2020-10-29_15-32-46.png)


![](./screenshot_from_2020-10-29_15-34-04.png)

* remove zero area faces that sometimes get created by poisson reconstruction

![](./screenshot_from_2020-10-29_15-36-40.png)

* perform a trivial plane parameterization which helps us know where the colors for our mesh should go

![](./screenshot_from_2020-10-29_15-37-06.png)

* Save your project, put in names for each object you've worked on so far

![](./screenshot_from_2020-10-29_15-37-43.png)


![](./screenshot_from_2020-10-29_15-38-30.png)

* Transfer the vertex attributes of the original point cloud to the texture of the reconstruction

![](./screenshot_from_2020-10-29_15-39-35.png)

    * make sure the  source mesh is the original point cloud with 11 million points
    * target mesh is the poisson mesh
    * texture width and height are atleast 4096 (higher numbers gives more resolution for final product )

![](./screenshot_from_2020-10-29_15-41-31.png)

* check that a png has been created

![](./screenshot_from_2020-10-29_15-42-25.png)

* inspect result

![](./screenshot_from_2020-10-29_15-42-50.png)

* export mesh as `.obj`

![](./screenshot_from_2020-10-29_15-43-31.png)


![](./screenshot_from_2020-10-29_15-44-40.png)

* uncheck vert color and vert normal because we don't need them and they'll make our file larger

![](./screenshot_from_2020-10-29_15-45-51.png)

## Blender step, exporting as `.glb`
* open blender

![](./screenshot_from_2020-10-29_15-46-55.png)

* import `.obj` (its also an option under the file menu import)

![](./screenshot_from_2020-10-29_15-47-34.png)

* select file from folder where you saved it

![](./screenshot_from_2020-10-29_15-48-57.png)

* turn on material shading so we can tell our model is colored correctly

![](./screenshot_from_2020-10-29_15-49-33.png)

* select model and set geometry to origin (lidar points position usually ) with the right click mouse and `set_origin` option

![](./screenshot_from_2020-10-29_15-51-00.png)

* scale down the model so we can see it, press `s` key and then type `.0001` to make it 1 /10000 th of its current size, and press enter

![](./screenshot_from_2020-10-29_15-52-47.png)

* set X rotation to 0 (might have to press the `n` key first to get the transform window to appear)

![](./screenshot_from_2020-10-29_15-53-26.png)

* Export as gltf option, we will be using the `.glb` that is by default 

![](./screenshot_from_2020-10-29_15-54-00.png)

* name export file something like `poisson_mesh` and the glb will be added on its own

![](./screenshot_from_2020-10-29_15-55-04.png)





