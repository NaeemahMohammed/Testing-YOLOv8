Hello Everyone, 
I recently did a project evaluating the accruracy of YOLOv8 in the detection of surfacce aquatic trash.
I carried ot 3 tests
1. Optimal train-to-valid ratio
2. Effect of rain on accuracy of YOLOv8
3. Effect of brightness on the accuracy of YOLOv8

I have attached all the codes I used in hopes that it can help anyone carrying out a similar project. Here is a brief description of each code

Apply Rain filter: As the name says this code applies a photoshop rain filter to all the images and it saves the images in a new directory but with their original names. However, the filter can be repalced with any .PNG or effect.

Darkening Code: This code simply darkens all the images to two degrees. You can play around with how dark you want the images. This code also preserves the images original names and saves them in a new folder

Shufflng code: This code shuffles all your train and valid images and splits them into a defined ratio. I used this when testing various train-to-valid ratios

