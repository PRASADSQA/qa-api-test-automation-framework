# QA API Test Automation Framework

## 📌 Overview
This project demonstrates a scalable API test automation framework using Postman and Newman with environment-based configuration.

## 🚀 Features
- Environment-based configuration (no hardcoding)
- Dynamic test data generation
- API automation (GET, POST)
- CLI execution using Newman
- HTML test reporting
- CI/CD integration using GitHub Actions

## 🛠 Tools Used
- Postman
- Newman
- Node.js
- GitHub Actions

## 📂 Project Structure
qa-api-test-automation-framework/
│── collection.json  
│── qa-env.json  
│── report.html  
│── .github/workflows/api-tests.yml  

## ▶️ How to Run Locally

### Install dependencies
```bash
npm install -g newman newman-reporter-html
