import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QAction, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

# Main window class
class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()

        # Disable JavaScript
        self.browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)

        self.browser.setUrl(QUrl("https://"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # URL bar
        self.url_bar = QLineEdit()
        navbar.addWidget(self.url_bar)

        # Submit button
        submit_btn = QPushButton('Go', self)
        submit_btn.clicked.connect(self.navigate_to_url)
        navbar.addWidget(submit_btn)

        # Update URL bar with the current page's URL
        self.browser.urlChanged.connect(self.update_url)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith(('http://', 'https://')):
            url = 'http://www.google.com/search?q=' + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

# PyQt application
app = QApplication(sys.argv)
QApplication.setApplicationName('Python Browser')
window = BrowserWindow()
app.exec_()