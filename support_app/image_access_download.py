import os
from django.conf import settings
from google.cloud import storage
from datetime import timedelta
from django.http import HttpResponse, HttpResponseNotFound
from .models import(
    ECTransportation, RRTransportation, PUCUpoloadMarks, JEEMain1, JEEMain2, COMEDK,
    )
from django.shortcuts import render, redirect, get_object_or_404
import zipfile
from io import BytesIO
from django.contrib import messages



# Mapping of model names to classes
model_mapping = {
    'ectransportation': ECTransportation,
    'rrtransportation': RRTransportation,
    'pucupoloadmarks': PUCUpoloadMarks,
    'jeemain1': JEEMain1,
    'jeemain2': JEEMain2,
    'comedk': COMEDK,
}

def download_all_images(request, model_name):
    # Get the model class from the mapping
    model_class = model_mapping.get(model_name)
    if not model_class:
        return render(request, 'error/404.html')
    
    # Initialize Google Cloud Storage client
    storage_client = storage.Client()
    bucket = storage_client.bucket(settings.BUCKET_NAME)

    # Create an in-memory ZIP file
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        images_found = False  # Flag to track if any images are added
        for upload in model_class.objects.all():
            # Dynamically check for fields
            file_field = None
            if hasattr(upload, 'upload_marks') and upload.upload_marks:
                file_field = upload.upload_marks
            elif hasattr(upload, 'photo') and upload.photo:
                file_field = upload.photo
                
            if file_field:
                blob_name = file_field.name
                blob = bucket.blob(blob_name)
                if blob.exists():
                    images_found = True
                    file_content = blob.download_as_bytes()
                    # Extract file extension and construct filename
                    file_extension = os.path.splitext(blob_name)[1]
                    # Sanitize the name by replacing spaces and dots with underscores
                    sanitized_name = re.sub(r'[ .]', '_', upload.name)
                    # Add the file to the ZIP with a formatted name
                    zip_file.writestr(f"{sanitized_name}_{upload.pk}{file_extension}", file_content)
                    if hasattr(upload, 'upload_marks') and upload.upload_marks:
                        zip_file.writestr(f"{sanitized_name}_{upload.registration_number}{file_extension}", file_content)
                    else:
                        zip_file.writestr(f"{upload.pk}_{sanitized_name}{file_extension}", file_content)

    # Handle the case where no images are found
    if not images_found:
        messages.warning(request, "No images found to download.")
        return render(request, 'error/404.html')
    
    # Return the ZIP file as a response
    zip_buffer.seek(0)
    response = HttpResponse(zip_buffer, content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{model_name}_images.zip"'
    return response

    
                
    
    
    
    
import re

def download_image(request, pk, model_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(settings.BUCKET_NAME)
    model_class = model_mapping.get(model_name)
    
    if model_class:
        image_details = get_object_or_404(model_class, pk=pk)
        
        file_field = None
        if hasattr(image_details, 'upload_marks') and image_details.upload_marks:
            file_field = image_details.upload_marks
        elif hasattr(image_details, 'photo') and image_details.photo:
            file_field = image_details.photo
            
        if file_field:
            blob_name = file_field.name
            blob = bucket.blob(blob_name)
            if blob.exists():
                # Fetch the file content
                file_content = blob.download_as_bytes()
                # Extract file extension and construct filename
                file_extension = os.path.splitext(blob_name)[1]

                # Sanitize the name by replacing spaces and dots with underscores
                sanitized_name = re.sub(r'[ .]', '_', image_details.name)

                # Create the response
                response = HttpResponse(file_content, content_type='application/octet-stream')
                if hasattr(image_details, 'upload_marks') and image_details.upload_marks:
                    response['Content-Disposition'] = f'attachment; filename="{sanitized_name}_{image_details.registration_number}{file_extension}"'
                else:
                    response['Content-Disposition'] = f'attachment; filename="{pk}_{sanitized_name}{file_extension}"'

                return response

    return render(request, 'error/404.html')


    
    
    
# def download_image(request, pk, blob_name):
#     storage_client = storage.Client()
#     bucket = storage_client.bucket(settings.BUCKET_NAME)
    
#     blob = bucket.blob(blob_name)

#     # Check if the object exists
#     if not blob.exists():
#         pass

#     # Fetch the file content
#     file_content = blob.download_as_bytes()
#     # Extract file extension and construct filename
#     file_extension = os.path.splitext(blob_name)[1]
#     # Create the response
#     response = HttpResponse(file_content, content_type='application/octet-stream')
#     response['Content-Disposition'] = f'attachment; filename="{pk}{file_extension}"'

#     return response



def generate_signed_url(blob_name, expiration=3600):
    """Generates a signed URL for a GCS object."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(settings.BUCKET_NAME)
    blob = bucket.blob(blob_name)

    # Ensure expiration is an integer
    expiration = int(expiration)

    url = blob.generate_signed_url(
        version="v4",
        expiration=timedelta(seconds=expiration),
        method="GET"
    )

    return url