"""
=========
 MicroDL
=========
MicroDL(Micropython Drawing library)是一款可以支持Micropython的嵌入式设备上的画图库

使用时需要将此文件库上传到你的嵌入式设备上，并且在你的主文件中加入以下代码：
import MicroDL as MDL

目前只包括Graphics模块
所有的基本绘制工作都有这个模块完成
"""


class Graphics:
    """
    Graphics包含了绘制坐标系、文字和基本图形的任务
    自身属性：
    画布宽度：width
    画布高度：height
    屏幕驱动器对象：display

    坐标原点：origin
    x轴单位向量：x_unit
    y轴单位向量：y_unit
    #背景颜色：background
    ======================
    自身方法：
    设置坐标系参数：
    ~.set_axes()
    坐标的转换操作：
    ~.transform_point()
    清屏：
    ~.cls()
    绘制坐标系：
    ~.draw_axis()
    显示:
    ~.show()
    图形包括：
    折线：~.plot()
    点：~.draw_point()
    线：~.draw_line()
    矩形：~.draw_rect()
    圆：~.draw_circle()
    文字包括：
    文字：~.draw_text()

    """

    def __init__(self, display):
        self.width = display.width
        self.height = display.height
        self.display = display

        self.origin = (120, 120)  # 坐标轴原点
        self.x_unit = (1, 0)   # x轴单位向量
        self.y_unit = (0, -1)  # y轴单位向量

        self.background_color = 0x000000  # 背景颜色

    def set_axes(self, origin, x_unit, y_unit):
        # 设置坐标系参数
        self.origin = origin
        self.x_unit = x_unit
        self.y_unit = y_unit

    def transform_point(self, x, y):
        # 将坐标轴上的点转换为画布上的点
        canvas_x = self.origin[0] + x * self.x_unit[0] + y * self.y_unit[0]
        canvas_y = self.origin[1] + x * self.x_unit[1] + y * self.y_unit[1]
        return (int(canvas_x), int(canvas_y))

    def cls(self):
        """
        清屏,以背景颜色清屏
        """
        self.display.fill(self.background_color)

    def draw_axis(self, color=0xFFFFFF, grid=False, grid_color=0xF0F000):
        """绘制坐标系

        参数:
            color (int, optional): 坐标轴以及刻度的颜色. 默认是 0xFFFFFF.
            grid (bool, optional): 是否需要绘制网格. 默认是 False.
            grid_color (int, optional): 网格的颜色. 默认是 0xF0F000.
        """
        if grid == True:
            for x in range(10, self.width, 10):
                if x == self.origin[0]:
                    continue
                self.display.line(x, 0, x, self.height, grid_color)
            for y in range(10, self.height, 10):
                if y == self.origin[1]:
                    continue
                self.display.line(0, y, self.width, y, grid_color)

        self.display.hline(0, self.origin[1], self.width, color)
        self.display.vline(self.origin[0], 0, self.height, color)
        # 绘制水平刻度
        for i in range(-self.origin[0], self.width-self.origin[0], 10):
            self.display.pixel(i+self.origin[0], self.origin[1]-2, color)
            self.display.pixel(i+self.origin[0], self.origin[1]+2, color)

        # 绘制竖直刻度
        for i in range(-self.origin[1], self.height-self.origin[1], 10):
            self.display.pixel(self.origin[0]-2, i+self.origin[1], color)
            self.display.pixel(self.origin[0]+2, i+self.origin[1], color)

    def plot(self, x_data, y_data, color=0xFFFFFF):
        """ 绘制折线图

        Args:
            x_data (int): 折线所有极值点按顺序排列的横坐标
            y_data (int): 折线所有极值点按顺序排列的纵坐标
            color (int): 折线的颜色.默认是 0xFFFFFF
        """
        coords = list(zip(x_data, y_data))
        for i in range(len(coords) - 1):
            x1, y1 = self.transform_point(coords[i][0], coords[i][1])
            x2, y2 = self.transform_point(coords[i+1][0], coords[i+1][1])
            self.display.line(x1, y1, x2, y2, color)

    def draw_point(self, x, y, color=0xFFFFFF):
        """绘制点

        Args:
            x (int): 点的横坐标
            y (int): 点的纵坐标
            color (int, optional): 点的颜色. 默认是 0xFFFFFF.
        """
        point = self.transform_point(x, y)
        self.display.pixel(point[0], point[1], color)

    def draw_line(self, x1, y1, x2, y2, color=0xFFFFFF):
        """绘制线条

        Args:
            x1 (int): 线起点的横坐标
            y1 (int): 线起点的纵坐标
            x2 (int): 线终点的横坐标
            y2 (int): 线终点的纵坐标
            color (int, optional): 线的颜色. 默认是 0xFFFFFF.
        """
        point_1 = self.transform_point(x1, y1)
        point_2 = self.transform_point(x2, y2)
        self.display.line(point_1[0], point_1[1],
                          point_2[0], point_2[1], color)

    def draw_rect(self, x, y, w, h, color=0xFFFFFF):
        """绘制矩形

        Args:
            x (int): 矩形左上角点的横坐标
            y (int): _description_
            w (int): _description_
            h (int): _description_
            color (int, optional): _description_. Defaults to 0xFFFFFF.
        """
        point = self.transform_point(x, y)
        self.display.rect(point[0], point[1], w, h, color)

    def draw_circle(self, x, y, r, color=0xFFFFFF):
        # 将圆心坐标转换为显示屏上的坐标
        point = self.transform_point(x, y)
        x_disp = point[0]
        y_disp = point[1] - 1
        # 初始化绘制参数
        x0 = r
        y0 = 0
        d = 3 - 2 * r
        # 使用 Bresenham 算法绘制圆
        while x0 >= y0:
            self.display.pixel(x_disp + x0, y_disp + y0, color)
            self.display.pixel(x_disp + y0, y_disp + x0, color)
            self.display.pixel(x_disp - y0, y_disp + x0, color)
            self.display.pixel(x_disp - x0, y_disp + y0, color)
            self.display.pixel(x_disp - x0, y_disp - y0, color)
            self.display.pixel(x_disp - y0, y_disp - x0, color)
            self.display.pixel(x_disp + y0, y_disp - x0, color)
            self.display.pixel(x_disp + x0, y_disp - y0, color)
            y0 += 1
            if d > 0:
                x0 -= 1
                d += 4 * (y0 - x0) + 10
            else:
                d += 4 * y0 + 6

    def draw_text(self, text, x, y, color=0xFFFFFF):
        point = self.transform_point(x, y)
        self.display.text(text, point[0], point[1], color)

    def show(self):
        # 将已绘制的图像显示在屏幕上
        self.display.show()
