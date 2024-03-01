## Kubikware Challenge

###### Lambda Script that is triggered by a URL, through which it generates a Dictionary with State as the key and associated counties as the values

## Installation of Pycharm, AWS SAM, and AWS CLI (Optional) for local execution

* 1. **__Install Pycharm, AWS SAM, and AWS CLI__** to run the script and test it locally. I'm sharing the folder **__Lambda_app_aws_sam__** with the Pycharm environment pre-configured. You only need to change the region where your account is located, as the credentials are automatically associated through Pycharm. The version of AWS SAM used by Pycharm is licensed, but a 30-day free trial is available to test and execute the solution. Docker Desktop also needs to be installed.


## Installation of Pycharm or any other IDE to execute the solution

* 2. **__Install Pycharm, Visual Studio or another IDE, and Docker.__** If you are going to run the script in Pycharm or another IDE, it's recommended to use Docker to dockerize the image of the lambda for direct deployment to the AWS account. For this, it's also necessary to have the credentials, which can also be configured through AWS CLI. This is a generic solution without implementing AWS SAM and AWS CLI.


The default Python libraries used in this project are: json, time, and logging
I did not use credentials since all the development was adapted to a Lambda in AWS, so it was not necessary. Also, to test it locally I used AWS SAM and AWS CLI.

* 3. Have the following libraries installed: **_pandas, and requests_** 

* 4. The default Python libraries used in this project are: **_json, time y logging_** 

* 5. I did not use credentials since all the development was adapted to a Lambda in AWS, so it was not necessary. Also, to test it locally I used AWS SAM and AWS CLI.