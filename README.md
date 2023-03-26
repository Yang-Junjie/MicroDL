=![](http://beisent.com/img/MicroDL/MicroDL-logo.jpg)

# MicroDL

**版本:** 0.1

**有用的链接:** [源代码](https://github.com/Yang-Junjie/MicroDL)

MicroDL(Micropython Drawing library)是一款可以支持Micropython的嵌入式设备上的画图库

# 入门

欢迎来到 MicroDL 的初学指南！如果您有任何意见或建议，请随时与我们联系！

## 下载 MicroDL

要下载 MicroDL，你需要前往我们的[Github源码库](https://github.com/Yang-Junjie/MicroDL)=>点击Code绿色按钮=>再点击Download ZIP下载，即可获得我们的源代码

## 如何导入 MicroDL

首先你需要将下载好的ZIP压缩包解压，这时候你会得到一个名为 `MicroDL.py`的文件，这正是我们的库文件，你只需要通过Thonny等其他方式将文件上传到你的嵌入式设备上，并且在同一文件路径上进行编程就行

要访问 MicroDL 及其函数，请将其导入您的 MicroPython 代码中，如下所示：

```python
>>>import MicroDL
```

## 开始使用 MicroDL

### 实例化一个Graphics对象

基本的画图操作都是由`Graphics`完成，可以使用以下代码创建一个`Graphics`对象，使用ST7789驱动做例子

```python
>>>display = st7789.ST7789(spi, cs=cs, dc=dc, rst=rst, width=width, height=height)    
>>>g = MicroDL.Graphics(display)#实例化一个Graphics对象
```

### Graphics对象属性

1. 画布宽度：`width`显示屏的宽度
2. 画布高度：`height`显示器的高度
3. 屏幕驱动器对象： `display` 参数，它用于表示你要绘制的目标画布。这意味着你可以将 `Graphics` 类与不同类型的显示屏幕一起使用，只需确保该屏幕实现了相应的绘制函数即可。
4. 坐标原点：`origin`定义了一个坐标轴的原点
5. x轴单位向量：一个x轴的单位向量
6. y轴单位向量：一个y轴的单位向量
7. 背景颜色：`background`背景颜色使用16进制

### 清屏操作

会以背景颜色清屏

```python
>>>draw.cls()
```

