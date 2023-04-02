=![](http://beisent.com/img/MicroDL/MicroDL-logo.jpg)

# MicroDL

**版本:** 0.2

**有用的链接:** [源代码](https://github.com/Yang-Junjie/MicroDL)

MicroDL(Micropython Drawing library)是一款可以支持Micropython的嵌入式设备上的画图库

# 入门

欢迎来到 MicroDL 的初学指南！如果您有任何意见或建议，请随时与我们联系！此文档只适用于MicroDL发布的最新版本.

## 下载 MicroDL

要下载 MicroDL，你需要前往我们的[Github源码库](https://github.com/Yang-Junjie/MicroDL)=>点击Code绿色按钮=>再点击Download ZIP下载，即可获得我们的源代码

## 如何导入 MicroDL

首先你需要将下载好的ZIP压缩包解压，这时候你会得到一个名为 `MicroDL.py`的文件，这正是我们的库文件，你只需要通过Thonny等其他方式将文件上传到你的嵌入式设备上，并且在同一文件路径上进行编程就行

要访问 MicroDL 及其函数，请将其导入您的 MicroPython 代码中，如下所示：

```python
>>>import MicroDL
```

## 开始使用 MicroDL

### 绝对坐标 与 相对坐标

`绝对坐标`：是以显示屏像素位置为坐标系的坐标，常规都是以显示屏的最左上角一个像素为坐标(1,1)

`相对坐标`：是以自行建立的坐标系的坐标

### 实例化一个 Graphics 对象

基本的画图操作都是由`Graphics`完成，可以使用以下代码创建一个`Graphics`对象，使用ST7789驱动的显示屏做例子。

```python
>>>display = st7789.ST7789(spi, cs=cs, dc=dc, rst=rst, width=width, height=height)    
>>>g = MicroDL.Graphics(display)#实例化一个Graphics对象
```

### Graphics对象属性

1. 画布宽度`width`：显示屏的宽度，默认从传入显示屏驱动器对象获取width属性
2. 画布高度`height`：显示器的高度，默认从传入显示屏驱动器对象获取height属性
3. 显示屏驱动器对象 `display` ：参数，它用于表示你要绘制的目标画布。这意味着你可以将 `Graphics` 类与不同类型的显示屏一起使用，只需确保该显示屏能够实现了相应的绘制函数即可。
4. 坐标原点`origin`：定义了一个自定义坐标系的原点，默认为`(120,120)`
5. 放缩比例`scale`：可以对自定义坐标系进行放缩，默认为`1`
6. x轴基底向量`x_unit`：自定义坐标系x轴的基底向量，你会绘制的每个坐标信息都是用向量表示出来的。默认为`(1,0)`
7. y轴基底向量`y_unit`：自定义坐标系y轴的基底向量，你会绘制的每个坐标信息都是用向量表示出来的。默认为`(0,-1)`
8. 背景颜色`background`：背景颜色，默认为`0x000000`

### set_axes 方法|设置坐标系参数

set_axes 方法 有三个参数需要传递：` origin, x_unit, y_unit,scale`

对应修改:自定义坐标系的原点，x轴基底向量，y轴基底向量，放缩比例.

```python
>>>g.set_axes((20,20),(2,0),(0,-2),1)
>>>print(g.origin,g.x_unit,g.x_unit,1)
(20,20),(2,0),(0,-2)
```

### transform_point 方法|将相对坐标转为绝对坐标

transform_point 方法有二个参数需要传递：`x，y`

返回值：`(int(canvas_x), int(canvas_y))`

分别对应：

x(相对坐标的横坐标)---->int(canvas_x)(绝对坐标的横坐标)

y(相对坐标的纵坐标)---->int(canvas_y)(绝对坐标的纵坐标)

```python
>>>print(g.transform_point(1,-1))
#基底向量已被重新设定
(40, 40)
```

### cls 方法|清屏操作

会以背景颜色清屏

```python
>>>draw.cls()
```

###  draw_axis 方法 | 绘制坐标系

 draw_axis 方法有五个参数：

`color (int, optional)`: 坐标轴以及刻度的颜色. 默认是 0xFFFFFF.

`grid (bool, optional)`: 是否需要绘制网格. 默认是 False.

`grid_color (int, optional)`: 网格的颜色. 默认是 0x696969.

`xlabel (str, optional)`: X轴标签文本.

` ylabel (str, optional)`: Y轴标签文本.

```python
>>>g.draw_axis(grid=True,xlabel = "x",ylabel = "y")
```

### plot 方法 | 绘制折线图

draw_axis 方法有三个参数：

` x_data (int):` 折线所有极值点按顺序排列的相对横坐标

` y_data (int): `折线所有极值点按顺序排列的相对纵坐标

` color (int):`折线的颜色.默认是 0xFFFFFF

```python
>>>g.plot([20,25,35,45,55,65,75,90,95],[-20,-10,-20,-10,-20,-10,-20,-10,-20])
```

### draw_point 方法 |绘制点

draw_point 方法有三个参数：

 `x (int): `点的相对横坐标

` y (int): `点的相对纵坐标

 `color (int, optional): `点的颜色. 默认是 0xFFFFFF.

```python
>>>g.draw_point(50,-5,0xFFFF0F)
```

### draw_line 方法 |绘制线条

draw_line 方法有五个参数:

`x1 (int): `线起点的相对横坐标

` y1 (int): `线起点的相对纵坐标

` x2 (int): `线终点的相对横坐标

` y2 (int): `线终点的相对纵坐标

 `color (int, optional):` 线的颜色. 默认是 0xFFFFFF.

```python
>>>g.draw_line(10,-10,10,-100,0xFF00FF)
```

### draw_rect 方法 | 绘制矩形

draw_rect 方法有六个参数:

` x (int): `矩形左上角点的相对横坐标

`y (int): `矩形左上角点的相对纵坐标

`w (int): `矩形以左上角为起点向右延伸的长度(宽度)

`h (int): `矩形以左上角为起点向下延伸的长度(高度)

`color (int, optional):` 矩形的颜色. 默认是 0xFFFFFF.

`f (bool,optional):`是否需要填充

```python
>>>g.draw_rect(20,-20,150,150,0xFFFFF0,f=True)
>>>g.draw_rect(30,-30,110,80)
```

### draw_circle 方法|绘制圆形

draw_circle 方法有五个参数:

`x (int):` 圆心的相对横坐标

`y (int): `圆心的相对纵坐标

`r (int): `圆的半径

`color (int, optional): `圆形的颜色. 默认是 0xFFFFFF.

`f (bool,optional):`是否需要填充

```python
>>>g.draw_circle(58,-50,40,0xFFF000,f=True)
>>>g.draw_circle(58,-50,30,0x00000F)
```

### draw_scatter 方法|绘制散点图

draw_scatter方法有三个参数:

`x_data (list): `所有点按顺序排列的相对横坐标

`y_data (list): ` 所有点按顺序排列的相对纵坐标

`color (_type_, optional): `折线的颜色.默认是 0xFFFFFF

```python
>>>g.draw_scatter([38,48,58,68,78],[-80,-80,-80,-80,-80])
```

### draw_text 方法|绘制文字

draw_text 方法有四个参数:

text (str): 文字的内容，目前只支持英文，数字和标点

x (int): 文字第一个字母左上角的相对横坐标

y (int): 文字第一个字母左上角的相对纵坐标

color (_type_, optional): 文字的颜色. 默认是 0xFFFFFF.

```python
>>>g.draw_text("MicroDL",45,-48,0x00000F)
```

### show 方法|将已绘制的图像显示在屏幕上

```python
>>>g.show()
```

## 使用上述代码绘制出的效果

![](http://beisent.com/img/MicroDL/MicroDL_docsexample.jpg)
