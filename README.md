# MOT16_Annotator
My attempt at creating a MOT16 annotation tool. I felt the need for this tool while working on my MS Thesis. This tool takes video as an input and allows the user to create bounding boxes on each frame, these bounding boxes are saved to a ``gt.txt`` file in MOT16 format.

The purpose of this file is to allow the user to manually create ground truth for their custom dataset. This ground truth file can then be used in conjunction with tracker output file to generate MOT metrics to gauge the performance of tracker on custom data.

# What is MOT16 format
MOT16 ground truth file is a CSV text-file containing one object instance per line. Each line must contain 10 values:

```
<frame>, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>
```

The ``<conf>`` value contains the detection confidence in the det.txt files. For the ground truth, it acts as a flag whether the entry is to be considered. A value of 0 means that this particular instance is ignored in the evaluation, while any other value can be used to mark it as active. The world coordinates x,y,z are ignored for the 2D challenge and can be filled with -1. Similarly, the bounding boxes are ignored for the 3D challenge. However, each line is still required to contain 10 values.

All frame numbers, target IDs and bounding boxes are 1-based. Here is an example:

```
1, 3, 794.27, 247.59, 71.245, 174.88, -1, -1, -1, -1
1, 6, 1648.1, 119.61, 66.504, 163.24, -1, -1, -1, -1
1, 8, 875.49, 399.98, 95.303, 233.93, -1, -1, -1, -1
```

This annotater uses a value of ``1`` for ``<conf>``

# What are MOT benchmark metrics
Popular MOT benchmark metrics are as follows:

Metric | Description
------ | -----------
MOTA | Multiple object tracker accuracy
MOTP | Multiple object tracker precision
MT | Number of objects tracked for at least 80 percent of lifespan
ML | Number of objects tracked less than 20 percent of lifespan
ID | Total number of track switches
FM | Total number of switches from tracked to not tracked (fragmentation)

You can read more about these metrics [here](https://arxiv.org/pdf/1504.01942.pdf)

# How to run
This application uses OpenCV, therefore you should install the package in your python installation.

On windows computer, open cmd and browse to the folder where `MOT-Annotation.py` is saved, use the following command to run the application.
````
python MOT-Annotation.py -l d:\myVideo.mp4
````

A new folder `gt` will be created in the same folder as the video. All the annotations would be saved in file `gt.txt` inside folder `gt`.
To increment object id press 'i'
To decrement object id press 'd'
To move to next frame press 'n'
To quit the app, press 'esc'

# Intended updates
- [x] Ability to assign ID to ground truth objects 
- [ ] Display bounding box for the current frame
- [ ] Option to remove incorrectly marked bounding box
- [ ] Display current frame and total frames on the top left
- [ ] Read from existing det.txt file and display the results on the video

# Citation
```
@article{MOTChallenge2015,
	title = {{MOTC}hallenge 2015: {T}owards a Benchmark for Multi-Target Tracking},
	shorttitle = {MOTChallenge 2015},
	url = {http://arxiv.org/abs/1504.01942},
	journal = {arXiv:1504.01942 [cs]},
	author = {Leal-Taix\'{e}, L. and Milan, A. and Reid, I. and Roth, S. and Schindler, K.},
	month = apr,
	year = {2015},
	note = {arXiv: 1504.01942},
	keywords = {Computer Science - Computer Vision and Pattern Recognition}
}
```

```
@article{MOT16,
	title = {{MOT}16: {A} Benchmark for Multi-Object Tracking},
	shorttitle = {MOT16},
	url = {http://arxiv.org/abs/1603.00831},
	journal = {arXiv:1603.00831 [cs]},
	author = {Milan, A. and Leal-Taix\'{e}, L. and Reid, I. and Roth, S. and Schindler, K.},
	month = mar,
	year = {2016},
	note = {arXiv: 1603.00831},
	keywords = {Computer Science - Computer Vision and Pattern Recognition}
}
```
