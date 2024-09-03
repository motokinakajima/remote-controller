import tkinter as tk
import socket
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        #self.ser = serial.Serial('/dev/tty.usbmodem111101',115200)
        self.master.title("ラジコン操作")     # ウィンドウタイトル

        #set ip address and port
        #==========================

        self.IPADDR = "192.168.0.1"
        hostname = 'kpcnavy.local'  # Replace with the desired hostname
        try:
            self.IPADDR = socket.gethostbyname(hostname)
            print(f"The IP address of {hostname} is: {self.IPADDR}")
        except socket.gaierror:
            print(f"Failed to resolve hostname: {hostname}")
            return
        self.PORT = 11452
        #==========================

        self.scale_var2 = tk.IntVar()
        scale2 = tk.Scale( self.master, 
                    variable = self.scale_var2, 
                    command = self.slider_scroll2,
                    orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                    length = 300,           # 全体の長さ
                    width = 20,             # 全体の太さ
                    sliderlength = 30,      # スライダー（つまみ）の幅
                    from_ = 0,            # 最小値（開始の値）
                    to = 255,               # 最大値（終了の値）
                    resolution=1,         # 変化の分解能(初期値:1)
                    tickinterval=50         # 目盛りの分解能(初期値0で表示なし)
                    )
        scale2.pack(side= tk.TOP)
        
    def slider_scroll2(self, event=None):
        '''スライダーを移動したとき'''
        output_data = self.scale_var2.get() + 90
        print_data2 = "!2<"
        print_data2 += str(output_data)
        print_data2 += ">."
        print(print_data2)
        self.sock = socket.socket(socket.AF_INET)
        self.sock.connect((self.IPADDR, self.PORT))
        self.data = print_data2

        self.sock.send(self.data.encode("utf-8")) 

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    #root.geometry("700x500")
    root.resizable(False, False)
    app.mainloop()