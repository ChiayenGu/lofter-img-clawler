保存喜欢的lofter博主的高清图片

==禁止商用！保存的高清大图仅作为个人欣赏，共享原则请按照原博主的要求！！！！本程序不对任何侵权行为负责==



因为有一些图片禁止右键，并且存图有水印，因此花一小会儿写了这个简单的爬虫。

之前写的那个丢了，现在需要用到feapder框架，等找到以前那个用requests写的再传上来吧

![image-20220513161231611](https://s2.loli.net/2022/05/13/yv2EdCJbSkc3WDx.png)

#### 使用方法

0. ~~安装需要的依赖~~

1. 打开`crawl_settings`文件，将地址和最大页数输入，默认在程序运行位置生成img文件夹并保存图片。

```
URL = 'https://kaninn.lofter.com/?page={}'
PAGEMAX = 23
SAVE_PATH = './img'
```

2. 运行`lofter_saveimg_spider.py`文件。



==禁止商用！保存的高清大图仅作为个人欣赏，共享原则请按照原博主的要求！！！！本程序不对任何侵权行为负责==