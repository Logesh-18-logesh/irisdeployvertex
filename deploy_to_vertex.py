import os
from google.cloud import aiplatform

def deploy_model():
    # Initialize the Vertex AI client
    project_id = os.getenv('GCP_PROJECT_ID')
    bucket_name = os.getenv('GCS_BUCKET_NAME')

    aiplatform.init(project=project_id, location='asia-south1')

    # Upload the model
    model = aiplatform.Model.upload(
        display_name='my-model',
        artifact_uri=f'gs://{bucket_name}/random_forest_model.pkl',
        serving_container_image_uri=f'asia-south1-docker.pkg.dev/{project_id}/model-server/img:latest',
    )

    model.wait()  # Wait for the model to finish uploading

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
