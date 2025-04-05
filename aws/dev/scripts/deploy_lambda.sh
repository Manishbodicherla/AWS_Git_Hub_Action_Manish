# deploy_lambda.sh
FUNCTION_NAME="my-lambda-dev"
ZIP_FILE="./aws/dev/lambda/Test_lambda1/deployment-package.zip"  # Path to deployment package

# Create deployment package
if [ ! -f "$ZIP_FILE" ]; then
    echo "Deployment package not found, creating zip..."
    cd ./aws/dev/lambda/function1 && zip -r ../deployment-package.zip *
    cd -
fi

# Deploy Lambda function
aws lambda update-function-code --function-name $FUNCTION_NAME --zip-file fileb://$ZIP_FILE
