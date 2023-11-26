import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt, QTimer, QPoint

def lerp(a, b, n):
    return (1 - n) * a + n * b


class MouseTrackerLabel(QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        # 创建一个无边框、置顶、半透明的窗口
        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.WindowStaysOnTopHint | Qt.WindowTransparentForInput)
        self.setWindowOpacity(0.9)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def move_to_mouse(self):
        b = self.pos()
        c = QCursor.pos() - QPoint(self.width() // 2, self.height() // 2) - b
        d = 100
        for t in range(1, d + 1):
            self.move(b + c * t / d)
            QApplication.processEvents()

    def smooth_move(self):
        target_pos = QCursor.pos() - QPoint(self.width() // 3, self.height() // 3)
        current_pos = self.pos()

        # 计算平滑移动的下一个位置
        next_pos = QPoint(
            int(lerp(current_pos.x(), target_pos.x(), 0.1)),
            int(lerp(current_pos.y(), target_pos.y(), 0.1))
        )

        # 移动窗口到鼠标中心
        self.move(next_pos)
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
    # 将QTimer对象的timeout信号连接到label的smooth_move槽函数
    timer.timeout.connect(label.smooth_move)
    # 启动定时器
    timer.start(10)
    # 进入应用程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())