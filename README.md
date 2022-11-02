# Asyncio Prometheus Client

Prometheus Http Client for Asyncio of Python

## install

    pip install aio-prometheus-client

## usage

    from aio_prometheus_client import PrometheusClient

    client = PrometheusClient('http://127.0.0.1:9090')
    result = await client.query('http_requests_total')

    for s in result.series:
        print(s.metric, s.value.timestamp, s.value.value)
