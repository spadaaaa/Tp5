"""
TP5
Adrielle Spada
"""

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "TP5 – Dessin avec Arcade"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()

arcade.draw.draw_lrbt_rectangle_filled(
    2,
    SCREEN_WIDTH,
    2,
    SCREEN_HEIGHT / 1.5,
    arcade.csscolor.DARK_GREY)

arcade.draw.draw_circle_filled(100, 300, 30, arcade.color.RED, num_segments=14, tilt_angle=35)
arcade.draw.draw_circle_outline(100, 300, 30, arcade.color.BLACK, num_segments=8)

arcade.draw.draw_circle_filled(200, 300, 30, arcade.color.RED, num_segments=14, tilt_angle=35)
arcade.draw.draw_circle_outline(200, 300, 30, arcade.color.BLACK, num_segments=8)

arcade.draw.draw_ellipse_filled(100, 300, 20, 55, arcade.color.BROWN, num_segments=15, tilt_angle=40)
arcade.draw.draw_ellipse_filled(200, 300, 20, 55, arcade.color.BROWN, num_segments=15, tilt_angle=40)

arcade.draw.draw_arc_filled(400, SCREEN_HEIGHT / 2 + 1, 200, 550, arcade.csscolor.PINK, 0, 180)

y = SCREEN_HEIGHT / 2 + 40
arcade.draw.draw_triangle_filled(400, y + 238,
                           300, y - 40,
                           500, y - 40,
                           arcade.color.INDIAN_YELLOW)

arcade.draw.draw_line(SCREEN_WIDTH - 800, SCREEN_HEIGHT - 500, SCREEN_WIDTH, SCREEN_HEIGHT - 500, arcade.color.BANANA_YELLOW, 8)

points = [(200, 315), (195, 335), (207, 350)]
arcade.draw.draw_polygon_filled(points, arcade.color.AERO_BLUE)

points = [(100, 315), (200, 315), (150, 330)]
arcade.draw.draw_polygon_filled(points, arcade.color.BLACK)

affichage = arcade.Text("Promenade dehors en vélo avec un obstacle.", 500, SCREEN_HEIGHT - 40, arcade.color.JAPANESE_INDIGO)
affichage.draw()


arcade.finish_render()

arcade.run()
