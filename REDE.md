<div class="grid-cols-1 grid gap-2.5 [&amp;_>_*]:min-w-0 space-y-4"><h1 class="font-600 text-2xl font-bold" level="1">Electronic Components Scraper</h1>
<h2 class="font-600 text-xl font-bold" level="2">项目描述</h2>
<p class="whitespace-pre-wrap break-words">聚合电子元器件数据，从 DigiKey 和 ICSource 网站抓取产品信息、库存和热度数据。</p>
<h2 class="font-600 text-xl font-bold" level="2">环境准备</h2>
<ol class="-mt-1 [li>&amp;]:mt-2 list-decimal space-y-2 pl-8" depth="0">
<li class="whitespace-normal break-words" index="0">Python 3.8+</li>
<li class="whitespace-normal break-words" index="1">MongoDB</li>
<li class="whitespace-normal break-words" index="2">安装依赖: <code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.3rem] px-1 py-px text-[0.9rem]">pip install -r requirements.txt</code></li>
</ol>
<h2 class="font-600 text-xl font-bold" level="2">配置</h2>
<ol class="-mt-1 [li>&amp;]:mt-2 list-decimal space-y-2 pl-8" depth="0">
<li class="whitespace-normal break-words" index="0">修改 <code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.3rem] px-1 py-px text-[0.9rem]">config.py</code>
<ul class="-mt-1 [li>&amp;]:mt-2 list-disc space-y-2 pl-8" depth="1">
<li class="whitespace-normal break-words" index="0">设置 MongoDB 连接</li>
<li class="whitespace-normal break-words" index="1">添加 ICSource 登录凭据</li>
</ul>
</li>
</ol>
<h2 class="font-600 text-xl font-bold" level="2">运行</h2>
<pre><div class="relative flex flex-col rounded-lg"><div class="text-text-300 absolute pl-3 pt-2.5 text-xs">bash</div><div class="pointer-events-none sticky my-0.5 ml-0.5 flex items-center justify-end px-1.5 py-1 mix-blend-luminosity top-0"><div class="from-bg-300/90 to-bg-300/70 pointer-events-auto rounded-md bg-gradient-to-b p-0.5 backdrop-blur-md"><button class="flex flex-row items-center gap-1 rounded-md p-1 py-0.5 text-xs transition-opacity delay-100 hover:bg-bg-200 opacity-60 hover:opacity-100"><svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" viewBox="0 0 256 256" class="text-text-500 mr-px -translate-y-[0.5px]"><path d="M200,32H163.74a47.92,47.92,0,0,0-71.48,0H56A16,16,0,0,0,40,48V216a16,16,0,0,0,16,16H200a16,16,0,0,0,16-16V48A16,16,0,0,0,200,32Zm-72,0a32,32,0,0,1,32,32H96A32,32,0,0,1,128,32Zm72,184H56V48H82.75A47.93,47.93,0,0,0,80,64v8a8,8,0,0,0,8,8h80a8,8,0,0,0,8-8V64a47.93,47.93,0,0,0-2.75-16H200Z"></path></svg><span class="text-text-200 pr-0.5">Copy</span></button></div></div><div><div class="code-block__code !my-0 !rounded-lg !text-sm !leading-relaxed" style="background: rgb(40, 44, 52); color: rgb(171, 178, 191); text-shadow: rgba(0, 0, 0, 0.3) 0px 1px; font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.5; tab-size: 2; hyphens: none; padding: 1em; margin: 0.5em 0px; overflow: auto; border-radius: 0.3em;"><code class="language-bash" style="background: rgb(40, 44, 52); color: rgb(171, 178, 191); text-shadow: rgba(0, 0, 0, 0.3) 0px 1px; font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.5; tab-size: 2; hyphens: none;"><span><span>python main.py</span></span></code></div></div></div></pre>
<h2 class="font-600 text-xl font-bold" level="2">数据存储</h2>
<ul class="-mt-1 [li>&amp;]:mt-2 list-disc space-y-2 pl-8" depth="0">
<li class="whitespace-normal break-words" index="0">DigiKey 产品信息存储在 <code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.3rem] px-1 py-px text-[0.9rem]">digikey_products</code> 集合</li>
<li class="whitespace-normal break-words" index="1">ICSource 库存信息存储在 <code class="bg-text-200/5 border border-0.5 border-border-300 text-danger-000 whitespace-pre-wrap rounded-[0.3rem] px-1 py-px text-[0.9rem]">icsource_inventory</code> 集合</li>
</ul>
<h2 class="font-600 text-xl font-bold" level="2">注意事项</h2>
<ul class="-mt-1 [li>&amp;]:mt-2 list-disc space-y-2 pl-8" depth="0">
<li class="whitespace-normal break-words" index="0">网站结构变化可能导致抓取失败</li>
<li class="whitespace-normal break-words" index="1">遵守网站的 robots.txt 和使用条款</li>
<li class="whitespace-normal break-words" index="2">建议添加代理和延时以避免被屏蔽</li>
</ul></div>
