# -url-
获取页面上所有url支持深度爬取
XY_JSFinder 使用文档

概述

XY_JSFinder 是一个Python脚本，用于从指定的网站或多个网站提取超链接，并支持将结果保存到本地文件。它提供了基本的网页爬取功能以及深度爬取选项。

功能

单个网站爬取：对指定的单个网站进行超链接爬取。
多个网站爬取：从文件中读取多个网站的URL，对每个网站进行超链接爬取。
深度爬取：对单个网站进行深入的链接爬取。
保存结果：将爬取的链接保存到指定的输出文件中。

使用方法

单个网站爬取：

命令格式：python XY_JSFinder.py -u [网站URL] -o [输出文件]
示例：python XY_JSFinder.py -u http://example.com -o output.txt

多个网站爬取：

命令格式：python XY_JSFinder.py -f [输入文件] -o [输出文件]
示例：python XY_JSFinder.py -f input.txt -o output.txt

深度爬取：

命令格式：python XY_JSFinder.py -u [网站URL] -o [输出文件] -d
示例：python XY_JSFinder.py -u http://example.com -o output.txt -d

参数说明

-u 或 --url：指定要爬取的单个网站URL。
-f 或 --file：指定包含多个网站URL的输入文件。
-o 或 --output：指定爬取结果的输出文件。
-d 或 --deep：启用深度爬取模式。

注意事项

确保您的使用符合法律法规和网站的爬取政策。
在进行深度爬取时，请注意不要对服务器造成过大负担。
安装脚本所需的Python库，如 requests 和 beautifulsoup4。
