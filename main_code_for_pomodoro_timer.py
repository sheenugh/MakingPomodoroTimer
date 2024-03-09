# Delima, Sheena Mae D.
# BSCPE 1-2
# ---------------------------------------------------

# - Reference/Credits by:
# https://youtu.be/6oJMd6FWUB8?si=y-f7aTlij-ag1uPd
# ---------------------------------------------------

# - Direction or Instruction
# Find any interested existing python project in YouTube. Follow the instructions or the code presented on the video. 
# Then after imitating the code, run it to test if it works. After that, create a demo.
# A demo that will explain a little bit about the code you've imitate from someone or on YouTube.
# No need to modify
# Add some details, wherein where you can apply the knowledge you have gain by following the video, or where can be your program can be applied or the benefits of it.


# ========= PSEUDO CODE =========
# || PACKAGES AND/OR LIBRARIES ||
import pygame
import sys
from button import Button


# || ACTUAL CODES ||
pygame.init()

# - Screen
width, height = 900, 600 #how big the screen is
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pomodoro Timer")

# - Clock Timer
clock = pygame.time.Clock()

# - Photos as background and button
background = pygame.image.load("datas\\background.png")
white_button = pygame.image.load("datas\\button.png")

# - For font
font = pygame.font.Font("datas\ArialRoundedMTBold.ttf", 120)
timer_text = font.render("25:00", True, "white")
timer_text_rect = timer_text.get_rect(center=(width/2, height/2-25))

# - Buttons 
start_stop_button = Button(white_button, (width/2, height/2+100), 170, 60, "START", 
                    pygame.font.Font("datas\ArialRoundedMTBold.ttf", 20), "#c97676", "#9ab034")
pomodoro_button = Button(None, (width/2-150, height/2-140), 120, 30, "Pomodoro", 
                    pygame.font.Font("datas\ArialRoundedMTBold.ttf", 20), "#FFFFFF", "#9ab034")
short_break_button = Button(None, (width/2, height/2-140), 120, 30, "Short Break", 
                    pygame.font.Font("datas\ArialRoundedMTBold.ttf", 20), "#FFFFFF", "#9ab034")
long_break_button = Button(None, (width/2+150, height/2-140), 120, 30, "Long Break", 
                    pygame.font.Font("datas\ArialRoundedMTBold.ttf", 20), "#FFFFFF", "#9ab034")

# - How long each session is
pomodoro_length = 1500 # 1500 secs / 25 mins
short_break_length = 300 # 300 secs / 5 mins
long_break_length = 900 # 900 secs / 15 mins

# For timer
current_seconds = pomodoro_length
pygame.time.set_timer(pygame.USEREVENT, 1000)
started = False

# - While loop to function
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_stop_button.check_for_input(pygame.mouse.get_pos()):
                if started:
                    started = False
                else:
                    started = True
            if pomodoro_button.check_for_input(pygame.mouse.get_pos()):
                current_seconds = pomodoro_length
                started = False
            if short_break_button.check_for_input(pygame.mouse.get_pos()):
                current_seconds = short_break_length
                started = False
            if long_break_button.check_for_input(pygame.mouse.get_pos()):
                current_seconds = long_break_length
                started = False
            if started:
                start_stop_button.text_input = "STOP"
                start_stop_button.text = pygame.font.Font("datas\ArialRoundedMTBold.ttf", 20).render(
                                        start_stop_button.text_input, True, start_stop_button.base_color)
            else:
                start_stop_button.text_input = "START"
                start_stop_button.text = pygame.font.Font("datas\ArialRoundedMTBold.ttf", 20).render(
                                        start_stop_button.text_input, True, start_stop_button.base_color)
        if event.type == pygame.USEREVENT and started:
            current_seconds -= 1

# - For the screen of the button
    screen.fill("#ba4949")
    screen.blit(background, background.get_rect(center=(width/2, height/2)))

    start_stop_button.update(screen)
    start_stop_button.change_color(pygame.mouse.get_pos())
    pomodoro_button.update(screen)
    pomodoro_button.change_color(pygame.mouse.get_pos())
    short_break_button.update(screen)
    short_break_button.change_color(pygame.mouse.get_pos())
    long_break_button.update(screen)
    long_break_button.change_color(pygame.mouse.get_pos())

    if current_seconds >= 0:
        display_seconds = current_seconds % 60
        display_minutes = int(current_seconds / 60) % 60
    timer_text = font.render(f"{display_minutes:02}:{display_seconds:02}", True, "white")
    screen.blit(timer_text, timer_text_rect)

    pygame.display.update()