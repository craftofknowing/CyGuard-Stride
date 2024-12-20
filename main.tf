provider "aws" {
  region = var.region
}

provider "random" {
    
}

module "s3" {
  source = "./moduless3.tf"
}

module "lambda" {
  source = "./lambda.tf"
}

module "api_gateway" {
  source = "./modulesapi_gateway.tf"
}
