# k6 load testing

## Installation
https://k6.io/docs/getting-started/installation/

go install go.k6.io/xk6/cmd/xk6@latest

xk6 build --with github.com/grafana/xk6-output-prometheus-remote@latest

## Usage
K6_PROMETHEUS_REMOTE_URL=http://localhost:9090/api/v1/write ./k6 run script.js -o output-prometheus-remote