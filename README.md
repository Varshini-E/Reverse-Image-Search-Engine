# Reverse-Image-Search-Engine
An optimized Reverse Image Search Engine for the Garments Industry.
Implemented in Python with Keras and Flask. 

## Research Paper
[Reverse Image Search Engine for Garment Industry](https://drive.google.com/file/d/1e7pwov88cNPT-dInZxqTy860lVGi_J3J/view)

## Usage
The dataset has been curated by webscraping relevant results from three e-commerce websites - Amazon, FabIndia, WestSide. To use the available data, follow the below steps: 
1. Download the images available in the drive link: [Images](https://drive.google.com/drive/folders/1s-9o37iDXzjIurALg4OXW7ZHT8Jcbwas?usp=sharing)
2. Create a folder called static and move the downloaded images to static/img.
3. Download the feature vectors available in the drive link: [Feature Vectors](https://drive.google.com/drive/folders/1FshtcFaYzAmRJzRCJn2OutILbajUgDGp?usp=sharing)
4. Move the downloaded features to static/feature. 
5. Next, the fine tuned model is to be downloaded from the drive link: [Model](https://drive.google.com/file/d/1v97HJSsV7PcVfwmE-p9FG6C22l8nkjXb/view?usp=sharing)
6. Create a new folder called output and place the downloaded model in output. 
7. Download the indexed tree set up for annoy indexing from the drive link: [Image Indexing](https://drive.google.com/drive/folders/1FshtcFaYzAmRJzRCJn2OutILbajUgDGp?usp=sharing)
8. The Flask interface now has been set up with corresponding folders.
9. Run server.py to get the desired web interface for performing reverse image search. 


