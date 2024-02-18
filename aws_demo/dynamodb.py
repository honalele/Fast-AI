import boto3

dynamodb = boto3.client("dynamodb")
print(dynamodb)

put_response = dynamodb.put_item(
    TableName="ZipcodeWeather",
    Item={
        "Zipcode": {"S": "90210"},
        "Temprature": {"N": "25"},
        "HumidityPercent": {"N": "25"},
    }
)

scan_response = dynamodb.scan(TableName="ZipcodeWeather")
print(scan_response)

query_response = dynamodb.query(
    TableName="ZipcodeWeather",
    KeyConditionExpression="Zipcode = :zipcode",
    ExpressionAttributeValues={
        ":zipcode": {"S": "90210"}
    }
)
print(query_response)
