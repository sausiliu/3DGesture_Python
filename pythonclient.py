import serial, pygame, time, string, sys
import xlrd
import xlwt

class eMPL_packet_reader:
    def __init__(self, port, quat_delegate=None, debug_delegate=None, data_delega=None):
        self.s = serial.Serial(port, 115200, timeout=0.1, write_timeout=0.2)

    # TODO: Will this break anything?
    ##Client attempts to write to eMPL.
    # try:
    # self.s.write("\n")
    # except serial.serialutil.SerialTimeoutException:
    # pass # write will timeout if umpl app is already started.
    if quat_delegate:
        self.quat_delegate = quat_delegate
    else:
        self.quat_delegate = empty_packet_delegate()

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
        '''
        create the first sheet
        '''
        sheet1 = file.add_sheet(u'sheet1', cell_overwrite_ok=True)
        row0 = [u'x', u'y', u'z']

        for i in range(0, len(row0)):
            sheet1.write(0, i, row0[i])
        # write(self, col, label, style=Style.default_style):

        file.save('test.xls')


# ============ PACKET DELEGATES ============
class packet_delegate(object):
    def loop(self, event):
        print("generic packet delegate loop w/event", event)


class cube_packet_viewer(packet_delegate):
    def __init__(self):
        self.screen = Screen(480, 400, scale=1.5)


# ============MAIN============
if __name__ == "__main__":
    if len(sys.argv) == 2:
        comport = sys.argv[1]
    else:
        print("usage : " + sys.argv[0] + " comx")
        exit(-1)

    pygame.init()
    viewer = cube_packet_viewer()

    reader = eMPL_packet_reader(comport,
                                quat_delegate=viewer)
    reader.set_excel_style('Times New Roman')

    reader.write_excel()
