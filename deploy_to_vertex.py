import os
from google.cloud import aiplatform

def deploy_model():
    # Initialize the Vertex AI client
    aiplatform.init(project='${{ secrets.GCP_PROJECT_ID }}', location='asia-south1')

    # Upload the model
    model = aiplatform.Model.upload(
        display_name='my-model',
        artifact_uri=f'gs://${{ secrets.GCS_BUCKET_NAME }}/random_forest_model.pkl',
        serving_container_image_uri=f'gcr.io/${{ secrets.GCP_PROJECT_ID }}/model-server:latest',
    )

    # Deploy the model to an endpoint
    endpoint = model.deploy(
        deployed_model_display_name='my-endpoint',
        machine_type='n1-standard-4',
        min_replica_count=1,
        max_replica_count=2,
    )

    print(f"Model deployed to endpoint: {endpoint.resource_name}")

if __name__ == '__main__':
    deploy_model()
