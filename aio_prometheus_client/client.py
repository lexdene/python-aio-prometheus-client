import time
from urllib.parse import urljoin

import httpx

DEFAULT_USER_AGENT = 'Python Aio Prometheus Client'


class PrometheusClient:
    def __init__(self, base_url, user_agent=DEFAULT_USER_AGENT):
        self.base_url = base_url
        self.user_agent = user_agent

    async def query(self, metric):
        async with httpx.AsyncClient() as client:
            r = await client.get(
                urljoin(self.base_url, 'api/v1/query'),
                params={
                    'query': metric,
                    'time': str(time.time())
                },
                headers={'User-Agent': self.user_agent},
            )

            r.raise_for_status()
            data = r.json()

        return data['data']['result']

    async def query_value(self, metric):
        data = await self.query(metric)
        return float(data[0]['value'][1])
