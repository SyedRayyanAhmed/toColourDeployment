from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Welcome(request):
    return render(request, 'index.html')

def Execute_toColour(request):
    #print('hello')
    if request.method == 'POST':
        uploadImgFile = request.FILES['image']

        #open() function to create a file object
        with open('./images/img1.jpg', 'wb') as f:
        # Write the contents of the image file to the file object
            f.write(uploadImgFile.read())

        #print(uploadImgFile)
        exec(open('./toColour.py').read())
        with open('./output/coloured.png', 'rb') as f:
            # Read the image data
            image_data = f.read()
        # Create an HttpResponse object with the image data
        response = HttpResponse(image_data, content_type='image/png')

    # Return the response
    return response
    #return render(request, 'result.html')
