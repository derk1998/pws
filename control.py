import pygame
import serial

ser = serial.Serial("COM10", 9600, timeout=1)
ser.setDTR(False)

pygame.init()
screen = pygame.display.set_mode((640, 400),0,32)
pygame.display.set_caption('Robot control')
done = False

gear = 1
gear2 = 1

reverse = 0
reverse2 = 0
while not done:
        for event in pygame.event.get():
                screen.fill((200,75,0))
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and gear == 1:
                        ser.write('b')
                    if event.key == pygame.K_w and gear == 2:
                        ser.write('c')
                    if event.key == pygame.K_w and gear == 3:
                        ser.write('d')
                    if event.key == pygame.K_w and gear == 4:
                        ser.write('e')
                    if event.key == pygame.K_w and gear == 5:
                        ser.write('f')
                    if event.key == pygame.K_w and gear == 6:
                        ser.write('g')
                    if event.key == pygame.K_w and gear == 7:
                        ser.write('h')
                    if event.key == pygame.K_1 and gear < 7:
                            gear = gear + 1
                            print gear
                    if event.key == pygame.K_2 and gear > 1:
                            gear = gear - 1
                            print gear
                            
                    if event.key == pygame.K_3 and reverse == 0:
                            ser.write("3")
                            reverse = 1
                            print "R1 aan"
                    if event.key == pygame.K_4 and reverse == 1:
                            ser.write("4")
                            reverse = 0
                            print "R1 uit"
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        ser.write('a')


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_o and gear2 == 1:
                        ser.write('B')
                    if event.key == pygame.K_o and gear2 == 2:
                        ser.write('C')
                    if event.key == pygame.K_o and gear2 == 3:
                        ser.write('D')
                    if event.key == pygame.K_o and gear2 == 4:
                        ser.write('E')
                    if event.key == pygame.K_o and gear2 == 5:
                        ser.write('F')
                    if event.key == pygame.K_o and gear2 == 6:
                        ser.write('G')
                    if event.key == pygame.K_o and gear2 == 7:
                        ser.write('H')
                    if event.key == pygame.K_9 and gear2 < 7:
                            gear2 = gear2 + 1
                            print gear2
                    if event.key == pygame.K_0 and gear > 1:
                            gear2 = gear2 - 1
                            print gear2
                    if event.key == pygame.K_7 and reverse2 == 0:
                            ser.write("7")
                            reverse2 = 1
                            print "R2 aan"
                    if event.key == pygame.K_8 and reverse2 == 1:
                            ser.write("8")
                            reverse2 = 0
                            print "R2 uit"
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_o:
                        ser.write('A')
                    

pygame.quit()
