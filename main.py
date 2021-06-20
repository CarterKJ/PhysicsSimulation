import pygame, sys, pymunk

def create_circle(space, pos):
    body = pymunk.Body(1,100,body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body,80)
    space.add(body,shape)
    return shape


def draw_circles(circles):
    for circle in circles:
        pos_x = int(circle.body.position.x)
        pos_y = int(circle.body.position.y)
        pygame.draw.circle(screen,(153, 170, 181),(pos_x,pos_y),80)

def static_ball(space, pos):
    body = pymunk.Body(body_type= pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,50)
    space.add(body,shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen, (153, 170, 181), (pos_x, pos_y), 50)


pygame.init()
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,500)

circles = []

balls = []




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                circles.append(create_circle(space,event.pos))
            else:
                balls.append(static_ball(space, event.pos))


    screen.fill((44,47,51))
    draw_circles(circles)
    draw_static_ball(balls)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)
