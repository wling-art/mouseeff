import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt, QTimer, QPoint


class MouseTrackerLabel(QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        # 创建一个无边框、置顶、半透明的窗口
        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.WindowStaysOnTopHint | Qt.WindowTransparentForInput)  # 设置窗口标志，使其无边框、置顶、不影响鼠标点击
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明

    def move_to_mouse(self):
        b = self.pos()
        c = QCursor.pos() - QPoint(self.width() // 2, self.height() // 2) - b
        d = 100
        for t in range(1, d + 1):
            self.move(b + c * t / d)
            QApplication.processEvents()


if __name__ == '__main__':
    # 创建一个应用程序对象
    app = QApplication(sys.argv)
    # 创建一个QPixmap对象
    pixmap = QPixmap("image/mouse.png")
    # 创建一个MouseTrackerLabel对象
    label = MouseTrackerLabel()
    # 设置标签的图像
    label.setPixmap(pixmap)
    # 设置标签的固定大小
    label.setFixedSize(pixmap.size())
    # 显示标签
    label.show()
    # 创建一个QTimer对象
    timer = QTimer()
    # 将QTimer对象的timeout信号连接到label的move_to_mouse槽函数
    timer.timeout.connect(label.move_to_mouse)
    # 启动定时器
    timer.start(10)
    # 进入应用程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
