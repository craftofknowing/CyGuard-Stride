output "s3_bucket_name" {
  value = aws_s3_bucket.tutus_logs.bucket
}

output "lambda_function_arn" {
  value = aws_lambda_function.file_processor.arn
}

output "api_gateway_endpoint" {
  value = aws_apigatewayv2_stage.api_stage.invoke_url
}
