import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = os.environ.get("AWS_S3_ENDPOINT_URL")
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")

# Supabase requires path-style addressing for S3
AWS_S3_ADDRESSING_STYLE = "path"

# --- ADD THESE TWO LINES ---
# This forces Django to use Supabase's public web URL format
AWS_S3_CUSTOM_DOMAIN = f"umsznczaiuftxjoqfpja.supabase.co/storage/v1/object/public/{AWS_STORAGE_BUCKET_NAME}"
# This stops Django from attaching ugly security signatures to your CSS URLs
AWS_QUERYSTRING_AUTH = False
# ---------------------------


AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}

# ADD THIS INSTEAD:
STORAGES = {
    "default": {
        "BACKEND": "cdn.backends.MediaRootS3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "cdn.backends.StaticRootS3Boto3Storage",
    },
}