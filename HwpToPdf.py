import os
import win32com.client as win32
import win32gui

hwpDir = "C:\\Users\\gmlwn\\Desktop\\hwp_to_pdf\\physics\\"
os.chdir(hwpDir)
print(os.listdir())

hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwnd = win32gui.FindWindow(None, 'Noname 1 - HWP')

print(hwnd)

win32gui.ShowWindow(hwnd, 0)

for i in os.listdir():
    hwp.Open(os.path.join(hwpDir, i))
    hwp.SaveAs(hwpDir+"\\"+i+".pdf", "PDF")


win32gui.ShowWindow(hwnd, 5)
hwp.Quit()