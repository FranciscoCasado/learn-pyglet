from pyglet import resource

resource.path = ["../resources"]
resource.reindex()


player_img = resource.image("ship.png")
bullet_img = resource.image("bullet.png")
asteroid_img = resource.image("asteroid.png")


def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
    
    
center_image(player_img)
center_image(bullet_img)
center_image(asteroid_img)