# MOT16_Annotator
My attempt at creating a MOT16 annotation tool. I felt the need for this tool while working on my MS Thesis This tool takes video as an input and allows the user to create bounding boxes on each frame, these bounding boxes are saved to a det.txt file in MOT16 format.

# What is MOT16 format
MOT16 ground truth file is a CSV text-file containing one object instance per line. Each line must contain 10 values:

```
<frame>, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>
```

The conf value contains the detection confidence in the det.txt files. For the ground truth, it acts as a flag whether the entry is to be considered. A value of 0 means that this particular instance is ignored in the evaluation, while any other value can be used to mark it as active. For submitted results, all lines in the .txt file are considered. The world coordinates x,y,z are ignored for the 2D challenge and can be filled with -1. Similarly, the bounding boxes are ignored for the 3D challenge. However, each line is still required to contain 10 values.

All frame numbers, target IDs and bounding boxes are 1-based. Here is an example:

```
1, 3, 794.27, 247.59, 71.245, 174.88, -1, -1, -1, -1
1, 6, 1648.1, 119.61, 66.504, 163.24, -1, -1, -1, -1
1, 8, 875.49, 399.98, 95.303, 233.93, -1, -1, -1, -1
```

# Intended updates
- [ ] Display bounding box for the current frame
- [ ] Option to remove incorrectly marked bounding box
- [ ] Display current frame and total frames on the top left
- [ ] Read from existing det.txt file and display the results on the video
