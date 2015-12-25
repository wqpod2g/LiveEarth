import win32gui,win32con,win32api
import urllib.request
import time
import string
import os

base_url = "http://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/" #官网图片地址前半部分

cwd = os.getcwd() #当前目录

def set_desktop(pic_path):
        k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "0") #2拉伸适应桌面,0桌面居中
        win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,pic_path, 1+2)
        
#获取当前图片url
def getPic_url():
        date = time.strftime('%Y/%m/%d',time.localtime(time.time()))
        hour = int(time.strftime('%H',time.localtime(time.time())))-1
        if(hour<=8):
                hour_url = (hour+24-8)*10000
        else:
                hour_url = (hour-8)*10000

        if(hour_url<100000):
                hour_url = "0"+str(hour_url)
        else:
                hour_url = str(hour_url)
        pic_url = base_url+date+"/"+hour_url+"_0_0.png"
        print(pic_url)
        return pic_url

#下载图片
def down_pic(pic_url):
        conn = urllib.request.urlopen(pic_url)
        date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        hour = str(int(time.strftime('%H',time.localtime(time.time())))-1)
        pic_name = cwd+"\\downloads\\"+date+"-"+hour+".png"
        conn = urllib.request.urlopen(pic_url)  
        f = open(pic_name,'wb')
        f.write(conn.read())  
        f.close()  
        print(pic_name+' Saved!')
        return pic_name
        
def main():
        if not os.path.exists(cwd+"/downloads"):
                os.mkdir(cwd+"/downloads") 
        while True:
                pic_url = getPic_url()
                pic_name = down_pic(pic_url)
                set_desktop(pic_name)
                time.sleep(3600)
main()

