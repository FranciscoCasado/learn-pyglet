import pyglet

from game import resources, load


game_window = pyglet.window.Window(800, 600)
main_batch = pyglet.graphics.Batch()

score_label = pyglet.text.Label(text="Score: 0", x=10, y=460, batch=main_batch)
level_label = pyglet.text.Label(
    text="Asteroids",
    x=game_window.width // 2,
    y=game_window.height // 2,
    anchor_x="center",
    batch=main_batch,
)

player_ship = load.player(batch=main_batch)
asteroids = load.asteroids(3, player_ship.position, batch=main_batch)

game_objects = [player_ship] + asteroids
def update(dt):
    for obj in game_objects:
        obj.update(dt)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
