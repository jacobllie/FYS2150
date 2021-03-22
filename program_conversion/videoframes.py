"""
Dette programmet spiller av en video frame by frame, ved å legge til hver
enkelt frame i en liste, for deretter å loope gjennom den manuelt.
l = framover
j = bakover
q = quit
"""

import cv2
#vet ikke helt hva slags filformat som støttes av VideoCaptur
cap = cv2.VideoCapture("penal.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count/fps

print("--------Video info--------")
print("fps = {:.3} 1/s\ntot frames = {} \nDuration = {:.3} s".format(fps,frame_count,duration))

check = True

frame_list = []
while(check == True):
    #read() returnerer True helt til siste frame, og den returnerer
    #data for hvert enkelt frame
    check , frame = cap.read()
    frame_list.append(frame)

# siste verdien i frame list er None
# vi må derfor fjerne den med pop

frame_list.pop()
frame_num = 0

#loopen som gjør det mulig å manuelt manøvrere seg gjennom frames
while frame_num < frame_count:
    cv2.imshow("Frame",frame_list[frame_num])
    print(frame_num)

    key = cv2.waitKey(0)

    while key not in [ord('q'), ord('l'), ord("j")]:
        key = cv2.waitKey(0)
    if key == ord("l"):
            frame_num += 1
    if key == ord("j") and frame_num != 0:
            frame_num -= 1
    # Quit when 'q' is pressed
    if key == ord('q'):
            break
#når videoen er ferdig avspilt, så lukkes vinduet automatisk.
cap.release()
cv2.destroyAllWindows()
