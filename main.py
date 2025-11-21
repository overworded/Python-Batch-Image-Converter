from PIL import Image as imagelib
from os import listdir, rename

def convertImage(imagePath: str, goalFormat: str):
  try:
    image = imagelib.open('Input\\' + imagePath)
  except:
    print("Unable to open " + imagePath + "'. Probably not an image file.")
    return False

  if image.format == goalFormat:
    image.close()
    rename('Input\\' + imagePath, 'Output\\' + imagePath)

    print("Image already formatted as a '" + goalFormat + "'")
    return False

  image.save('Output\\' + imagePath.rsplit('.', 1)[0] + '.' + goalFormat, goalFormat)
  image.close()

  print("Reformatted '" + imagePath.rsplit('.', 1)[0] + "' to a " + goalFormat)

  return True


def main():
  files = listdir('Input')
  goalFormat = 'png'

  print("#"*5 + " Reformatting " + str(len(files)) + " image(s) to '" + goalFormat + "' " + "#"*5)
  fileCount = 0

  for fileName in files:
    if convertImage(fileName, goalFormat):
      fileCount += 1
  
  print("#"*5 + " Reformatted " + str(fileCount) + " image(s) to '" + goalFormat + "' " + "#"*5)

main()