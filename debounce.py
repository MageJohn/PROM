import time
#initialise a previous input variable to 0 (assume button not pressed last)
prevInput = 0
while True:
  #take a reading
  newInput = GPIO.input(17)#will be whatever port we use
  #if the previous input is different to this input the button has been pressed
  if ((not prevInput) and newInput):
    print("Button pressed")
  #update previous input
  prevInput = input
  #delay to debounce the button for 0.05s
  time.sleep(0.05)
