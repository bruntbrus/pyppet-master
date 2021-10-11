# Control browser with Pyppeteer.

import asyncio
from pyppeteer import launch


async def main():
  browser = await launch()
  page = await browser.newPage()
  await page.goto('http://vecka.nu')
  # await page.screenshot({'path': 'out/example.png'})

  dimensions = await eval_js_function('getDimensions', page)

  print(dimensions)

  await browser.close()


async def eval_js_function(function_name, page):
  js_code = ''

  with open(f'js/{function_name}.js', 'r') as js_file:
    js_code = js_file.read()

  return await page.evaluate(js_code)


if __name__ == '__main__':
  asyncio.get_event_loop().run_until_complete(main())
