from django.shortcuts import render
from django.http import JsonResponse
import base64
import tempfile

from pages.roboflow_api import predict_image

def index_view(request):
    return render(request, 'index.html', {
    })

def upload_endpoint(request):
    if request.method == 'POST':
        snapshot = request.POST.get('snapshot')
        data_part = snapshot.split(',')[1]
        binary_image = base64.b64decode(data_part)

        # Create a temporary file to save the binary image data
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(binary_image)
            image_path = temp_file.name
            giving_birth = predict_image(image_path)
        return JsonResponse({'message': giving_birth}, status=200)
    else:
        return JsonResponse({'message': 'Snapshot upload failed'}, status=400)

