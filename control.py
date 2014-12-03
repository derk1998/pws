import pygame
import serial

port = (raw_input("Port: "))
ser = serial.Serial(port, 9600, timeout=1)
ser.setDTR(False)

pygame.init()
screen = pygame.display.set_mode((640, 400),0,32)
pygame.display.set_caption('Robot control')
done = False
myfont = pygame.font.SysFont("comicsansms", 16)
throttle = myfont.render("Throttle:", 1, (255,255,255))
geartext = myfont.render("Gear:", 1, (255,255,255))

gr = myfont.render("R", 1, (255,255,255))
g0 = myfont.render("N", 1, (255,255,255))
g1 = myfont.render("1", 1, (255,255,255))
g2 = myfont.render("2", 1, (255,255,255))
g3 = myfont.render("3", 1, (255,255,255))
g4 = myfont.render("4", 1, (255,255,255))
g5 = myfont.render("5", 1, (255,255,255))
g6 = myfont.render("6", 1, (255,255,255))
g7 = myfont.render("7", 1, (255,255,255))
g8 = myfont.render("8", 1, (255,255,255))
g9 = myfont.render("9", 1, (255,255,255))

p1 = myfont.render("10%", 1, (255,255,255))
p2 = myfont.render("20%", 1, (255,255,255))
p3 = myfont.render("30%", 1, (255,255,255))
p4 = myfont.render("40%", 1, (255,255,255))
p5 = myfont.render("50%", 1, (255,255,255))
p6 = myfont.render("60%", 1, (255,255,255))
p7 = myfont.render("70%", 1, (255,255,255))
p8 = myfont.render("80%", 1, (255,255,255))
p9 = myfont.render("90%", 1, (255,255,255))
p10 = myfont.render("100%!", 1, (255,255,255))

gear = 0
gear2 = 0
gear3 = 0

reverse1 = 0
reverse2 = 0

