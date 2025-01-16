import asyncio
import logging
import sys

from PyQt5.QtWidgets import QApplication, QListWidget, QVBoxLayout, QWidget

from db.database import post_plane
from get_data import get_planes_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FlightApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Китайские самолеты")
        self.setGeometry(250, 400, 1000, 600)
        self.layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)
        self.setLayout(self.layout)

        asyncio.run(self.load_data())

    async def load_data(self):
        data = await get_planes_data()
        await asyncio.sleep(10)
        post_plane(data)
        for flight in data:
            flight_id = flight['flightid']
            registration = flight['extraInfo']['reg']
            item_text = f"Flight ID: {flight_id},  Reg: {registration}"
            self.list_widget.addItem(item_text)

        logger.info(f'Добавлено новых самолетов:\n {data}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FlightApp()
    ex.show()
    sys.exit(app.exec_())
