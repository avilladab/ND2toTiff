# ND2toTiff
Python program to split an ND2 file into separate Tiff stacks.

This program uses "pims" to read the ND2 file, "tifffile" to save the tiff stacks and "os" to manage directories

This program splits the ND2 file "test.nd2" into tiff stacks.

"workdir" is the directory where the ND2 file is and "filename" is the name of the ND2 file (without extension).

By running the first block you will realise if the file "test.nd2" is in the directory "/home/user/folder", note that this syntax is for Linux, for Windows you will have to use the inverse slash, and to set something like
workdir = 'C:\\User\\Folder\\'

"n" is the number of stacks in the ND2 file.

The tiff stacks will be stored in "/home/user/folder/sep/" with the name "test_TXXXXXX.tif" and the number XXXXXX is the stack number "x" with preceding zeros to form a 6 digit number.
