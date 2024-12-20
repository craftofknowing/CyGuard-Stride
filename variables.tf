variable "region" {
  default = "us-east-1"
}

variable "bucket_name" {
  default = "tutus-ai-logs"
}

variable "lambda_function_name" {
  default = "TutusFileProcessor"
}

variable "api_gateway_name" {
  default = "TutusAPI"
}
