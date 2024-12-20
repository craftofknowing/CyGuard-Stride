
# TUTUS: A Serverless, AI-Driven Cyber Intelligence Platform

TUTUS is a cutting-edge cyber intelligence solution designed to augment cybersecurity teams by automating routine tasks, streamlining threat detection, and delivering actionable insights. Built on a serverless architecture and leveraging AI, TUTUS empowers analysts to detect and respond to threats more efficiently.

## Features

- **Serverless Architecture**: Scalable, cost-effective, and easy to maintain.
- **AI-Powered Threat Detection**: Utilizes Large Language Models (LLMs) for reasoning and summarization.
- **Semantic Search**: Integrates with Amazon Kendra for precise and context-aware log retrieval.
- **Daily Insights**: Provides automated daily digests of threats and anomalies.
- **Modular Design**: Decoupled components for ingestion, analysis, and reporting.

## Architecture

![Architecture Diagram](./architecture-diagram.png)

### Core Components

1. **Amazon S3 & CloudFront**: Hosts and delivers the static dashboard UI.
2. **API Gateway**: Routes secure requests between the front-end and back-end services.
3. **Lambda Functions**:
    - **IngestLogsLambda**: Processes and indexes log data.
    - **AnalyzeThreatsLambda**: Identifies threats using AI and semantic search.
    - **GetDashboardLambda**: Summarizes threats for the daily dashboard.
4. **Amazon Kendra**: Powers semantic search for log data.
5. **Amazon Bedrock**: Provides AI capabilities for threat detection and insights.
6. **DynamoDB**: Stores logs and detected threats.

## Installation

### Prerequisites

- AWS CLI configured with proper IAM permissions.
- Terraform for Infrastructure as Code (IaC).
- Python 3.8+ for Lambda functions.

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/tutus.git
   cd tutus
   ```

2. Deploy infrastructure using Terraform:
   ```bash
   terraform init
   terraform apply
   ```

3. Package and deploy Lambda functions:
   ```bash
   cd lambdas
   ./deploy.sh
   ```

4. Upload the static dashboard to S3:
   ```bash
   aws s3 sync ./dashboard s3://your-s3-bucket-name
   ```

5. Access the dashboard via the CloudFront URL.

## Usage

- **Log Ingestion**: Send log data to the `/ingest` endpoint.
- **Threat Analysis**: Query the `/analyze` endpoint for detected threats.
- **Daily Dashboard**: Access the dashboard UI to view summarized insights.

## Roadmap

- **Short-Term Goals**:
    - Fine-tune LLMs on internal threat data.
    - Add more OSINT data sources.
- **Mid-Term Goals**:
    - Implement feedback loops for continuous learning.
    - Introduce explainable AI capabilities.
- **Long-Term Vision**:
    - Enable semi-autonomous threat detection and response.

## Contributing

We welcome contributions! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- OpenAI for advancements in LLM technology.
- AWS for serverless infrastructure and AI services.
- The open-source community for tools and frameworks that made this project possible.

---

For detailed documentation, please refer to the [Wiki](https://github.com/your-username/tutus/wiki).
