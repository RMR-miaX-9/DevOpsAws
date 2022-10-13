import boto3

aws_region = "eu-west-3"
textract = boto3.client("textract", region_name=aws_region)

textract.start_document_text_detection(
    DocumentLocation={
        "S3Object": {
            "Bucket": "test-20221007-rmr",      # Bucket de entrada
            "Name": "textract_input_file.jpg"   # Fichero a procesar (png, pdf, ...)
        }
    },
    #NotificationChannel={"RoleArn": rolearn, "SNSTopicArn": snstarn},
    OutputConfig={
        "S3Bucket": "test-20221007-rmr",    # Bucker de salida
        "S3Prefix": "textract_output_file"  # Nombre de la carpeta donde se generarán los ficheros de salida
    },
)
