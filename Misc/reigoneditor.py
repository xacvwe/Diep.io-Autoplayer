import pyautogui

#Edit reigon to locate colors on certain reigon inside
im1 = pyautogui.screenshot(region=(0,70,1440,800)) #this is my reigon edit yours!!
im1.save(r"./reigon.png")
