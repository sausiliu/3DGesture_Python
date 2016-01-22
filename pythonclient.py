import serial, pygame, time, string, sys
import xlrd
import xlwt


class eMPL_packet_reader:
    #    def __init__(self, port, quat_delegate=None, debug_delegate=None, data_delega=None):
    def __init__(self, port):
        self.s = serial.Serial(port, 115200, timeout=0.1, write_timeout=0.2)

    def read(self):
        NUM_BYTES = 23
        p = None
        while self.s.inWaiting() > NUM_BYTES:
            rs = self.s.read(NUM_BYTES)
            if ord(rs[0]) == ord('$'):
                print("received a character c ")

    def write(self):
        self.s.write(a)

    def close(self):
        self.s.close()

    def set_excel_style(name, height, bold=False):
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = name
        font.bold = bold
        font.colour_index = 4
        font.height = height

        style.font = font
        return style

    def write_excel(self):
        file = xlwt.Workbook()
        sheet1 = file.add_sheet(u'sheet1', cell_overwrite_ok=True)

        file.save('test.xlsx')


# ============MAIN============
if __name__ == "__main__":
    if len(sys.argv) == 2:
        comport = sys.argv[1]
    else:
        print("usage : " + sys.argv[0] + " comx")
        exit(-1)

    pygame.init()
    reader = eMPL_packet_reader(comport)

    reader.write_excel()
