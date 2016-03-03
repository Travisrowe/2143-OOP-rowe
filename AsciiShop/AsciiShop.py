"""
Travis Rowe
3/3/16

"""
import os
import time
from PIL import Image
import sys
import urllib3, uuid

"""
This and the getCat method is code that nullifies the need to import cat.
"""
url = 'http://thecatapi.com/api/images/get'

def getCat(directory=None, filename=None, format='png'):

    basename = '%s.%s' % (filename if filename else str(uuid.uuid4()), format)
    savefile =  os.path.sep.join([directory.rstrip(os.path.sep), basename]) if directory else basename
    downloadlink = url + '?type=%s' % format
    http = urllib3.PoolManager()
    r = http.request('GET', downloadlink)
    fp = open(savefile, 'wb')
    fp.write(r.data)
    fp.close()

    return savefile

class RandomCat(object):

    def __init__(self):

        self.name = ''          # name of image
        self.path = '.'         # path on local file system
        self.format = 'png'
        self.width = 0          # width of image
        self.height = 0         # height of image        
        self.img = None         # Pillow var to hold image


    """
    @Description: 
    - Uses random cat to go get an amazing image from the internet
    - Names the image
    - Saves the image to some location
    @Returns: 
    """

    """
    def getImage(self):
        self.name = self.getTimeStamp()
        getCat(directory=self.path, filename=self.name, format=self.format)
        self.img = Image.open(self.name+'.'+self.format)
        
        self.width, self.height = self.img.size
    """
    def getImage(self):
        inpt = input("Do you have an image of your own? (Y/N)\n")
        if(inpt == 'Y'):
            self.path = input('Input the path now (without the image title).\n')
            self.name = input('Input just the image title now\n')
        else:
            self.name = self.getTimeStamp()
        getCat(directory=self.path, filename=self.name, format=self.format)
        self.img = Image.open(self.name+'.'+self.format)
        
        self.width, self.height = self.img.size
    
        
    """
    Saves the image to the local file system given:
    - Names
    - Path
    """
    def saveImage(self):
        pass

    """
    """
    def nameImage(self):
        pass

    """
    Gets time stamp from local system
    """
    def getTimeStamp(self):
        seconds,milli = str(time.time()).split('.')
        return seconds 


""" 
The ascii character set we use to replace pixels. 
The grayscale pixel values are 0-255.
0 - 25 = '#' (darkest character)
250-255 = '.' (lightest character)
"""

alteredAsciiImage = [] #This will be used to store the inverted picture

class AsciiImage(RandomCat):

    def __init__(self,new_width="not_set"):
        super(AsciiImage, self).__init__()

        self.newWidth = new_width
        self.newHeight = 0
            
        self.asciiChars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
        self.imageAsAscii = []
        self.matrix = None
        
        
    """
    @name: convertToAscii
    @Description:
    - Takes the image supplied either by the user or getCat
    - Converts the image to greyscale using a built-in Python method
    - Divides the greyscale pixel values (0-255, with 0 being the darkest color) and divides them by 25
    - Assigns characters based on the "new pixel values (0-10)"
    - Stores the new image as a matrix
    @Params: None
    @Returns: None
    """
    def convertToAscii(self):
    
        if self.newWidth == "not_set":
            self.newWidth = self.width
            
        self.newHeight = int((self.height * self.newWidth) / self.width)
            
        if self.newWidth == None:
            self.newWidth = self.width
            self.newHeight = self.height
            
        self.newImage = self.img.resize((self.newWidth, self.newHeight))
        self.newImage = self.newImage.convert("L") # convert to grayscale
        all_pixels = list(self.newImage.getdata())
        self.matrix = listToMatrix(all_pixels,self.newWidth)
        
        if(self.imageAsAscii == []):
            for pixel_value in all_pixels:
                index = int(pixel_value / 25) # 0 - 10
                self.imageAsAscii.append(self.asciiChars[index])
        else:
            for pixel_value in all_pixels:
                index = int(pixel_value / 25) # 0 - 10
                alteredAsciiImage.append(self.asciiChars[index])

    """
    Print the image to the screen
    """
    def printImage(self):
        if(alteredAsciiImage == []):    #Checks whether to print inverted picture
            tempAsciiImage = ''.join(ch for ch in self.imageAsAscii)    #Uses a temp list so that the original is not converted to a string
            for c in range(0, len(tempAsciiImage), self.newWidth):  #Iterates through each line of the image for printout (y-axis)
                print (tempAsciiImage[c:c+self.newWidth])   #Prints one horizontal line of the image (x-axis)
        else:
            tempAsciiImage = ''.join(ch for ch in alteredAsciiImage) #Inverted picture
            for c in range(0, len(tempAsciiImage), self.newWidth):
                print (tempAsciiImage[c:c+self.newWidth]) 

