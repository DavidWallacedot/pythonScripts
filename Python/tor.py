import sys, webbrowser,pyautogui,time

pyautogui.typewrite('cd Downloads/tor-browser_en-US')
pyautogui.press('enter')
pyautogui.typewrite('./start-tor-browser.desktop')
pyautogui.press('enter')
pyautogui.click(348,175)
time.sleep(5)
pyautogui.typewrite('https://www.youtube.com/user/AmRenVideos/videos')
pyautogui.ctrl+t
pyautogui.typewrite('')
