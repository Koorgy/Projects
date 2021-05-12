import pygame

pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Grape story")

walkRight = [pygame.image.load('D:\Projects\client\gig1.png'), pygame.image.load('D:\Projects\client\gig2.png'), pygame.image.load('D:\Projects\client\gig3.png'), pygame.image.load('D:\Projects\client\gig4.png'), pygame.image.load('D:\Projects\client\gig5.png'), pygame.image.load('D:\Projects\client\gig6.png')]

walkLeft = [pygame.image.load('D:\Projects\client\lef1.png'), pygame.image.load('D:\Projects\client\lef2.png'), pygame.image.load('D:\Projects\client\lef3.png'), pygame.image.load('D:\Projects\client\lef4.png'), pygame.image.load('D:\Projects\client\lef5.png'), pygame.image.load('D:\Projects\client\lef6.png')]

bg = pygame.image.load('D:\Projects\client\gg.jpg')
playerStand = pygame.image.load('D:\Projects\client\idle.png')

clock = pygame.time.Clock()

x = 50
y = 425
WIGHT = 60
HEIGHT = 71
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = "right"

class shoot():
	def __init__(self, x, y, radius, color, facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing
		self.vel = 8 * facing

	def draw(self, win):
		pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

def drawWindow():
	global animCount
	win.blit(bg,(0,0))

	if animCount + 1 >= 30:
		animCount = 0
	
	if left:
		win.blit(walkLeft[animCount // 5], (x,y))
		animCount += 1
	elif right:
		win.blit(walkRight[animCount // 5], (x,y))
		animCount += 1
	else:
		win.blit(playerStand, (x,y))

	for bullet in bullets:
		bullet.draw(win)

	pygame.display.update()

run = True
bullets = []

while run:
	clock.tick(30)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	for bullet in bullets:
		if bullet.x < 500 and bullet.x > 0:
			bullet.x += bullet.vel
		else:
			bullets.pop(bullets.index(bullet))

	keys = pygame.key.get_pressed()

	if keys[pygame.K_f]:
		if lastMove == "right":
			facing = 1
		else:
			facing = -1
		if len(bullets) < 5:
			bullets.append(shoot(round(x + WIGHT // 2), round(y + HEIGHT // 2), 5, (255,0,0), facing))

	if keys[pygame.K_LEFT] and x > 5:
		x -= speed
		left = True
		right = False
		lastMove = "left"
	elif keys[pygame.K_RIGHT] and x < 500 - WIGHT - 5:
		x += speed
		left = False
		right = True
		lastMove = "right"
	else:
		left = False
		right = False
		animCount = 0
	if not(isJump):
		if keys[pygame.K_SPACE]:
			isJump = True
	else:
		if jumpCount >= -10:
			if jumpCount < 0:
				y += (jumpCount ** 2) / 2
			else:
				y -= (jumpCount ** 2) / 2
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10
	drawWindow()

pygame.quit()