"""
Convert to 2D list of lists to help with manipulating the ascii image.
Example:
    
    L = [0,1,2,3,4,5,6,7,8]
    
    L = to_matrix(L,3)
    
    L becomes:
    
    [[0,1,2],
    [3,4,5],
    [6,7,8]]
"""
def listToMatrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

class AsciiShop(AsciiImage):

    """
    @Name: flip
    @Description:
        This method will flip an image horizontally, or vertically. 
        Vertically means all pixels in row 0 => row N, row 1 => row N-1, ... row N/2 => row N/2+1
        Horizontally means all pixels in col 0 => col N, col 1 => col N-1, ... col N/2 => col N/2+1
    @Params: direction (string) - [horizontal,vertical] The direction to flip the cat.
    @Returns: (string) - Flipped ascii image.
    """
    def flip(self,direction = ""):
        tempAsciiImage = ''.join(ch for ch in self.imageAsAscii)    #Uses a temporary list so the original is not converted to a string
        direction = input('Which way should the image be flipped? (horizontal/vertical) ')

        if(direction == 'vertical'):
            for c in range(len(tempAsciiImage), -1, -self.newWidth): #Traverses through each line of the original image from bottom to top
                print (tempAsciiImage[c:c+self.newWidth])

        elif(direction == 'horizontal'):
            str = ""
            for c in range(0, len(tempAsciiImage), self.newWidth):  #Iterates through each line of the image for printout
                print("")   #Prints a new line
                for d in reversed(range(self.newWidth)):    #Traverses a horizontal line backwards
                    print(tempAsciiImage[c+d],end = "")     #Adds d, the index of backwards-traversal, to c, the beginning of the row

        else:
            print("Input not valid.\n")
            sleep(1.0)

    """
    @Name: invert 
    @Description:
        This method will take all the lightest pixels and make them the darkest, next lightest => next darkest, etc..
    @Params: None
    @Returns: (string) - Inverted ascii image.
    """
    def invert(self):
        tempAsciiChars = self.asciiChars
        self.asciiChars = [ '.', ',', ':', '*', '<', '+', 'S', '%', '@', 'A', '#']
        
        self.convertToAscii()
        self.printImage()
        self.asciiChars = tempAsciiChars

    """
    @Name: crop
    @Description:
        This will crop an image from a starting x,y coordinate to an ending x,y coordinate. For example:
        crop((col,row),(col,row))
        crop((1,1),(8,4)) (all the zeros are cropped from the image)
        **********          0000000000
        **********          0*******00
        **********   =>     0*******00    
        **********          0*******00
        **********          0*******00
    @Params: 
      start (tuple) - (x,y)
      end (tuple) - (x,y)
    @Returns: (string) - Cropped ascii image.
    """
    def crop(self,x1,y1,x2,y2):
        #These if statements check if the input-dimensions fit inside the original picture
        if(x1 < 0):
            x1 = 0
        if(x2 > self.newWidth):
            x2 = self.newWidth
        if(y1 < 0):
            y1 = 0
        if(y2 > self.newHeight):
            y2 = self.newHeight

        tempAsciiImage = ''.join(ch for ch in self.imageAsAscii)    #Uses a temp list so that the original is not converted to a string
        
        for c in range(self.newWidth*y1+x1, self.newWidth * y2, self.newWidth):  #Starts the iterator on the correct column, x1, and ends it on the correct row, self.newWidth * y2
            #if(c >= self.newWidth * y1):    #Checks if the iterator has gotten to the starting row yet
            print (tempAsciiImage[c:c+x2-x1])   #Prints the rows from the starting x coordinate to the ending one
                                                    #Note: On row 0 (y1 = 0) c+x2-x1 = x2 because on row 0, c = x1.

        

if __name__=='__main__':
    awesomeCat = AsciiShop(150)
    awesomeCat.getImage()
    
    awesomeCat.convertToAscii()
    awesomeCat.printImage()

    awesomeCat.invert()

    inp = 0
    while(not inp=='exit'):  #Allows the user to decide which method to call or to exit
        inp = input('\n\nWhat would you like to do?\n flip\n crop\n exit\n')
        if(inp == 'flip'):
            awesomeCat.flip()
        elif(inp == 'crop'):
            coords = input('What are the starting and ending coordinates you want to keep in your new image\n e.g. \"x1,y1,x2,y2\"\n')
            x1, y1, x2, y2 = coords.split(',')
            awesomeCat.crop(int(float(x1)),int(float(y1)),int(float(x2)),int(float(y2)))
        elif(inp == 'exit'):
            print("Exiting...")
        else:
            print("Input not valid")