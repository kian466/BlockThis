"""
'Block This' Game
"""
import arcade
import random

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Block This"
# Constants used to scale our sprites from their original size
ENEMY_SCALING = 1
PLAYER_SCALING = 1
TILE_SCALING = 0.5
BOW_SCALING = 1.25 
SHIELD_SCALING = 0.70
ARROW_SCALING = 0.75
PYRAMID_SCALING = 4
SUN_SCALING = 3
ARROW_SPEED = 5
SQUARE_SCALING = 0.45

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites
        self.wall_list = None
        self.player_list = None
        self.bow_list = None
        self.shield_list = None
        self.arrow_list = None
        self.enemy_list = None
        self.pyramid_list = None
        self.sun_list = None
        self.square_list = None
        self.score = 0
        # Separate variable that holds the player sprite
        self.player_sprite = None
        
        arcade.set_background_color(arcade.color.ARYLIDE_YELLOW)
    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bow_list = arcade.SpriteList()
        self.shield_list = arcade.SpriteList()
        self.arrow_list = arcade.SpriteList()
        self.pyramid_list = arcade.SpriteList()
        self.sun_list = arcade.SpriteList()
        self.square_list = arcade.SpriteList()
        self.score = 0
        # Set up the enemy at specified coordinates
        image_source = "C:\\Users\\kians\\Desktop\\robot_idle.png"
        self.enemy_sprite = arcade.Sprite(image_source, ENEMY_SCALING)
        self.enemy_sprite.center_x = 64
        self.enemy_sprite.center_y = 128
        self.enemy_list.append(self.enemy_sprite)
        #Set up the player at specified coordinates
        image_source_2 = "C:\\Users\\kians\\Desktop\\maleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source_2, PLAYER_SCALING)
        self.player_sprite.center_x = 936
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)
        # Background image and center
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/sandCenter.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)
        # Bow image and position
        coordinate_list_bow = [[95,110]]
        for coordinates in coordinate_list_bow:
            bow = arcade.Sprite('C:\\Users\\kians\\Desktop\\item_bow.png', BOW_SCALING)
            bow.position = coordinates
            self.bow_list.append(bow)
        # Sun image and postion
        coordinate_list_sun = [[487,500]]
        for coordinates1 in coordinate_list_sun:
            sun = arcade.Sprite('C:\\Users\\kians\\Desktop\\particleYellow_4.png', SUN_SCALING)
            sun.position = coordinates1
            self.sun_list.append(sun)
        # Pyramids image and position
        coordinate_list_pyramids = [[500,150],[300,100],[700,100]]
        for coordinates2 in coordinate_list_pyramids:
            pyramid = arcade.Sprite('C:\\Users\\kians\\Desktop\\piramid.png', PYRAMID_SCALING)
            pyramid.position = coordinates2 
            self.pyramid_list.append(pyramid)
        coordinate_list_squares = [[890,80], [890,110], [890,140]]
        for coordinates3 in coordinate_list_squares:
            square = arcade.Sprite('C:\\Users\\kians\\Desktop\\platformPack_tile009.png', SQUARE_SCALING)
            square.position = coordinates3
            self.square_list.append(square)
    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 453, 615, arcade.color.BLACK, 20)
        # Draw our sprites
        self.sun_list.draw()
        self.pyramid_list.draw()
        self.wall_list.draw()
        self.enemy_list.draw()
        self.player_list.draw()
        self.arrow_list.draw()
        self.bow_list.draw()
        self.shield_list.draw()
        self.square_list.draw()
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        
        # Create an arrow
        arrow = arcade.Sprite("C:\\Users\\kians\\Desktop\\item_arrow.png", ARROW_SCALING)
        #angle of arrow is horizontal
        arrow.angle = 0
        # Speed of the arrow
        arrow.change_x = ARROW_SPEED
        # Possible position of the arrow
        arrow.center_x = 64
        arrow.top = random.choice([80,110,140])
        self.arrow_list.append(arrow)
        # Create a shield
        shield = arcade.Sprite("C:\\Users\\kians\\Desktop\\item_.png", SHIELD_SCALING)       
        # Shield position where mouse clicks
        shield.position = [x,y]
        self.shield_list.append(shield)
    def on_update(self, delta_time):
        """ Movement and game logic """
  
        # Call update on arrow sprites
        self.arrow_list.update()
        # Loop through each bullet
        for arrow in self.arrow_list:
           # Check this arrow to see if it hit a shield
            hit_list = arcade.check_for_collision_with_list(arrow, self.shield_list)
           # Check this arrow to see if it hits the player
            hit_list1 = arcade.check_for_collision_with_list(arrow, self.player_list)
            # If it hits shield, get rid of the arrow
            if len(hit_list) > 0:
                arrow.remove_from_sprite_lists()
            # If it hits player, get rid of arrow, shield, and score becomes 0
            if len(hit_list1) > 0:
                arrow.remove_from_sprite_lists()
                for shield in self.shield_list:
                    shield.remove_from_sprite_lists()
                self.score = 0
            # For every shield we hit, add to the score and remove the shield
            for shield in hit_list:
                shield.remove_from_sprite_lists()
                self.score += 1
            # If the arrow flies off-screen, remove it.
            if arrow.top > SCREEN_WIDTH:
                arrow.remove_from_sprite_lists()
                
def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()