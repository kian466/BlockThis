import arcade 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 
SCREEN_TITLE = "Catch This"
def draw_background():
    arcade.draw_lrtb_rectangle_filled(0,
                                     SCREEN_WIDTH,
                                     SCREEN_HEIGHT/3,
                                     0,
                                     arcade.color.ARYLIDE_YELLOW)
    arcade.draw_lrtb_rectangle_filled(0,
                                     SCREEN_WIDTH,
                                     SCREEN_HEIGHT,
                                     SCREEN_HEIGHT*(1/3),
                                     arcade.color.CADMIUM_ORANGE)
def draw_pyramids(x,y):
    arcade.draw_triangle_filled(x + 320, y,
                                x, y - 400,
                                x + 640, y - 400,
                                arcade.color.DARK_TAN)
def draw_pyramids_outline(x,y):
    arcade.draw_triangle_outline(x + 320, y,
                                x, y - 400,
                                x + 640, y - 400,
                                arcade.color.BLACK)
def draw_sun(x,y):
    arcade.draw_circle_filled(x, y, 200, arcade.color.YELLOW)
def draw_position(x,y):
    arcade.draw_point(x, y, arcade.color.RED, 30)
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.start_render()
    draw_background()
    draw_sun(405,500)
    draw_pyramids(200,550)
    draw_pyramids(0,550)
    draw_pyramids_outline(100,500)
    draw_pyramids(100,500)
    draw_position(50,50)
    draw_position(760,50)
    arcade.finish_render()
    arcade.run()
if __name__ == "__main__":
    main()