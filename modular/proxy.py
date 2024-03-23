import socket
import time

import requests
import socks
from bs4 import BeautifulSoup

from Mix import *

__modles__ = "Proxy"
__help__ = get_cgr("help_prox")


async def measure_latency(proxy_address):
    try:
        start_time = time.time()
        with socks.socksocket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.set_proxy(socks.SOCKS5, proxy_address[0], int(proxy_address[1]))
            sock.settimeout(5)
            sock.connect(("www.google.com", 80))
        latency = time.time() - start_time
        return latency
    except Exception as e:
        print(f"Failed to measure latency for {proxy_address}: {e}")
        return float("inf")


def scrape_proxies():
    proxies = []
    try:
        url = "https://proxyscrape.com/free-proxy-list"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        proxy_rows = soup.find_all("td")
        for row in proxy_rows[1:]:
            columns = row.find_all("tr")
            if len(columns) >= 2:
                host = columns[0].text.strip()
                port = columns[1].text.strip()
                country = columns[5].text.strip()
                proxies.append((host, port, country))
    except Exception as e:
        print(f"Failed to scrape proxies: {e}")
    return proxies


async def find_best_proxies(proxies):
    best_proxies = []

    for proxy in proxies:
        host, port, country = proxy
        latency = await measure_latency((host, port))
        best_proxies.append((host, port, latency, country))

    best_proxies.sort(key=lambda x: x[2])

    return best_proxies[:2]



@ky.ubot("proxy", sudo=True)
async def get_proxies(client, message):
    em = Emojik()
    em.initialize()
    pros = await message.reply(cgr("proses").format(em.proses))
    try:
        scraped_proxies = scrape_proxies()

        best_proxies = await find_best_proxies(scraped_proxies)

        if best_proxies:
            response = f"**{em.sukses} Top 2 best of list Proxy:**\n"
            for i, (proxy, port, latency, country) in enumerate(best_proxies, start=1):
                response += f"**{i}. Negara : `{country}` | `{proxy}:{port}` - Latensi: `{round(latency, 2)}` detik\n"

            await message.reply_text(response)
            await pros.delete()
        else:
            await message.reply(cgr("err").format(em.gagal))
            await pros.delete()
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
        await pros.delete()
    await pros.delete()