couple = False
while not done:
        for event in pygame.event.get():
                screen.fill((200,75,0))
                if event.type == pygame.QUIT:
                        done = True
                        pygame.quit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LSHIFT and gear < 6 and couple == False:
                                gear = gear + 1
                        if event.key == pygame.K_LCTRL and gear > 0 and couple == False:
                                gear = gear - 1
                        if event.key == pygame.K_QUOTE and gear2 < 6 and couple == False:
                                gear2 = gear2 + 1
                        if event.key == pygame.K_RIGHTBRACKET and gear2 > 0 and couple == False:
                                gear2 = gear2 - 1

                        if event.key == pygame.K_LSHIFT and gear < 6 and couple == True:
                                gear = gear + 1
                                gear2 = gear2 + 1
                        if event.key == pygame.K_LCTRL and gear > 0 and couple == True:
                                gear = gear - 1
                                gear2 = gear2 - 1
                        if event.key == pygame.K_5 and couple == False and gear == gear2:
                                couple = True
                        if event.key == pygame.K_6 and couple == True:
                                couple = False
                        if event.key == pygame.K_w and couple == False:
                                if gear == 1:
                                       ser.write("b")
                                       screen.blit(p1, (100, 150))
                                if gear == 2:
                                        ser.write("c")
                                        screen.blit(p2, (100, 150))
                                if gear == 3:
                                        ser.write("d")
                                        screen.blit(p3, (100, 150))
                                if gear == 4:
                                        ser.write("e")
                                        screen.blit(p4, (100, 150))
                                if gear == 5:
                                        ser.write("f")
                                        screen.blit(p5, (100, 150))
                                if gear == 6:
                                        ser.write("g")
                                        screen.blit(p6, (100, 150))
                                if gear == 7:
                                        ser.write("h")
                                        screen.blit(p7, (100, 150))
                                if gear == 8:
                                        ser.write("i")
                                        screen.blit(p8, (100, 150))
                                if gear == 9:
                                        ser.write("j")
                                        screen.blit(p9, (100, 150))

                        if event.key == pygame.K_w and couple == True:
                                if gear == 1:
                                       ser.write("b")
                                       screen.blit(p1, (100, 150))
                                if gear == 2:
                                        ser.write("c")
                                        screen.blit(p2, (100, 150))
                                if gear == 3:
                                        ser.write("d")
                                        screen.blit(p3, (100, 150))
                                if gear == 4:
                                        ser.write("e")
                                        screen.blit(p4, (100, 150))
                                if gear == 5:
                                        ser.write("f")
                                        screen.blit(p5, (100, 150))
                                if gear == 6:
                                        ser.write("g")
                                        screen.blit(p6, (100, 150))
                                if gear == 7:
                                        ser.write("h")
                                        screen.blit(p7, (100, 150))
                                if gear == 8:
                                        ser.write("i")
                                        screen.blit(p8, (100, 150))
                                if gear == 9:
                                        ser.write("j")
                                        screen.blit(p9, (100, 150))
                                if gear2 == 1:
                                       ser.write("l")
                                       screen.blit(p1, (575, 150))
                                if gear2 == 2:
                                        ser.write("m")
                                        screen.blit(p2, (575, 150))
                                if gear2 == 3:
                                        ser.write("n")
                                        screen.blit(p3, (575, 150))
                                if gear2 == 4:
                                        ser.write("o")
                                        screen.blit(p4, (575, 150))
                                if gear2 == 5:
                                        ser.write("p")
                                        screen.blit(p5, (575, 150))
                                if gear2 == 6:
                                        ser.write("q")
                                        screen.blit(p6, (575, 150))
                                if gear2 == 7:
                                        ser.write("r")
                                        screen.blit(p7, (575, 150))
                                if gear2 == 8:
                                        ser.write("s")
                                        screen.blit(p8, (575, 150))
                                if gear2 == 9:
                                        ser.write("t")
                                        screen.blit(p9, (575, 150))
                        
                        if event.key == pygame.K_o and couple == False:
                                if gear2 == 1:
                                       ser.write("l")
                                       screen.blit(p1, (575, 150))
                                if gear2 == 2:
                                        ser.write("m")
                                        screen.blit(p2, (575, 150))
                                if gear2 == 3:
                                        ser.write("n")
                                        screen.blit(p3, (575, 150))
                                if gear2 == 4:
                                        ser.write("o")
                                        screen.blit(p4, (575, 150))
                                if gear2 == 5:
                                        ser.write("p")
                                        screen.blit(p5, (575, 150))
                                if gear2 == 6:
                                        ser.write("q")
                                        screen.blit(p6, (575, 150))
                                if gear2 == 7:
                                        ser.write("r")
                                        screen.blit(p7, (575, 150))
                                if gear2 == 8:
                                        ser.write("s")
                                        screen.blit(p8, (575, 150))
                                if gear2 == 9:
                                        ser.write("t")
                                        screen.blit(p9, (575, 150))
                                              

                        if event.key == pygame.K_q:
                                ser.write("8")
                                screen.blit(geartext, (25, 25))
                                screen.blit(gr, (120, 25))
                                if event.key == pygame.K_TAB:
                                        ser.write("7")
                                if event.key == pygame.K_p:
                                        ser.write("9")
                                        screen.blit(geartext, (500, 25))
                                        screen.blit(gr, (600, 25))
                        if event.key == pygame.K_1:
                                ser.write("9")
                        if event.key == pygame.K_2:
                                ser.write("6")
                        if event.key == pygame.K_9:
                                ser.write("8")
                        if event.key == pygame.K_0:
                                ser.write("7")
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w and couple == False:
                                ser.write("a")
                        if event.key == pygame.K_o and couple == False:
                                ser.write("k")
                        if event.key == pygame.K_w and couple == True:
                                ser.write("a")
                                ser.write("k")
                        
                if gear == 0:
                        ser.write("a")
                        screen.blit(geartext, (25, 25))
                        screen.blit(g0, (70, 25))
                        screen.blit(throttle, (25, 150))
                if gear2 == 0:
                        ser.write("k")
                        screen.blit(geartext, (500, 25))
                        screen.blit(g0, (550, 25))
                        screen.blit(throttle, (500, 150))

                if gear == 1:
                        screen.blit(geartext, (25, 25))
                        screen.blit(g1, (70, 25))
                        screen.blit(throttle, (25, 150))
                if gear == 2:
                        screen.blit(geartext, (25, 25))
                        screen.blit(g2, (70, 25))
                        screen.blit(throttle, (25, 150))
                if gear == 3:
                        screen.blit(geartext, (25, 25))
                        screen.blit(g3, (70, 25))
                        screen.blit(throttle, (25, 150))
                if gear == 4:
                        screen.blit(geartext, (25, 25))
                        screen.blit(g4, (70, 25))
                        screen.blit(throttle, (25, 150))
                if gear == 5:
                        screen.blit(geartext, (25, 25))
                        screen.blit(g5, (70, 25))
                        screen.blit(throttle, (25, 150))
                if gear == 6:
                        screen.blit(geartext, (25, 25))
                        screen.blit(g6, (70, 25))
                        screen.blit(throttle, (25, 150))
                if gear == 7:
                        screen.blit(geartext, (25, 25))
                        screen.blit(g7, (70, 25))
                        screen.blit(throttle, (25, 150))
                if gear == 8:
                        screen.blit(geartext, (25, 25))
                        screen.blit(g8, (70, 25))
                        screen.blit(throttle, (25, 150))
                if gear == 9:
                        screen.blit(geartext, (25, 25))
                        screen.blit(g9, (70, 25))
                        screen.blit(throttle, (25, 150))       


                if gear2 == 1:
                        screen.blit(geartext, (500, 25))
                        screen.blit(g1, (550, 25))
                        screen.blit(throttle, (500, 150))
                if gear2 == 2:
                        screen.blit(geartext, (500, 25))
                        screen.blit(g2, (550, 25))
                        screen.blit(throttle, (500, 150))
                if gear2 == 3:
                        screen.blit(geartext, (500, 25))
                        screen.blit(g3, (550, 25))
                        screen.blit(throttle, (500, 150))
                if gear2 == 4:
                        screen.blit(geartext, (500, 25))
                        screen.blit(g4, (550, 25))
                        screen.blit(throttle, (500, 150))
                if gear2 == 5:
                        screen.blit(geartext, (500, 25))
                        screen.blit(g5, (550, 25))
                        screen.blit(throttle, (500, 150))
                if gear2 == 6:
                        screen.blit(geartext, (500, 25))
                        screen.blit(g6, (550, 25))
                        screen.blit(throttle, (500, 150))
                if gear2 == 7:
                        screen.blit(geartext, (500, 25))
                        screen.blit(g7, (550, 25))
                        screen.blit(throttle, (500, 150))
                if gear2 == 8:
                        screen.blit(geartext, (500, 25))
                        screen.blit(g8, (550, 25))
                        screen.blit(throttle, (500, 150))
                if gear2 == 9:
                        screen.blit(geartext, (500, 25))
                        screen.blit(g9, (550, 25))
                        screen.blit(throttle, (500, 150))
        pygame.display.update()
        pygame.display.flip()
pygame.quit()
